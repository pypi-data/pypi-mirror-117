import argparse
import copy
import dgl
import numpy as np
import torch
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import torch.nn.functional as F
from openhgnn.models import build_model
from openhgnn.models import HGNN_AC
from . import BaseFlow, register_flow
from ..tasks import build_task
from ..utils import extract_embed, EarlyStopping


@register_flow("node_classification")
class NodeClassification(BaseFlow):

    """Node classification flows.
    Supported Model: HAN/MAGNN/GTN
    Supported Dataset：ACM

    The task is to classify the nodes of HIN(Heterogeneous Information Network).

    Note: If the output dim is not equal the number of classes, a MLP will follow the gnn model.
    """

    def __init__(self, args):
        super(NodeClassification, self).__init__(args)

        self.args = args
        if self.args.model == 'MAGNN_AC':
            self.model_name = 'MAGNN'
            self.loss_ac = 0.0
        else:
            self.model_name = args.model
        self.device = args.device
        self.task = build_task(args)

        self.hg = self.task.get_graph().to(self.device)
        
        self.num_classes = self.task.dataset.num_classes
        if hasattr(self.task.dataset, 'in_dim'):
            self.args.in_dim = self.task.dataset.in_dim
        if not hasattr(self.task.dataset, 'out_dim') or args.out_dim != self.num_classes:
            print('Modify the out_dim with num_classes')
            args.out_dim = self.num_classes

        self.args.category = self.task.dataset.category
        self.category = self.args.category
        self.model = build_model(self.model_name).build_model_from_args(self.args, self.hg)
        self.model = self.model.to(self.device)
        if self.args.model == 'MAGNN_AC':
            # src_node_type = list(self.model.in_feats.keys())[0]
            # self.hgnn_ac = HGNN_AC(in_dim = self.hg.nodes[src_node_type].data['emb'].shape[1], 
            #                     hidden_dim = self.args.attn_vec_dim, 
            #                     dropout = self.args.dropout, activation = F.elu, 
            #                     num_heads = self.args.num_heads)
            self.hgnn_ac = build_model("HGNN_AC").build_model_from_args(self.args, self.hg)
            
        self.evaluator = self.task.get_evaluator('f1')
        self.loss_fn = self.task.get_loss_fn()
        self.optimizer = (
            torch.optim.Adam(self.model.parameters(), lr=args.lr, weight_decay=args.weight_decay))
        self.patience = args.patience
        self.max_epoch = args.max_epoch

        self.train_idx, self.val_idx, self.test_idx = self.task.get_idx()
        self.labels = self.task.get_labels().to(self.device)
        if self.args.mini_batch_flag:
            # sampler = dgl.dataloading.MultiLayerNeighborSampler([self.args.fanout] * self.args.n_layers)
            sampler = dgl.dataloading.MultiLayerFullNeighborSampler(self.args.n_layers)
            self.loader = dgl.dataloading.NodeDataLoader(
                self.hg.to('cpu'), {self.category: self.train_idx.to('cpu')}, sampler,
                batch_size=self.args.batch_size, device=self.device, shuffle=True, num_workers=0)

    def preprocess(self):
        if self.args.model == 'GTN':
            if hasattr(self.args, 'adaptive_lr_flag') and self.args.adaptive_lr_flag == True:
                self.optimizer = torch.optim.Adam([{'params': self.model.gcn.parameters()},
                                                   {'params': self.model.linear1.parameters()},
                                                   {'params': self.model.linear2.parameters()},
                                                   {"params": self.model.layers.parameters(), "lr": 0.5}
                                                   ], lr=0.005, weight_decay=0.001)
            else:
                # self.model = MLP_follow_model(self.model, args.out_dim, self.num_classes)
                pass
        if self.args.model == 'MAGNN_AC':
            mask_list = []
            feature_list = []
            emb = torch.tensor([])
            i = 0
            for ntype in self.model.in_feats.keys():
                feature_list.append(torch.FloatTensor(self.hg.nodes[ntype].data['feat'].cpu()))
                mask_list.append(torch.tensor(list(range(i, i + self.hg.nodes[ntype].data['feat'].shape[0]))))
                emb = torch.cat((emb,torch.FloatTensor(self.hg.nodes[ntype].data['emb'].cpu())))
                i = self.hg.nodes[ntype].data['feat'].shape[0] + i
            #feature_list = torch.FloatTensor(feature_list).to(self.device)
            feat_keep_idx, feat_drop_idx = train_test_split(np.arange(mask_list[self.args.src_node_type].shape[0]),
                                                            test_size = self.args.feats_drop_rate)
            adj = torch.zeros(emb.shape[0], emb.shape[0])
            for etype in self.model.edge_type_list:
                ntype = list(self.model.in_feats.keys())
                src = ntype.index(etype[0])
                dst = ntype.index(etype[-1])
                for i, j in enumerate(mask_list[src][self.hg.edges(etype = etype)[0]]):
                    adj[j][mask_list[dst][self.hg.edges(etype = etype)[1][i]]] = 1
                
                
            feat_src = feature_list[self.args.src_node_type]
            feat_src_re = self.hgnn_ac(adj[mask_list[self.args.src_node_type]]
                                    [:, mask_list[self.args.src_node_type]][:, feat_keep_idx],
                                    emb[mask_list[self.args.src_node_type]],
                                    emb[mask_list[self.args.src_node_type]][feat_keep_idx],
                                    feat_src[feat_keep_idx])
            self.loss_ac = 1 - F.cosine_similarity(feat_src[feat_drop_idx], feat_src_re[feat_drop_idx, :], 
                                              dim = 1).sum() / feat_src[feat_drop_idx].shape[0]
            
            self.hg = self.hg.to('cpu')
            for i, opt in enumerate(list(self.args.feats_opt)):
                if opt == '1':
                    feat_ac = self.hgnn_ac(adj[mask_list[i]][:, mask_list[self.args.src_node_type]],
                                           emb[mask_list[i]], emb[mask_list[self.args.src_node_type]],
                                           feat_src[mask_list[self.args.src_node_type] 
                                                    - mask_list[self.args.src_node_type][0]])
                    self.hg.nodes[list(self.model.in_feats.keys())[i]].data['feat'] = feat_ac
                    feature_list[i] = feat_ac
            self.hg = self.hg.to(self.device)
        return

    def train(self):
        self.preprocess()
        stopper = EarlyStopping(self.args.patience, self._checkpoint)
        epoch_iter = tqdm(range(self.max_epoch))
        for epoch in epoch_iter:
            if self.args.mini_batch_flag:
                loss = self._mini_train_step()
            else:
                loss = self._full_train_step()
            #if (epoch + 1) % self.evaluate_interval == 0:
            f1, losses = self._test_step()

            train_f1 = f1["train"]
            val_f1 = f1["val"]
            test_f1 = f1['test']
            val_loss = losses["val"]
            # epoch_iter.set_description(
            #     f"Epoch: {epoch:03d}, Train_macro_f1: {train_f1[0]:.4f}, Train_micro_f1: {train_f1[1]:.4f}, Val_macro_f1: {val_f1[0]:.4f}, Val_micro_f1: {val_f1[1]:.4f}, ValLoss:{val_loss: .4f}"
            # )
            print((
                f"Epoch: {epoch:03d}, Loss: {loss:.4f}, Train_macro_f1: {train_f1[0]:.4f}, Train_micro_f1: {train_f1[1]:.4f}, "
                f"Val_macro_f1: {val_f1[0]:.4f}, Test_macro_f1: {test_f1[0]:.4f}, ValLoss:{val_loss: .4f}"
            ))
            early_stop = stopper.step(val_loss, val_f1[0], self.model)
            if early_stop:
                print('Early Stop!\tEpoch:' + str(epoch))
                break

        print(f"Valid_micro_f1 = {stopper.best_score: .4f}, Min_loss = {stopper.best_loss: .4f}")
        stopper.load_model(self.model)
        test_f1, _ = self._test_step(split="test")
        val_f1, _ = self._test_step(split="val")
        print(f"Test_macro_f1 = {test_f1[0]:.4f}, Test_micro_f1: {test_f1[1]:.4f}")
        return dict(Acc=test_f1, ValAcc=val_f1)

    def _full_train_step(self):
        self.model.train()

        logits = self.model(self.hg)[self.category]
        loss = self.loss_fn(logits[self.train_idx], self.labels[self.train_idx])
        if self.args.model == "MAGNN_AC":
            loss = self.args.loss_lambda * self.loss_ac + loss
        self.optimizer.zero_grad()
        loss.backward(retain_graph = True)
        self.optimizer.step()
        return loss.item()

    def _mini_train_step(self,):
        self.model.train()
        loss_all = 0
        for i, (input_nodes, seeds, blocks) in enumerate(self.loader):
            blocks = [blk.to(self.device) for blk in blocks]
            seeds = seeds[self.category]  # out_nodes, we only predict the nodes with type "category"
            # batch_tic = time.time()
            emb = extract_embed(self.model.embed_layer(), input_nodes)
            lbl = self.labels[seeds].to(self.device)
            logits = self.model(blocks, emb)[self.category]
            loss = self.loss_fn(logits, lbl)
            loss_all += loss.item()
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        return loss_all

    def _test_step(self, split=None, logits=None):
        self.model.eval()
        with torch.no_grad():
            logits = logits if logits else self.model(self.hg)[self.category]
            if split == "train":
                mask = self.train_idx
            elif split == "val":
                mask = self.val_idx
            elif split == "test":
                mask = self.test_idx
            else:
                mask = None

            if mask is not None:
                loss = self.loss_fn(logits[mask], self.labels[mask])
                metric = self.task.evaluate(logits[mask].argmax(dim=1).to('cpu'), name='f1', mask=mask)
                return metric, loss
            else:
                masks = {'train': self.train_idx, 'val': self.val_idx, 'test': self.test_idx}
                metrics = {key: self.task.evaluate(logits[mask].argmax(dim=1).to('cpu'), name='f1', mask=mask) for key, mask in masks.items()}
                losses = {key: self.loss_fn(logits[mask], self.labels[mask]) for key, mask in masks.items()}
                return metrics, losses
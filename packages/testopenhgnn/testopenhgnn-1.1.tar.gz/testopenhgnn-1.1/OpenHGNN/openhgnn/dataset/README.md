# Dataset

A dataset is related to a task. So dataset should load not only a heterograph, but also some index involving training, validation and testing.

For now, we have two downstream tasks, which are node classification and link prediction.

#### NodeClassificationDataset

- ##### RDF_NodeCLassification

  - [AIFB/MUTAG/BGS/AM](https://github.com/dmlc/dgl/tree/master/examples/pytorch/rgcn-hetero)

- ##### HIN_NodeCLassification

  - ###### ACM

    |             | author | paper | Subject | Paper-Author | Paper-Subject | Features                      | Train | Val  | Test  |
    | ----------- | ------ | ----- | ------- | ------------ | ------------- | ----------------------------- | ----- | ---- | ----- |
    | acm4GTN     | 5,912  | 3,025 | 57      | 9,936        | 3,025         | 1,902                         | 600   | 300  | 2,125 |
    | acm_han_raw | 17,351 | 4,025 | 72      | 13,407       | 4,025         | 1,903                         | 808   | 401  | 2,816 |
    | acm4NSHE    | 7,167  | 4,019 | 60      | 13,407       | 4,019         | 128(Embedding from deep walk) | -     | -    | -     |

  - ###### academic4HetGNN

    |                 | author | paper  | Venue | Paper-Author | Paper-venue | Paper-paper |
    | --------------- | ------ | ------ | ----- | ------------ | ----------- | ----------- |
    | academic4HetGNN | 28,646 | 21,044 | 18    | 69,311       | 21,044      | 21,357      |

  - ###### DBLP

    |            | author | paper  | Conf | Venue | Paper-Author | Paper-Conf | Paper-Term | Train | Val  | Test  |
    | ---------- | ------ | ------ | ---- | ----- | ------------ | ---------- | ---------- | ----- | ---- | ----- |
    | dblp4HAN   | 4,057  | 14,328 | 20   | 8,789 | 19,645       | 14,328     | 88,420     | 800   | 400  | 2,857 |
    | dblp4GTN   |        |        |      |       |              |            |            |       |      |       |
    | dblp4MAGNN | 4,057  | 14,328 | 20   | 7,723 | 19,645       | 14,328     | 85,810     | 400   | 400  | 3257  |

    

  - ###### IMDB

    |            | Movie | Actor | Director | Movie-Actor | Movie-Director | Train | Val  | Test  |
    | ---------- | ----- | ----- | -------- | ----------- | -------------- | ----- | ---- | ----- |
    | imdb4HAN   | 4,780 | 5,841 | 2,269    | 14,340      | 4,780          | 300   | 300  | 2,687 |
    | imdb4GTN   | 4,661 | 5,841 | 2,270    | 13,983      | 4,661          | 300   | 300  | 2,339 |
    | imdb4MAGNN | 4,278 | 5,257 | 2,081    | 12,828      | 4,278          | 400   | 400  | 3,478 |

- ##### OGB_NodeCLassification

  - [ogbn-mag](https://ogb.stanford.edu/docs/nodeprop/#ogbn-mag)

#### LinkPredictionDataset

- ##### HIN_LinkPrediction

  - ###### academic4HetGNN

- ##### KG_LinkPrediction

  - 'wn18', 'FB15k', 'FB15k-237'

### How to build a new dataset

We use [dgl.heterograph](https://docs.dgl.ai/en/latest/guide/graph-heterogeneous.html#guide-graph-heterogeneous) as our graph data structure.

The API [dgl.save_graphs](https://docs.dgl.ai/en/latest/generated/dgl.save_graphs.html) and  [dgl.load_graphs](https://docs.dgl.ai/en/latest/generated/dgl.load_graphs.html#) can be used in storing graph into the local.

##### The Flow

1. Process your dataset as [dgl.heterograph](https://docs.dgl.ai/en/latest/guide/graph-heterogeneous.html#guide-graph-heterogeneous). 
2. Store as *graph.bin*. Compress as *dataset_name4model_name.zip*
3. Upload the zip file to s3.
4. If the dataset is Heterogeneous Information Network, you can modify the [AcademicDataset](./academic_graph.py) directly. Or you can refer to it building a new *Class Dataset*.

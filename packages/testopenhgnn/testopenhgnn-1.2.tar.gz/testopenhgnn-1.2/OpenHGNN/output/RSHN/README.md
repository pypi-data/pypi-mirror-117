# RSHN[ICDM2019]

-   paper: [Relation Structure-Aware Heterogeneous Graph Neural Network](https://ieeexplore.ieee.org/abstract/document/8970828)
-   Code from author: [RSHN](https://github.com/CheriseZhu/RSHN)

## How to run

- Clone the Openhgnn-DGL

  ```bash
  python main.py -m RSHN -t node_classification -d aifb -g 0
  ```

  If you do not have gpu, set -gpu -1.

  the rdf_dataset is supported.

## Performance: Node classification

| Method               | AIFB      | MUTAG     | BGS       | AM        |
| -------------------- | --------- | --------- | --------- | --------- |
| **RSHN**             | **97.22** | **82.35** | **93.10** | **90.40** |
| **RSHN(dgl)**（best) | **97.22** | **85.29** | **93.10** | **89.39** |

### Dataset: [RDFDataset](../../dataset/#RDF_NodeCLassification)

## TrainerFlow: entity classification trainer

### Model

- *1) Coarsened Line Graph Neural Network (CL-GNN):*
  - We implement the API [coarsened_line_graph](../../sampler/RSHN_sampler.py)
- *2) Heterogeneous Graph Neural Network (H-GNN):*

## Hyper-parameter specific to the model

You can modify the parameters in openhgnn/config.ini

#### Description

```python
# The next two hyper-parameters are used in building the coarsened-line graph.
rw_len = 5
batch_size = 1000
#	edga_layer means number of CL-GNN layers, node_layer means number of H-GNN layers
num_node_layer = 2
num_edge_layer = 1
```

Best config can be found in [best_config](../../utils/best_config.py)

## More

#### Contirbutor

Tianyu Zhao[GAMMA LAB]

#### If you have any questions,

Submit an issue or email to [tyzhao@bupt.edu.cn](mailto:tyzhao@bupt.edu.cn).
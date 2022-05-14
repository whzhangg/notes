# PyTorch Geometric
Pytorch geometric is a package that organize points and graphs data and pervide mini-batches. It also include basic neural network structure that can learn about geometric datas.

Reference: https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html
### Data
A graph can be stored in a `torch_geometric.data.Data` object. Each Data object specify a graph. The following attributes are stored when Data is created:
- *data.x features*: with shape `[num_nodes, num_node_features]`
- *data.edge_index*: graph connectivity with shape `[2, num_edges]` with torch.long as datatype
- *data.edge_attr*: features associated with each edge `[num_edges, num_edge_features]`
- *data.y*: target data of any shape that is associated with a graph. It can be node level: `[num_nodes, *]` or graph level target `[1, *]`
- *data.pos*: the position of the points `[num_nodes, num_dimensions]`

The following is an example of using the Data object:
```python
import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0, 1],
                           [1, 0],
                           [1, 2],
                           [2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index.t().contiguous())
>>> Data(edge_index=[2, 4], x=[3, 1])

print(data.keys)
>>> ['x', 'edge_index']

print(data['x'])
>>> tensor([[-1.0],
            [0.0],
            [1.0]])

for key, item in data:
    print(f'{key} found in data')
>>> x found in data
>>> edge_index found in data

'edge_attr' in data
>>> False

data.num_nodes
>>> 3

data.num_edges
>>> 4

data.num_node_features
>>> 1

data.has_isolated_nodes()
>>> False

data.has_self_loops()
>>> False

data.is_directed()
>>> False

# Transfer data object to GPU.
device = torch.device('cuda')
data = data.to(device)
```

### Dataloader
We can create batches of data using *Dataloader*. Dataloader can be iterated to obtain *batches*. Batches has similar properties as Data, but now with an additional attributes called batch, which specifies which graph does a point belong. 

Basically, our neural network should operate on batches, instead of individual graphs
```python
from torch_geometric.datasets import TUDataset
from torch_geometric.loader import DataLoader

dataset = TUDataset(root='/tmp/ENZYMES', name='ENZYMES', use_node_attr=True)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

for batch in loader:
    batch
    >>> DataBatch(batch=[1082], edge_index=[2, 4066], x=[1082, 21], y=[32])

    batch.num_graphs
    >>> 32
```

### Dataset
We can obtain the common benchmark dataset as following:

```python
from torch_geometric.datasets import QM7b

dataset = QM7b(root = '.')

print(type(dataset))
>>> <class 'torch_geometric.datasets.qm7.QM7b'>
print(dataset[0])
>>> Data(edge_index=[2, 25], edge_attr=[25], y=[1, 14], num_nodes=5)
```

It will automatically download the dataset online and store it in the given directory. A dataset provide a collection of Data objects that can be indexed and iterated. [Reference](https://pytorch-geometric.readthedocs.io/en/latest/notes/create_dataset.html)

### Transformations
We can apply transformations to Dataset and individual Data, see: 
https://pytorch-geometric.readthedocs.io/en/latest/notes/introduction.html#data-transforms 
and 
https://pytorch-geometric.readthedocs.io/en/latest/modules/transforms.html
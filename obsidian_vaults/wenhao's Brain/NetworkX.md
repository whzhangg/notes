# NetworkX

Created: January 23, 2022 9:52 PM
Description: Networkx package for graph datastructure
Type: API

## NetworkX

---

`import networkx as nx`

- **Website:** [https://networkx.org/documentation/stable/index.html](https://networkx.org/documentation/stable/index.html)
- **Citing:** Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, [“Exploring network structure, dynamics, and function using NetworkX”](http://conference.scipy.org/proceedings/SciPy2008/paper_2/), in [Proceedings of the 7th Python in Science Conference (SciPy2008)](http://conference.scipy.org/proceedings/SciPy2008/index.html), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

### Types of Graphs

There are 4 different graphs that can be constructed

1. `nx.Graph()` the basic graph class provide undirected graph
2. `nx.DiGraph()` graphs with directed edges
3. `nx.MultiGraph()` graph that allows multiple undirected edges between pairs of nodes
4. `nx.MultiDiGraph()` directed version of multigraph

### Adding nodes and edged

Any property can be attached to a node, graph or edges, they are specified as **key/value** pairs in an associated attribute dictionary

- Global graph attributes can be specified when the graph is created: `G = nx.Graph(day = “Friday”)`
- `G.add_node(name, *attributes)` create a node in the graph with given attributes associated with it, Node name can be any hashable objects and they do not need to be the same type (internally, their hash are used)
- `G.add_edge(node1, node2)` create an edge at a time, edge attributes can be added as arguments, especially, weight attributes can be specified, which is used for the graph related algorthims.

**To add nodes and edges**

```python
import networkx as nx
G = nx.Graph()
G.add_node("node1", color = "red")
G.add_node("node2", color = "blue")
G.add_node("node3", color = "green")
G.add_edge("node1", "node2", weight = 1.0, description = "first edge")
G.add_edge("node1", "node3", weight = 2.0, description = "second edge")
```

### Visiting graph information

A read only access is provided by class properties:

- `G.nodes` set of all the nodes
- `G.edges` set of all the edges
- `G.adj` neighbors of a given node
- `G.degree` the number of edges connected to the given node

**Subscript notation**

Underneath the hood, a graph is stored as “dictionary of dictionaries of dictionaries”

- `G` itself is a dictionary with keys being all the nodes in the graph
- `G[”node1”]` represent a dictionary, with key being the connected nodes and value being edge description
- `G[”node1”][”node2”]` represent a dictionary that contain edge properties

The following is an output of accessing the properties of the graph created above

```python
print(G["node1"])
>> {'node2': {'weight': 1.0, 'description': 'first edge'}, 'node3': {'weight': 2.0, 'description': 'second edge'}}

print(G["node1"]["node2"])
>> {'weight': 1.0, 'description': 'first edge'}

print(G["node1"]["node2"]["description"])
>> first edge

print(G.nodes["node1"])
>> {'color': 'red'}
```

**Adding attirbutes**

To add attributes to graph, nodes or edges, the most standard way is to get the components using G.nodes, G.edges etc. which can be considered as dictionaries containing the information of the attributes:

```python
# graph
G.graph['day'] = "Monday"
# nodes
G.nodes[1]['room'] = 714
# edges
G[1][2]['weight'] = 4.7
G.edges[3, 4]['weight'] = 4.2
```

**Removing elements from a graph**

Graph object provide methods to remove the components in a graph:

- `Graph.remove_node(node1)`: remove node1
- `Graph.remove_nodes_from(node1)`: remove nodes connecting to node1
- `Graph.remove_edge(node1, node2)`: remove the edge connecting to node1 and node2

### Drawing Graphs

To draw a graph with matplotlib, we can use nx.draw() method, providing the axs object;

`nx.draw(G, pos = None, ax = None, **kwds)`

- **ax** is a matplotlib axes object
- **pos** is a dictionary with **nodes as keys and positions as values**, layouts can be computed by by position algorithms provided by the networkx package: [https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout](https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout)
    
    Two common layout scheme is:
    
    - nx,kamada_kawai_layout(G): all nodes are separated by distance that is approximately proportional to weight
    - nx.spring_layout(G): all nodes are connected by spring with force porportional to the weight ( larger the weight, shorter the distance)
- optional parameters can be found [here](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html#networkx.drawing.nx_pylab.draw_networkx)

As an example, this is a script that plot the graph by matplotlib:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
fig.set_size_inches(8, 8) 
axs = fig.subplots()

edge_to_draw = self._graph.edges()

position = nx.kamada_kawai_layout(self._graph)
xs = [ v[0] for v in position.values()]
ys = [ v[1] for v in position.values()]
axs.set_xlim( min(xs) - (max(xs) - min(xs))/6, max(xs) + (max(xs) - min(xs))/6 )  # we set the range of the figure
axs.set_ylim( min(ys) - (max(ys) - min(ys))/6, max(ys) + (max(ys) - min(ys))/6 )  # so that the graph is approximately 
                                                                                  #in the center

nx.draw(self._graph, pos = position, 
                     ax = axs, node_color='r', edge_color='#d1d1d1', edgelist = edge_to_draw, 
                     with_labels = True, node_size = 200, font_size = 6) 
# edgelist specifies which edge to be draw
fig.savefig(filename)
```

## Additional Reference

[https://towardsdatascience.com/customizing-networkx-graphs-f80b4e69bedf](https://towardsdatascience.com/customizing-networkx-graphs-f80b4e69bedf)
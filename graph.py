"""Graph implementation."""

from ipdb import set_trace


class Node(object):
  """Represents a node of a graph."""
  def __init__(self, label):
    self.label = label

  def __repr__(self):
    return 'Node(%s)' % label

  __str__ = __repr__


class Edge(tuple):
  def __new__(cls, node_1, node_2):
    return tuple.__new__(cls, (node_1, node_2))

  def __repr__(self, node_1, node_2):
    return 'Edge(%s, %s)' % repr(self[0], self[1])

  __str__ = __repr__


class Graph(dict):
  def __init__(self, nodes=None, edges=None):
    # Maybe redundant after below handling.
    if edges and not nodes:
      raise ValueError('Edges can not be added without nodes!')

    # self.nodes = nodes or []
    nodes = nodes or []
    edges = edges or []

    map(self.add_node, nodes)
    map(self.add_edge, edges)

  def add_node(self, node):
    self[node] = {}

  def add_edge(self, edge):
    """Adds a bidirectional edge to the Graph."""
    node_1, node_2 = edge
    try:
      self[node_1][node_2] = edge
      self[node_2][node_1] = edge
    except KeyError as e:
      print 'Edges must have their endpoint nodes in the Graph!'
      raise e


if __name__ == '__main__':
  set_trace()

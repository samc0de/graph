"""Graph implementation."""
# TODO: Investigate numpy arrays.

import itertools
import logging
from ipdb import set_trace


class Node(object):
  """Represents a node of a graph."""
  def __init__(self, label):
    self.label = label

  def __repr__(self):
    return 'Node(%s)' % label

  __str__ = __repr__


# TODO: Support weights.
# TODO: Support directed edges.
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
    map(self.add_node, nodes or [])
    map(self.add_edge, edges or [])

  def add_node(self, node):
    self[node] = {}

  def add_edge(self, edge=None, node_1=None, node_2=None):
    """Adds a bidirectional edge to the Graph."""
    # Validate args here.
    if not node_1 or node_2:
      node_1, node_2 = edge

    try:
      self[node_1][node_2] = edge
      self[node_2][node_1] = edge
    except KeyError as e:
      logging.error('Edges must have their endpoint nodes in the Graph!')
      raise e

  def get_shortest_path(self, node_1, node_2):
    """Gets shortest paths between given two nodes."""
    raise NotImplementedError()

  def get_edge(self, node_1=None, node_2=None, edge=None):
    # Validate args here.
    if not node_1 or node_2:
      node_1, node_2 = edge

    try:
      return self[node_1][node_2]
    except KeyError as e:
      logging.error('No such edge in this graph.')

  def remove_edge(self, edge):
    node_1, node_2 = edge
    edge_in_graph = self.get_edge(node_1, node_2)
    if edge_in_graph:
      logging.warn('Removing edge %s', edge)
      self[node_1].pop(node_2)
    # Or simply for all 4 lines:
    # self[node_1].pop(node_2, None)

  @property
  def nodes(self):
    return self.keys()

  @property
  def edges(self):
    edges = set()
    for node_1, dest in self.iteritems():
      edges.update(dest.values())

    return edges

  def complete_graph(self):
    for node_1, node_2 in itertools.combinations(self.nodes, 2):
      self.add_edge(Edge((node_1, node_2)))

if __name__ == '__main__':
  set_trace()

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
          return
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check that v1 and v2 exist in the vertices dictionary
        if v2 not in self.vertices[v1] and v2 in self.vertices and v1 in self.vertices:
          # add v2 to the vertices at v1
          self.vertices[v1].add(v2)
        else:
          # raise an exception and give an error
          raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    # instantiate a new graph object
  graph = Graph()
    # loop over all pairs in ancestors
  for pair in ancestors:
        # add pair[0] and pair[1] to the graph
      graph.add_vertex(pair[0])
      graph.add_vertex(pair[1])
        # build the edges in reverse
      graph.add_edge(pair[1], pair[0])
    # Do a BFS (with paths)
    # create a queue
  q = Queue()
    # enqueue starting node inside a list
  q.enqueue([starting_node])
    # set a max path length to 1
  max_path_length = 1
    # set initial earlyest ancestor
  earliest_ancestor = -1
    # while queue has contents
  while q.size() > 0:
        # dequeue the path
      path = q.dequeue()
        # get the last vert
      vert = path[-1]
        # if path is longer or equal and the value is smaller, or if the path is longer
      if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the vert
          earliest_ancestor = vert
            # set the max path length to the len of the path
          max_path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of vert
      for neighbor in graph.vertices[vert]:
            # make a copy of the path
          path_copy = list(path)
            # append neighbor to the coppied path
          path_copy.append(neighbor)
            # then enqueue the copied path
          q.enqueue(path_copy)
    # return earliest ancestor
  return earliest_ancestor
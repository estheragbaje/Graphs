# create a class Queue
class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


# create a class Graph
class Graph:
    """ 
        Represent a graph as a dictionary of verts 
        mapping labels to edges 
    
    """
    def __init__(self):
        self.vertices = {}
    
    # def add_vertex(self, vertex_id):
    #     if vertex_id not in self.vertices:
    #         self.vertices[vertex_id] = set()
    
    # def add_edge(self, v1, v2):
    #     if v1 in self.vertices and v2 in self.vertices:
    #         self.vertices[v1].add(v2)
    #     else:
    #         raise KeyError("That vertex does not exist!")

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
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

def earliest_ancestor(ancestors, starting_node):
    # instantiate a new graph object
    graph = Graph()
    # loop over all pairs in ancestors
    for pair in ancestors:
      # add pair[0] and pair[1] to the graph
      graph.add_vertex(pair[0])
      graph.add_vertex(pair[1])
      # build the edges in reverse
      graph.add_edge(pair[1], pair[0]) # can this be pair[0], pair[1]?

      # Do a BFS (with paths)
      q = Queue()
      # enqueue starting node inside a list
      q.enqueue([starting_node])
      # set a max path length to 1
      max_path_length = 1
      # set initial earliest ancestor
      earliest_ancestor = -1
      # while queue has contents
      while q.size() > 0:
        # dequeue the path
        path = q.dequeue()
        # get the last vertex
        last_vertex = path[-1]
        # if path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_length and last_vertex < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the last_vertex
            earliest_ancestor = last_vertex
            # set the max path length to the len of the path
            max_path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of last_vertex
        for neighbor in graph.vertices[last_vertex]:
            # make a copy of the path
            path_copy = list(path)
            # append neighbor to the coppied path
            path_copy.append(neighbor)
            # then enqueue the copied path
            q.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor


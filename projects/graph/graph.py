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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check that v1 and v2 exist in the vertices dictionary
        if v1 in self.vertices and v2 in self.vertices:
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create empty queue
        q = Queue()
        # enqueue the starting vertex id
        q.enqueue(starting_vertex_id)
        # create a set to store our visited vertices
        visited = set()

        # while queue is not empty (len is greater than 0)
        while q.size() > 0:
          # dequeue the first vertex
          v = q.dequeue()
          # if that vertex has not been visited
          if v not in visited:
            # mark as visited and print for debugging
            visited.add(v)
            print(v) # for debugging
            # iterate over the child vertices of the current vertex
            for next_vertex in self.vertices[v]:
              # enqueue the next vertex
              q.enqueue(next_vertex)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack
        s = Stack()
        # push the starting vertex id
        s.push(starting_vertex_id)
        # create a set to store our visited vertices
        visited = set()

        # while stack is not empty (len greater than 0)
        while s.size > 0 :
          # pop the first vertex
          v = s.pop()
          # if that vertex has not been visited
          if v not in visited:
            # mark as visited and print for debugging
            visited.add(v)
            print(v) # for debugging
            # iterate over the child vertices of the current vertex
            for next_vertex in self.vertices[v]:
              # push the next vertex
              s.push(next_vertex)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # enqueue A PATH TO the starting vertex 
        q.enqueue(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
          # Dequeue the first PATH eg -> [a, b, c, r, g]
          path = q.dequeue()
          # Grab the last vertex from the PATH
          last_vertex = path[-1]
          # If the last vertex has not been visited...
          if last_vertex not in visited:
            # CHECK IF IT'S THE TARGET
            if last_vertex == destination_vertex:
              return path
            # Mark it as visited...
            last_vertex in visited
            # Then add A PATH TO its neighbors to the back of the queue
            visited.add(last_vertex)
            for neighbor in self.vertices[last_vertex]:
              # create new path list
              new_path = list(path)
              # APPEND THE NEIGHBOR TO THE BACK
              new_path.append(neighbor)






    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Empty dictionary 
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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # print('neighbor',self.vertices[vertex_id])
        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue 
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to stored visited nodes
        visited = set()
        # While the queue is not empty ...
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited ....
            if v not in visited:
                print(v)
                # Mark it has been visited
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        print("bft-----------")

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the queue
        s.push(starting_vertex)
        # Create an empty set to stored visited nodes
        visited = set()
        # While the stack is not empty ...
        while s.size() > 0:
            # Pop, the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited ....
            if v not in visited:
                # Mark it has been visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        print("dft------------")
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if node is visited
        if visited is None:
            visited = set()
        # Setbase case 
        # if not visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            # Make as visited
            # Print
            print(starting_vertex)
            # Call Dft_Recursive on each child 
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        print("dft_recursive------------")

                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex (target) in
        breath-first order.
        """
        q = Queue()
        q.enqueue( [starting_vertex] )
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v == destination_vertex:
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        print("bfs------------")
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # Add A PATH TO the starting vertex_id to the stack
        s.push( [starting_vertex] )
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        counter = 0
        while s.size() > 0:
            counter += 1
            print(counter)
            # Pop, the first PATH
            path = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # CHECK IF IT'S THE TARGET
            if v == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    # (Make a copy of the path before adding)
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # Check if starting vertex has been visited
        if starting_vertex not in visited:
        # If not ...
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # If starting_vertex is destination:
            if starting_vertex == destination_vertex:
                return path_copy
                # return path
            # Mark as visited
            # Call DFS recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        print("dfs_recursvie-------")

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

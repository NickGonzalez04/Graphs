# 1. Translate the problem into graph terminology
# Undirected 
# Acyclic
# Path(edge) Parent-child 
# bfs 
# 2. Build your graph
# 3. Traverse your graph
# nodes are numbers, edges/neighbors are child that differ by one and only one letter


from util import Stack, Queue


class Graph:
    def __init__(self):
        # Create empty dictionary
        self.vertices = {}
    def add_vertex(self, vertex_id):
        # Add vertex as a set if it does not exist 
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_path(self, v1, v2):
        """
        Add a directed path to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            raise IndexError(f"{v1} does not exist")
        elif v2 not in self.vertices:
            raise IndexError(f"{v2} does not exist")
        else:
            raise IndexError("That vertex does not exist!")
    def get_ancestor(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        # Add each vertex
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        # Add paths
        graph.add_path(i[1], i[0])
    print(graph.vertices)
    # Create an empty queue 
    q = Queue()
    # Add the starting vertex_id to the queue
    q.enqueue( [starting_node] )    
    # Set the shortest possible path to 1, will return 1 if it is the shortest
    shortest_path = 1
    # if no earliest ancestor return -1
    earliest_ancestor = -1
    # While the queue is not empty ...
    while q.size() > 0:
        # Dequeue, the first vertex
        path = q.dequeue()
        # Grab the last vertext 
        visited = path[-1]
        if (len(path) >= shortest_path and visited < earliest_ancestor) or (len(path) > shortest_path):
            earliest_ancestor = visited
            shortest_path = len(path)
            

            # Then add all neighbors to the back of the queue
        for ancestors in graph.get_ancestor(visited):
            path_copy = path.copy()
            path_copy.append(ancestors)
            q.enqueue(path_copy)

    return earliest_ancestor





'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```
Write a function that, given the dataset and the ID of an individual in the dataset, 
returns their earliest known ancestor – 
the one at the farthest distance from the input individual. 
If there is more than one ancestor tied for "earliest",
     return the one with the lowest numeric ID. 
If the input individual has no parents, 
    return -1
'''
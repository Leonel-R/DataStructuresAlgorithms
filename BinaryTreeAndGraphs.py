class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

#example of a tree: Node A has left child node B and right child node C
node1 = TreeNode("B")
node2 = TreeNode("C")
# Correct the mistake
root_node = TreeNode("A",node1, node2)

class Graph:
    def __init__(self) -> None:
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, source, target):
        self.vertices[source].append(target)

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
    # Set the data for the vertex
        self.vertices[vertex] = []

    def add_edge(self, source, target, weight):
    # Set the weight
        self.vertices[source].append([target, weight])

#example:
my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge('Toulouse', 'Biarritz', 312)
my_graph.add_edge('Biarritz', 'Paris', 783)

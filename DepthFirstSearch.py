#Process of visiting all nodes in tree or graph: Depth first search and Breadth first search
#DFS:
#in order: left -> current node -> right 

class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    #DFS in order (ascedning values) (O(n))
    def in_order(self, current_node):
        if current_node:
            self.in_order(current_node.left_child)
            print(current_node.data)
            self.in_order(current_node.right_child)
    
    #DFS pre-order traversal  current node -> left  -> right    
    #can be used for creating copies of trees or to get prefix expressions
    def pre_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)

    #DFS post-order traversal  left -> right -> current node        
    #can be used for the deletion of trees or to get prefix expressions
    def post_order(self, current_node):
        if current_node:
            print(current_node.data)
            self.in_order(current_node.left_child)
            self.in_order(current_node.right_child)

#DFS for graphs
class Graph:
    def __init__(self) -> None:
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, source, target):
        self.vertices[source].append(target)
    
#Complexity: O(V + E) - where V is amount of vertexes and E is the amount of edges 
def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)

graph = {
  '0' : ['1','2'],
  '1' : ['0', '2', '3'],
  '2' : ['0', '1', '4'],
  '3' : ['1', '4'],
  '4' : ['2', '3']
}

dfs(set(), graph, '0')

import queue 

class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    #Complexity of O(n)
    def bfs(self):
        if self.root:
            visited_nodes = []
            bfs_queue = queue.SimpleQueue()
            bfs_queue.put(self.root)
            while not bfs_queue.empty():
                current_node = bfs_queue.get()
                visited_nodes.append(current_node.data)
                if current_node.left:
                    bfs_queue.put(current_node.left) 
                if current_node.right:
                    bfs_queue.put(current_node.right)
            return visited_nodes

#BFS for grpahs
class Graph:
    def __init__(self) -> None:
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, source, target):
        self.vertices[source].append(target)
    
#Complexity of O(V + E)    V - # of vertices   E - # of edges  
def bfs(graph,initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)
    
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    return visited_vertices

#BFS
# Target close to  the starting vertex
# Applications: Web crawling, finding shortest path in unweighted graphs, finding connected locations using GPS  

#DFS
#Target far away from the starting vertex
#Applications: Solving puzzles with only one solution(maze), detecting cyles in graphs, finding shortest path in a weighted graph 

#Both search methods are used as a part of more complex algorithms



#Binary Search Tree: 
#left subtree value < root node/ right subtree value > root node
#Much faster than searching/deleting/inserting than arrays and linked lists
class TreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False
    
    def insert(self,data):
        new_node = TreeNode(data)
        if self.root == None:
            self.root = new_node
            return
        else: 
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return 
                    else:
                        current_node = current_node.left_child
                elif data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child
    
    def delete_node(self,root, key):
 
        # pointer to store the parent of the current node
        parent = None
    
        # start with the root node
        current_node = root
    
        # search key in the BST and set its parent pointer
        while current_node and current_node.data != key:
    
            # update the parent to the current node
            parent = current_node
    
            # if the given key is less than the current node, go to the left subtree;
            # otherwise, go to the right subtree
            if key < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
    
        # return if the key is not found in the tree
        if current_node is None:
            return root
    
        # Case 1: node to be deleted has no children, i.e., it is a leaf node
        if current_node.left is None and current_node.right is None:
    
            # if the node to be deleted is not a root node, then set its
            # parent left/right child to None
            if current_node != root:
                if parent.left == current_node:
                    parent.left = None
                else:
                    parent.right = None
    
            # if the tree has only a root node, set it to None
            else:
                root = None
    
        # Case 2: node to be deleted has two children
        elif current_node.left and current_node.right:
    
            # find its inorder successor node
            successor = self.find_min(current_node.right)
    
            # store successor value
            val = successor.data
    
            # recursively delete the successor. Note that the successor
            # will have at most one child (right child)
            self.delete_node(root, successor.data)
    
            # copy value of the successor to the current node
            current_node.data = val
    
        # Case 3: node to be deleted has only one child
        else:
    
            # choose a child node
            if current_node.left:
                child = current_node.left
            else:
                child = current_node.right
    
            # if the node to be deleted is not a root node, set its parent
            # to its child
            if current_node != root:
                if current_node == parent.left:
                    parent.left = child
                else:
                    parent.right = child
    
            # if the node to be deleted is a root node, then set the root to the child
            else:
                root = child
    
        return root

        
    def find_min(self):
        current_node = self.root
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data
    
    def find_max(self):
        current_node = self.root
        while current_node.right_child:
            current_node = current_node.right_child
        return current_node.data



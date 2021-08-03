#binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.data = key
        self.right = None

#create root
class Tree:
    def createNode(self, data):
        return Node(data)

#inserting a node
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node
#inorder traversal
    def traversal_inorder(self, root):
        if root is not None:
            self.traversal_inorder(root.left)
            print(root.data)
            self.traversal_inorder(root.right)
    
#minimum value node
    def minValNode(self, node): #loop down to leftmost leaf
        current = node
        while current.left is not None:
            current = current.left
        return current

#maximum value node
    def maxValNode(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current




#driver code

tree = Tree()
root = tree.createNode(5)
print(root.data)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)

print("inorder ---->")
tree.traversal_inorder(root)


        

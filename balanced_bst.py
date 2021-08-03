#converting normal bst into a balanced binary search tree
#step1 -> inorder traversal and get the elements into an array. The elements will already be sorted 
#as we are doing inroder traversal
#step2 -> from this array construct a BST using recursive method

class Node:
    def __init__(self,data = None):
        self.left = None
        self.right = None
        self.data = data

def storeBSTnodes(root, nodes):
    if root is None:
        return

    storeBSTnodes(root.left,nodes)
    nodes.append(root)
    storeBSTnodes(root.right,nodes)

#rec funtion to construct a binary tree
def buildBinaryTree(nodes,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    node = nodes[mid]
    node.left = buildBinaryTree(nodes,start,mid-1)
    node.right = buildBinaryTree(nodes,mid+1,end)
    return node

def buildTree(root):
    nodes = []
    storeBSTnodes(root,nodes)
    n = len(nodes)
    return buildBinaryTree(nodes,0,n-1)

def preOrder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

if __name__=="__main__":
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    root = buildTree(root)
    preOrder(root)
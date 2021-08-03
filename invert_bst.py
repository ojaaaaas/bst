#inverting a binary tree
#form a mirror image
#left -> right and vice versa
class Node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

def invertBST(root):
    if not root:
        return 
    
    temp = root
    
    temp = root.left
    root.left = root.right
    root.right = temp

    invertBST(root.left)
    invertBST(root.right)

def printTree(root):
    if not root:
        return 
    printTree(root.left)
    print(root.data,end=" ")
    printTree(root.right)

if __name__=="__main__":
    root = Node(2)
    root.left = Node(1)
    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(5)
    printTree(root)
    invertBST(root)
    # printTree(root)



        
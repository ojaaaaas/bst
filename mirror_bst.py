#mirror inorder of a bst
class Node(object):
    def __init__(self, data=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def inorder_mirror(root):
    if root is None:
        return 0
    else:
        inorder_mirror(root.rightChild)
        if root.data is None:
            return 0
        else:
            print(root.data, end=" ")
        inorder_mirror(root.leftChild)

if __name__=="__main__":
    root = Node(2)
    root.leftChild = Node(1)
    root.rightChild = Node(8)
    root.leftChild.leftChild = Node(12)
    root.rightChild.rightChild = Node(9)
    print(inorder_mirror(root))

#diameter of a tree 
class Node(object):
    def __init__(self, data = None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def height(node):
    if node is None:
        return 0
    else:
        leftHeight = height(node.leftChild)
        rightHeight = height(node.rightChild)

    return leftHeight+rightHeight+1

if __name__=="__main__":
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)
    root.rightChild.leftChild = Node(7)
    root.leftChild.leftChild = Node(4)
    root.leftChild.leftChild.leftChild = Node(5)
    

    a = height(root)
    print(a)
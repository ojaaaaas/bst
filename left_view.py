#left view of a bst
class Node(object):
    def __init__(self, data = None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def leftViewUntil(root, level, max_level):
    if root is None:
        return
    
    if (max_level[0] < level):
            print("%d" %(root.data))
            max_level[0] = level
    leftViewUntil(root.leftChild, level+1, max_level)
    leftViewUntil(root.rightChild, level+1, max_level)

def leftView(root):
    max_level = [0]
    leftViewUntil(root, 1, max_level)
    
        

if __name__=="__main__":
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)
    root.leftChild.leftChild = Node(4)
    leftView(root)


        
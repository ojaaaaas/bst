class Node(object):
    def __init__(self, data=None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def inorder(root):
    
    if root is not None:
        inorder(root.leftChild)
        # lst1.append(root.data)
        return root.data
        inorder(root.rightChild)

def sorted_inorder(root):
    a = []
    a.append(inorder(root))
    print(a)
    return a.sort()


if __name__ == "__main__":
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)
    
    print(sorted_inorder(root))

        


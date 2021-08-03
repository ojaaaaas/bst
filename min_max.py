#minimum element in a BST
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def minele(root):
    # curr = root
    
    # while curr.left is not None:
    #     curr = curr.left
    # return curr.data
    if root is None:
        return 0
    while root.left is not None:
        root = root.left
    return root.data

if __name__=="__main__":
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.right = Node(6)
    print(minele(root))
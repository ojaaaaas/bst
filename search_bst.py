#searching in a BST
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def search(root,key):
    if root.data == key:
        return root
    
    if root.data < key:
        return search(root.right,key)

    return search(root.left,key)

if __name__=="__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    print(search(root,4))
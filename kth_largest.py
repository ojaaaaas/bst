#return kth largest element in a bst
class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.data = data

def inorder(root,arr=[],n=0,k=0):
    if root is None:
        return
    inorder(root.left)
    arr.append(root.data)
    inorder(root.right)

    return arr[n-k-1]

if __name__=="__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    arr = []
    n = len(arr)
    k = 1
    print(inorder(root,arr,n,k))
    
    
#check if a binary tree is bst or not
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def bstcheck(root, l=None, r=None):
    if root is None:
        return True #empty binary tree is also a BST
    if(l != None and root.data <= l.data):
        return False

    if(r != None and root.data >= r.data):
        return False
    
    return bstcheck(root.left,l,root) and bstcheck(root.right,root,r)

if __name__=="__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(6)
    if(bstcheck(root,None,None)):
        print("is BST")
    else:
        print("Not a BST")
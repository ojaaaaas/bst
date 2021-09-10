#find inorder predecessor and susccessor
class Node:
    def __init__(self, key=None):
        self.left = None
        self.right = None
        self.key = key

def predsuc(root,key):
    if root is None:
        return
    
    if root.key == key:
        #rightmost value in left subtree is predecessor
        if root.left is not None:
            tmp = root.left
            while(tmp.right):
                tmp = tmp.right
            predsuc.pre = tmp

        #leftmost value in right subtree is successor
        if root.right is not None:
            tmp = root.right
            while(tmp.left):
                tmp = tmp.left
            predsuc.suc = tmp

        return
    
    if root.key > key:
        predsuc.suc = root
        predsuc(root.left,key)
    
    if root.key < key:
        predsuc.pre = root
        predsuc(root.right,key)

if __name__=="__main__":
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    key = 10
    predsuc.pre = None
    predsuc.suc = None
    predsuc(root,key)
        
    if predsuc.pre is not None:
        print("predecessor is ", predsuc.pre.key)

    else:
        print("no predecessor")

    if predsuc.suc is not None:
        print("successor is", predsuc.suc.key)
    
    else:
        print("no successor")
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
class TreeNode(object):
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None


def traverseTreeRecEx(root):
    res=[]

    def inorder(node):
        # LNR

        if not node:
            return 

        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res

def traverseTreeIter(root):
    res=[]
    stack=[]

    while stack or root:
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            res.append(root.val)
    return res


def iterSol(root):
    res=[]
    stack=[]
    cur=root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur.val)
        cur=cur.right
    return res
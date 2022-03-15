

# class TreeNode(object):
#     def __init__(self,val) -> None:
#         self.val=val
#         self.left=None
#         self.right=None



# class Codec:
#     def serialize(self,root):
#         res=[]

#         def dfs(node):
#             if not node:
#                 res.append("N")
#                 return 
#             res.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
#         return ",".join(res)

#     def desrialize(self,data):
#         vals=data.split(",")
#         self.i=0

#         def dfs():
#             if vals[self.i]=="N":
#                 self.i+=1
#                 return None
#             node=TreeNode(int(vals[self.i]))
#             self.i+=1
#             node.left=dfs()
#             node.right=dfs()
#             return node
#         return dfs()



#         class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         if isSameTree(root,subRoot):
#             return True
#         return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    
# def isSameTree(p,q):
#     if not p and not q:
#         return True
#     return isSameTree(p.left,p.left) and isSameTree(p.right,q.right)
#     return False

# all the above stuff is not working because l do not understand the problem
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def dfs():
            stack=[root]
            while len(stack):
                node=stack.pop()
                print(node.val)
                if node.val==subRoot.val:
                    stack1=[node]
                    stack2=[subRoot]
                    while len(stack1) and len(stack2):
                        node1=stack1.pop()
                        node2=stack2.pop()
                        print("node 1",node1.val)
                        print("node 2",node2.val)
                        if node1.val!=node2.val:
                            return False
                        else:
                            if node1.left:
                                stack1.append(node1.left)
                            if node2.left:
                                stack2.append(node2.left)
                            if node1.right:
                                stack1.append(node1.right)
                            if node2.right:
                                stack2.append(node2.right)
                    return True
                else:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
            return False
        return dfs()


a=TreeNode(3)
b=TreeNode(4)
c=TreeNode(5)
d=TreeNode(1)
e=TreeNode(2)

a.left=b
a.right=c
b.left=d
b.right=e


f=TreeNode(4)
g=TreeNode(1)
h=TreeNode(2)

f.left=g
f.right=h

print(Solution().isSubtree(a,f))
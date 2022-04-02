"""
    Given the root of a binary search tree and an integer k,
    return the kth (1-indexed) smallest element in the tree

    use a stack and perform an inorder traversal ie dig far left before going right 
    maintaning a counter and return the current node val when the counter matches the k passed in

    if thats not the case we then move over to the next element

    We bank on the fact that an inorder traversal of a binary tree gives us a sorted order of the values in the tree

"""


class TreeNode:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def kthSmallest(self,root,k):
        n=0
        stack=[root]
        cur=root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right

    def kthSmallestRecursive(self,root,k):
        if not root:
            return 
        self.kthSmallestRecursive(root.left,k)
# Testing it out

t3=TreeNode(3)
t1=TreeNode(1)
t2=TreeNode(2)
t4=TreeNode(4)


t3.left=t1
t1.right=t2
t3.right=t4

a=Solution()

print(a.kthSmallest(t3,1))
print(a.kthSmallestRecursive(t3,1))
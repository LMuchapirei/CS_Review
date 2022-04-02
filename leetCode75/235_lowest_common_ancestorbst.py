"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self,root,p,q):

        cur=root

        while cur:
            # We are handling three cases

            # if both the two children are to the left of root or the right of right a common ancestor by default

            # to check that we compare if the values of our nodes p and q are greater than the root value ie go to the right based on the binary search tree invariant

            #else check if they are to the left given that both the p and q nodes values are less than the root

            # these two cases let us traverse accordingly and thus leads us to the final case when either the above cases are actually false

            # then we have the lowest common ancestor on our hands
            if p.val > cur.val and q.val > cur.val:
                cur=cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur=cur.next
            else:
                return cur
    # recursively we could do the following
    def dfs(self,root,p,q):
        if p.val > root.val and q.val > root.val:
            # go to the right subtree
            return self.dfs(root.right,p,q)
        elif p.val< root.val and q.val < root.val:
            # go tp the left subtree
            return self.dfs(root.left,p,q)
        # we have the ancestor on our hands
        return root
        
    

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor = root
        
        while ancestor:
            if ancestor == p:
                return p
            elif ancestor == q:
                return q
            elif (ancestor.val < p.val and ancestor.val < q.val):
                ancestor = ancestor.right
            elif (ancestor.val > p.val and ancestor.val > q.val):
                ancestor = ancestor.left
            else:
                return ancestor

        return ancestor
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    d = dict()
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True
        else:
            left_res = self.isBalanced(root.left)
            right_res = self.isBalanced(root.right)
            if (root.left and root.right):
                if (left_res and right_res):
                    if (abs(self.d[root.left] - self.d[root.right]) <= 1):
                        self.d[root] = max(self.d[root.left], self.d[root.right]) + 1
                        return True
            elif (not root.left and not root.right):
                self.d[root] = 1
                return True
            elif (not root.left):
                if (root.right in self.d.keys() and self.d[root.right] <= 1):
                    self.d[root] = self.d[root.right] + 1
                    return True
            else:
                if (root.left in self.d.keys() and self.d[root.left] <= 1):
                    self.d[root] = self.d[root.left] + 1
                    return True
        return False

        
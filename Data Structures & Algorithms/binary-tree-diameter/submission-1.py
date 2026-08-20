# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ''' recurse through the left and right subtrees, add them together to add their
        two heights together to get the diameter, compare it with previous diameters. 
        Add to keep track of the number of edges when finding the height.'''
        
        self.res = 0
        #Returns height
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res
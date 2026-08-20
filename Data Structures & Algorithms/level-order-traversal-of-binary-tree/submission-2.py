# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ''' 
        Logic is to implement a queue and a breadth first search approach. 
        When an element is popped, add it to a sublist that keeps track of every
        element in its level. Append that sublist to the final resulting list and return 
        that resulting list. I can use len(queue) to figure out how many elements I need
        to pop in a given level. '''

        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: 
                res.append(level)

        return res
                     
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
          return levels
        
        def printlevel(node, level):
          if len(levels) == level:
            levels.append([])
            
          levels[level].append(node.val)
          
          if node.left:
            printlevel(node.left, level+1)
          if node.right:
            printlevel(node.right, level+1)
            
        printlevel(root, 0)
        return levels
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
          res.append(root.val)
          res = res + self.preorderTraversal(root.left)
          res = res + self.preorderTraversal(root.right)
        return res

#root->left->right
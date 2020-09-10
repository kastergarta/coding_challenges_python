class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global ans
        ans = 0
        self.sumOfNode(root)
        return ans 
        
    def sumOfNode(self, root):
        if (root == None):
            return 0

        left = self.sumOfNode(root.left)
        right = self.sumOfNode(root.right)

        global ans
        ans += abs(left - right)
        return left + right + root.val
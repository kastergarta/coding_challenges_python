class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        root.level = 0
        q = [root]
        ans = []
        sum, num, curLevel = 0, 0, 0

        while len(q):
            item = q[0]
            del q[0]
            if item.level == curLevel:
                sum += item.val 
                num += 1
            else:
                ans.append(sum / num)
                curLevel += 1
                sum = item.val 
                num = 1
            
            if item.left:
                item.left.level = item.level + 1
                q.append(item.left)
            if item.right:
                item.right.level = item.level + 1
                q.append(item.right)
            
        ans.append(sum / num)
        return ans
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum, pre, s = 0, 0, set()

        for item in nums:
            sum += item
            if (k):
                sum %= k

            if (sum in s):
                return True

            s.add(pre)
            pre = sum

        return False
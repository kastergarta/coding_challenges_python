import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        array = []
        for index, item in enumerate(self.nums):
            if item == target:
                array.append(index)

        index = int(random.random() * len(array))
        return array[index]
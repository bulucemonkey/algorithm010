#两数之和
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numlist = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in numlist:
                return [numlist[another_num], index]
            numlist[num] = index
        return None

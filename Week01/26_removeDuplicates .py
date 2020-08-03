# 删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1 if nums else 0

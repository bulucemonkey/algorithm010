# 旋转数组
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def exchange(l, r):
            while(l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l = l+1
                r = r-1
        exchange(0, n-k-1)
        exchange(n-k, n-1)
        exchange(0, n-1)
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    a = Solution().rotate(nums, 2)
    print(a)

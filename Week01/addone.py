# 加一
class Solution:
    def plusOne(self, digits):
        n = 0
        for i in digits:
            n = n*10
            n += i
        nums = []
        n += 1
        for i in str(n):
            nums.append(int(i))

        return nums

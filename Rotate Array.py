# -*- coding:utf-8 -*-
__author__ = 'Muming'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if k != 0:
            nl = len(nums)
            step = k % len(nums)
            nums.extend(nums)
            for x in range(nl - step):
                nums.pop(0)
            for y in range(step):
                nums.pop(-1)
        print nums

if __name__ == '__main__':
    so = Solution()
    # p = [1,2,3,4,5,6,7]
    p = [1]
    n = 0
    print so.rotate(p, n)

# 1 2 3 4 5 6 7
# 1 2 3 4 [5 6 7 1 2 3 4] 5 6 7
#          |              |
#        k = 3        len(num) - k
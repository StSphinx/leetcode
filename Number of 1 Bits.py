# -*- coding:utf-8 -*-
__author__ = 'Muming'

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        if n == 0:
            return 0
        count = 0
        for i in range(32):
            if n >> i & 1:
                count += 1
        return count



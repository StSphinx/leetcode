# -*- coding:utf-8 -*-
from operator import itemgetter

__author__ = 'Muming'
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        res_str = []
        if numRows == 1:
            return s
        val, mod = divmod(len(s), (2 * numRows - 2))

        for y in range(numRows):
            for x in range(val + mod):
                res_str.append(s[2 * numRows - 2 + y - 2 * x])

        print res_str

def test():
    tt = Solution()
    print tt.convert('01234567890123456789', 5)
if __name__ == '__main__':
    test()
    pass
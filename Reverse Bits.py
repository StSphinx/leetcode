# -*- coding:utf-8 -*-
__author__ = 'Muming'

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n > 4294967295:
            return None
        bi = str(bin(n)[2:])
        bi_r = bi[::-1]
        bi_res = bi_r + '0' * (32 - len(bi_r))
        return int(bi_res, 2)

if __name__ == '__main__':
    so = Solution()
    print so.reverseBits(8)



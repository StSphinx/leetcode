# -*- coding:utf-8 -*-
__author__ = 'Muming'

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        res = 0
        str = s.split(' ')
        for s in str:
            count = len(s)
            if count != 0:
                res = count
        return res


def test():
    st = Solution()
    print st.lengthOfLastWord("a    bd     ")


if __name__ == '__main__':
    test()
    pass
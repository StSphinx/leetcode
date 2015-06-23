# -*- coding:utf-8 -*-
__author__ = 'Muming'

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        res = []
        if len(strs) == 0:
            return ''
        num = len(strs)
        temp = zip(*strs)
        for str in temp:
            char = set(str)
            if len(char) == 1:
                res.extend(list(char)[0])
            else:
                return ''.join(res)
        return ''.join(res)

def test():
    st = Solution()
    print st.longestCommonPrefix([''])

if __name__ == '__main__':
    test()
    pass
# -*- coding:utf-8 -*-
__author__ = 'Muming'
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        return list(s) == list(t)[::-1]

so = Solution()
print so.anagram("abcd", "ddcba")
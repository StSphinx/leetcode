# -*- coding:utf-8 -*-
__author__ = 'Muming'
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        for k, v in enumerate(string):
            if v == ' ':
                string[k] = '%20'
                length += 3
        return length, string

so = Solution()
print so.replaceBlank(list("abcd efg hij"), 12)
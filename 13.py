# -*- coding:utf-8 -*-

"""
-------------------------------------------------
   File Name：  13
   date:        2019-03-07 23:51
   Author:      Tornado
   Description: 
-------------------------------------------------
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ss = list(s)
        print ss
        sum = letter_dict[ss[0]]

        length = len(ss)

        for i in range(length):
            j = i + 1
            if j >= length:
                return sum
            if letter_dict[ss[j]] <= letter_dict[ss[i]]:
                sum += letter_dict[ss[j]]
            else:
                sum = sum + letter_dict[ss[j]] - 2 * letter_dict[ss[i]]


def test():
    st = Solution()
    print st.romanToInt('MCMXCIV')

if __name__ == '__main__':
    test()
    pass

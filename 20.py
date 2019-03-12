# -*- coding:utf-8 -*-

"""
-------------------------------------------------
   File Name：  20
   date:        2019-03-08 00:33
   Author:      Tornado
   Description: 
-------------------------------------------------
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pare_dict = {'(': ')', '[': ']', '{': '}'}
        end_bra = [')', ']', '}']
        length = len(s)
        if length % 2 != 0:
            return False
        queue = []
        for ch in s:
            if len(queue) == 0 and ch not in end_bra:
                queue.append(ch)
                continue
            elif ch not in end_bra:
                queue.append(ch)
                continue
            elif ch in end_bra:
                if len(queue) != 0 and pare_dict[queue[-1]] == ch:
                    del queue[-1]
                    continue
                else:
                    return False

        return queue == []



def test():
    st = Solution()
    print st.isValid('{[]}')

if __name__ == '__main__':
    test()
    pass

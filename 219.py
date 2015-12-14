# -*- coding:utf-8 -*-
__author__ = 'Muming'
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if nums is None or k == 0:
            return False
        dict = {}
        for i, v in enumerate(nums):
            if dict.get(v) is not None:
                dict[v].append(i)
            else:
                dict[v] = [i,]

        for key, value in dict.items():
            for ia, va in enumerate(value[:-1]):
                if va + k >= value[ia + 1]:
                    return True
        return False


def test():
    st = Solution()
    print st.containsNearbyDuplicate([-1, 0, -1, -1], 1)


if __name__ == '__main__':
    test()
    pass
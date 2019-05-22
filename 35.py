from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value >= target:
                return index
            else:
                continue


def test():
    st = Solution()
    print(st.searchInsert([1, 3, 5, 6], 5))


if __name__ == '__main__':
    test()
    pass

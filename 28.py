class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pos = -1
        ln = len(needle)


        if ln == 0:
            return 0

        if needle not in haystack:
            return -1

        for index, value in enumerate(haystack):
            if value != needle[0]:
                continue
            else:
                if haystack[index:ln + index] == needle:
                    return index
                else:
                    continue
        return pos


def test():
    st = Solution()
    print(st.strStr('', ''))


if __name__ == '__main__':
    test()
    pass

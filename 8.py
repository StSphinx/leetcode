class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        MAX = 2147483647
        MIN = -2147483648

        pa = re.compile(r'^\s*[-+]?\d+')
        res = pa.match(str)

        if res:
            res = res.group()
            res = int(res.strip())
            if res > MAX:
                return MAX
            if res < MIN:
                return MIN
            return res

        else:
            return 0


def test():
    tt = Solution()
    print(tt.myAtoi("+1"))


if __name__ == '__main__':
    test()

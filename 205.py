# -*- coding:utf-8 -*-
__author__ = 'Muming'
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds = {}
        dt = {}
        for k, v in enumerate(s):
            if ds.get(v) is not None:
                ds[v].append(k)
            else:
                ds[v] = [k,]

        for kk, vv in enumerate(t):
            if dt.get(vv) is not None:
                dt[vv].append(kk)
            else:
                dt[vv] = [kk,]

        if set(map(set, ds.values())) == set(map(set, dt.values())):
            return True
        else:
            return False

def test():
    st = Solution()
    print st.isIsomorphic("ab", "ca")


if __name__ == '__main__':
    test()
    pass
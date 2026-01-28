1# https://leetcode.com/problems/guess-number-higher-or-lower/description/
2
3# The guess API is already defined for you.
4# @param num, your guess
5# @return -1 if num is higher than the picked number
6#          1 if num is lower than the picked number
7#          otherwise return 0
8# def guess(num: int) -> int:
9
10class Solution:
11    def guessNumber(self, n: int) -> int:
12        L = 1
13        R = n
14
15        while L <= R:
16            M = (L + R) // 2
17            if guess(M) > 0:
18                L = M + 1
19            elif guess(M) < 0:
20                R = M - 1
21            else:
22                return M
23        
24        return -1
25
26
1# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
2class Solution:
3    def checkIfExist(self, arr: List[int]) -> bool:
4        from collections import defaultdict
5        dct = defaultdict(int)
6        
7        for i in arr:
8            dct[i] += 1
9            
10        
11        for i in arr:
12            if i != 0 and 2 * i in dct:
13                return True
14            
15            if i == 0 and dct[i] > 1:
16                return True
17        
18        return False
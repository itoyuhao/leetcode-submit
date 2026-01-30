# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        from collections import defaultdict
        dct = defaultdict(int)
        
        for i in arr:
            dct[i] += 1
            
        
        for i in arr:
            if i != 0 and 2 * i in dct:
                return True
            
            if i == 0 and dct[i] > 1:
                return True
        
        return False
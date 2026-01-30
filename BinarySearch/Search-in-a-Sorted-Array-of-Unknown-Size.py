# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/description/
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        # idea: create a while-loop to do doubling whenever the upper bound is smaller than the target
                # end looping when we find an index that is greater than target value
                # then we do binary search
        
        
        left, right = 0, 1
        
        if reader.get(left) == target:
            return 0
        
        # finding lower/upper bound
        while reader.get(right) < target:
            left = right
            right = right * 2
        
        # doing binary search
        while left <= right:
            mid = (left + right) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1
            
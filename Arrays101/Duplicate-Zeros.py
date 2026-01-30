# https://leetcode.com/problems/duplicate-zeros/description/
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # while-loop
        n = len(arr)
        next_ptr = 0
        while next_ptr < n:
            if arr[next_ptr] == 0:
                arr.insert(next_ptr, 0)
                arr.pop()
                next_ptr += 1
            next_ptr += 1
        
        # # for-loop
        # n = len(arr)
        # zero_cnt = 0
        # for i in range(n):
        #     if i + zero_cnt >= n:
        #         break
        #     if arr[i+zero_cnt]  == 0:
        #         arr.insert(i+zero_cnt, 0)
        #         arr.pop()
        #         zero_cnt += 1

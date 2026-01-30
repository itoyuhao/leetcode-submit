# https://leetcode.com/problems/split-array-largest-sum/description/
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 1

            for element in nums:
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # 開一個新的子陣列裝當前這個元素
                    current_sum = element
                    splits_required += 1
            
            return splits_required
        
        left = max(nums)
        right = sum(nums)
        # 初始值可以設為最大的可能總和
        minimum_larget_split_sum = right

        while left <= right:
            mid = (left + right) // 2

            if min_subarrays_required(mid) <= k:
                # 份數小於等於 k，代表 mid 可能還可以更小
                minimum_larget_split_sum = mid
                right = mid - 1
            else:
                # 份數大於 k，代表 mid 太小了，必須往右找
                left = mid + 1
        
        # 關鍵：return 要在 while 之外
        return minimum_larget_split_sum
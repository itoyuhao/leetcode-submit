1# https://leetcode.com/problems/split-array-largest-sum/description/
2from typing import List
3
4class Solution:
5    def splitArray(self, nums: List[int], k: int) -> int:
6        
7        def min_subarrays_required(max_sum_allowed: int) -> int:
8            current_sum = 0
9            splits_required = 1
10
11            for element in nums:
12                if current_sum + element <= max_sum_allowed:
13                    current_sum += element
14                else:
15                    # 開一個新的子陣列裝當前這個元素
16                    current_sum = element
17                    splits_required += 1
18            
19            return splits_required
20        
21        left = max(nums)
22        right = sum(nums)
23        # 初始值可以設為最大的可能總和
24        minimum_larget_split_sum = right
25
26        while left <= right:
27            mid = (left + right) // 2
28
29            if min_subarrays_required(mid) <= k:
30                # 份數小於等於 k，代表 mid 可能還可以更小
31                minimum_larget_split_sum = mid
32                right = mid - 1
33            else:
34                # 份數大於 k，代表 mid 太小了，必須往右找
35                left = mid + 1
36        
37        # 關鍵：return 要在 while 之外
38        return minimum_larget_split_sum
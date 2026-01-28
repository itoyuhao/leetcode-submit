1# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
2class Solution:
3    def search(self, nums: List[int], target: int) -> int:
4        
5        if len(nums) == 1:
6            return 0 if nums[0] == target else -1
7        
8        if target < nums[0] and target > nums[-1]:
9            return -1
10        
11        
12        left, right = 0, len(nums) - 1
13        
14        
15        while left < right:
16            if target == nums[left]:
17                return left
18            if target == nums[right]:
19                return right
20            
21            mid = (left + right) // 2
22            
23            if target == nums[mid]:
24                return mid
25            
26            # case 2: subarray on mid's left is sorted
27            elif nums[mid] >= nums[left]:
28                if target >= nums[left] and target < nums[mid]: # target is in left-side
29                    right = mid - 1
30                else:
31                    left = mid + 1
32            
33            # case 3: subarray on mid's right is sorted
34            else:
35                if target <= nums[right] and target > nums[mid]: # target is in right-side
36                    left = mid + 1
37                else:
38                    right = mid - 1
39
40        return -1
41
42        #     if nums[left] > nums[right]:  # rotated array 的情況
43                
44        #         if (target > nums[mid]) and target > nums[right]:
45        #             left = mid + 1
46        #         elif (target < nums[mid]) and target < nums[right]:
47        #             left = mid + 1
48        #         # elif (target < nums[mid]) and target > nums[left]:
49        #         #     right = mid -1
50        #         else:
51        #             right = mid - 1
52                
53        #         # if target < nums[right] and target < nums[mid]:  # 表示target在右側
54        #         #     left = mid + 1
55        #         # elif target > nums[left]:
56        #         #     right = mid - 1
57        #     else:  # 是一般 array
58        #         if target < nums[mid]:
59        #             right = mid - 1
60        #         else:
61        #             left = mid + 1
62                
63        # return -1
64            
65            
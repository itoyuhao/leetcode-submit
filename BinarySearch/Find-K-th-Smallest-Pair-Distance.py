1# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
2class Solution:
3    def smallestDistancePair(self, nums: List[int], k: int) -> int:
4        # 配對距離最小就是0，最大是最大的元素與最小元素的差距。 (bounded)
5        # 如果小於或等於 d 的配對距離的數量比 k 小，那第 k 小的配對距離一定大於 d；
6        # 反之，如果小於或等於 d 的配對距離的數量等於或大於 k，那第 k 小的配對距離一定小於或等於 d
7
8        nums.sort()
9        array_size = len(nums)
10
11
12        # Initialize binary search range
13        low = 0
14        high = nums[array_size - 1] - nums[0]
15
16        while low < high:
17            mid = (low + high) // 2
18
19            # Count pairs with distance <= mid
20            count = self._count_pairs_with_max_distance(nums, mid)
21
22            # Adjust binary search bounds based on count
23            if count < k:
24                low = mid + 1
25            else:
26                high = mid
27        
28        return low
29    
30    # Count number of pairs with distance <= max_distance using a moving window
31    def _count_pairs_with_max_distance(
32        self,
33        nums: List[int],
34        max_distance: int
35    ) -> int:
36        count = 0
37        array_size = len(nums)
38        left = 0
39
40        for right in range(array_size):
41            # Adjust the left pointer to maintain the window with distances <= max_distance
42            while nums[right] - nums[left] > max_distance:
43                left += 1
44            
45            # Add the number of valid pairs ending at the current right index
46            count += right - left
47        
48        return count
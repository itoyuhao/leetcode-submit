# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        if target < nums[0] and target > nums[-1]:
            return -1
        
        
        left, right = 0, len(nums) - 1
        
        
        while left < right:
            if target == nums[left]:
                return left
            if target == nums[right]:
                return right
            
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            # case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]: # target is in left-side
                    right = mid - 1
                else:
                    left = mid + 1
            
            # case 3: subarray on mid's right is sorted
            else:
                if target <= nums[right] and target > nums[mid]: # target is in right-side
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        #     if nums[left] > nums[right]:  # rotated array 的情況
                
        #         if (target > nums[mid]) and target > nums[right]:
        #             left = mid + 1
        #         elif (target < nums[mid]) and target < nums[right]:
        #             left = mid + 1
        #         # elif (target < nums[mid]) and target > nums[left]:
        #         #     right = mid -1
        #         else:
        #             right = mid - 1
                
        #         # if target < nums[right] and target < nums[mid]:  # 表示target在右側
        #         #     left = mid + 1
        #         # elif target > nums[left]:
        #         #     right = mid - 1
        #     else:  # 是一般 array
        #         if target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
                
        # return -1
            
            
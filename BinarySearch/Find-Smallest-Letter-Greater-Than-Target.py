1# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
2class Solution:
3    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
4        
5        # edge case: no characters in letters that is lexicographically greater than target
6        if target >= letters[-1]:
7            return letters[0]
8        
9        left, right = 0, len(letters) - 1
10        
11        while left < right:
12            mid = (left + right) // 2
13            
14            if letters[mid] <= target:
15                left = mid + 1
16            
17            elif letters[mid] > target:
18                right = mid
19        
20        
21        return letters[left] if letters[left] > target else letters[right]
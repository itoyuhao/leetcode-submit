# Binary Search Problem Solving Techniques

This guide summarizes the core concepts and the three standardized templates for Binary Search, based on the `leetcode-submit/BinarySearch` problem set. Binary Search is not just for finding a number in an array; it is a general strategy for "reducing the search space."

## 1. The 3 Templates
The most confusing parts of Binary Search are the `while` condition (`<` vs `<=`) and the boundary updates (`mid` vs `mid+1`).

### Template I: Standard Search (`left <= right`)
- **Use Case**: Search for a specific element (Index Check). No need to access neighbors.
- **Condition**: `while left <= right`
- **Update**: `left = mid + 1`, `right = mid - 1`
- **Termination**: `left > right` (Return -1 if not found)
- **Applications**: `Binary Search`, `Sqrt(x)` (Find the rightmost value in answer range), `Guess Number`

### Template II: Range Search (`left < right`)
- **Use Case**: Determine direction based on `nums[mid+1]`, or find the *first* element meeting a condition.
- **Condition**: `while left < right`
- **Update**: `left = mid + 1` (Exclude mid), `right = mid` (Include mid as potential answer)
- **Termination**: `left == right` (Often requires post-processing to check `nums[left]`)
- **Applications**: `First Bad Version`, `Find Minimum in Rotated Sorted Array`

### Template III: Neighbors Search (`left + 1 < right`)
- **Use Case**: Need to access `mid`'s neighbors (`nums[mid-1]`, `nums[mid+1]`) simultaneously without going out of bounds.
- **Condition**: `while left + 1 < right`
- **Update**: `left = mid`, `right = mid` (Shrink interval, keep mid)
- **Termination**: `left + 1 == right` (2 elements remaining; requires post-processing for both)
- **Applications**: `Find Peak Element`, `Find K Closest Elements`

## 2. Rotated Sorted Array
The core insight for `Rotated` arrays: **Even if rotated, one half of the array will always be sorted.**
- Determine which half is sorted: `if nums[left] <= nums[mid]` (Left half is sorted) else (Right half is sorted).
- Check if target lies within the sorted half to decide the search direction.

## 3. Search in Answer Space
When the problem defines a condition and asks for a minimum/maximum value (without a given array), you can perform Binary Search on the "Answer Range."
- **Applications**: `Sqrt(x)`, `Split Array Largest Sum`, `Find K-th Smallest Pair Distance`

---

## Problems & Techniques Mapping

| Problem | Current Strategy | Recommended Strategy | Key Notes |
| :--- | :--- | :--- | :--- |
| **Binary Search** | Template I (`<=`) | Template I | Standard problem. |
| **Find First and Last Position...** | Custom Template (`<=`) | Template I or II | Search for lower bound and upper bound separately. |
| **Find Minimum in Rotated...** | Template II (`<`) | Template II | Compare `nums[mid]` with `nums[right]` to find the minimum. |
| **Find Peak Element** | Template III (`+1 <`) | Template II (`<`) | Template III is safe, but Template II is cleaner for single-neighbor check. |
| **First Bad Version** | Template I (`<=`) | Template II | Find the first `True` version. Classic Template II, but Template I also works. |
| **Guess Number...** | Template I (`<=`) | Template I | Similar to standard search. |
| **Search in Rotated Sorted Array** | Template I (`<=`) + Logic | Template I | Identify sorted half, then check if target is inside. |
| **Sqrt(x)** | Template I (`<=`) | Template I (Answer Space) | Range is `[0, x]`. Find rightmost integer where `k^2 <= x`. |
| **Search in a Sorted Array of Unknown Size** | Template I | Template I | Find boundary by doubling index, then Binary Search. |

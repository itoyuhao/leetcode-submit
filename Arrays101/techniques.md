# Array Problem Solving Techniques

This guide summarizes key problem-solving techniques based on the `leetcode-submit/Arrays101` problem set. Mastering these techniques will help you evolve from "Brute Force" to "Optimal Solutions."

## 1. Two Pointers Technique - Read/Write Pointers
This is the most common technique for **In-place** array modifications.
When a problem asks you to remove elements, move zeroes, or deduplicate, and requires $O(1)$ space complexity, avoid using Python's `pop()` or `insert()` methods within loops. These operations are $O(N)$, leading to an overall time complexity of $O(N^2)$.

**Core Concept:**
Use two variables (pointers):
- `read_pointer` (usually the loop index `i`): Iterates through the array to find target elements.
- `write_pointer` (often `k`): Points to the index where the next "valid element" should be placed.

**Applications:**
- **Remove Duplicates from Sorted Array**: When `read` finds a new unique element, write it to the `write` position and increment `write`.
- **Move Zeroes**: Write non-zero elements to the `write` position, then fill the remainder with zeroes.
- **Sort Array By Parity**: Similar to the Partition concept, move elements satisfying the condition to the front (via swap or overwrite).

## 2. Iterating Backwards
When an array operation affects elements "not yet visited" or requires "information from the right," iterating backwards is often the optimal strategy.

**Core Concept:**
- **Avoid Overwriting**: When merging two arrays without extra space, writing from front to back might overwrite original data that hasn't been processed yet. Filling from back to front avoids this issue.
- **Accumulating Information**: If the problem asks for "max element to the right" or "count of elements to the right," iterating backwards allows you to solve it in a **One Pass** scan.

**Applications:**
- **Merge Sorted Array**: When merging two sorted arrays into one (with sufficient buffer space), compare elements from the end and fill from the back to avoid overwriting the original array values.
- **Replace Elements with Greatest Element on Right Side**: Scan from the last element, maintaining a `max_so_far` variable. This achieves $O(N)$ time complexity, unlike the $O(N^2)$ brute force approach of finding the max for every element.

## 3. Pitfalls of In-place Operations
A common mistake when solving LeetCode Array problems in Python is over-relying on intuitive List methods.

- **Avoid**: Frequently using `arr.insert(index, val)` or `arr.pop(index)` inside `for` or `while` loops.
- **Reason**: Each `insert` or `pop` operation shifts all subsequent elements, costing $O(N)$ time. This results in $O(N^2)$ total time complexity.
- **Solution**:
    - Prefer **Swap**: `arr[i], arr[j] = arr[j], arr[i]`
    - Or **Overwrite**: `arr[write_idx] = arr[read_idx]`, then adjust the array length (if the language permits) or ignore the remainder.

## 4. Edge Cases
Array problems are deceptive; they seem simple but are prone to **Index Out of Bound** errors.
- Empty array (`[]`) or single-element array.
- Checks like `next_ptr < n` when moving pointers.
- Be extra careful with boundary logic involving `i+1` or `i-1`.

---

### Quick Checklist
When approaching a new problem, consider these questions in order:
1. **Can I iterate backwards?** (Simplifies right-side dependency issues)
2. **Can I use Two Pointers?** (Solves removal, moving, and partitioning problems)
3. **Do I strictly need O(1) space?** (If yes, the problem is likely about index manipulation and swaps)

---

## Problems & Techniques Mapping

The following table maps problems from `Arrays101` to their current approaches and recommended optimizations.

| Problem | Current Strategy | Recommended Strategy (Optimal) | Key Notes |
| :--- | :--- | :--- | :--- |
| **Check If N and Its Double Exist** | `Hash Map` (Set/Dict) | `Hash Map` | $O(N)$ Space/Time. This is the standard solution. |
| **Duplicate Zeros** | `Loop` + `Insert/Pop` ($O(N^2)$) | **Two Pointers (Backwards)** | Iterating backwards achieves $O(N)$ Time and $O(1)$ Space, avoiding massive element shifts. |
| **Find All Numbers Disappeared...** | `In-place Index Marking` | `In-place Index Marking` | Use indices as Hash Keys (marking with negative sign) to save space. |
| **Find Numbers with Even...** | `Linear Scan` + Digit Count | `Linear Scan` | Simple and intuitive. No special optimization needed. |
| **Height Checker** | `Bubble Sort` ($O(N^2)$) | `Counting Sort` | Since height range is small (1-100), Counting Sort yields $O(N)$. |
| **Max Consecutive Ones** | `Linear Scan` | `Linear Scan` | Simple traversal to track maximum count. |
| **Max Consecutive Ones II** | `Sliding Window` (Zero Counter) | `Sliding Window` | General template for "at most k flips" problems. |
| **Merge Sorted Array** | `Two Pointers` + `Insert/Pop` | **Two Pointers (Backwards)** | The key is filling from the back to avoid `Insert`'s $O(N^2)$ complexity. |
| **Move Zeroes** | `Pop` + `Append` ($O(N^2)$) | **Two Pointers (Read/Write)** | "Snowball" technique or read/write pointers allow doing this in one pass ($O(N)$). |
| **Remove Duplicates...** | `Pop` inside Loop ($O(N^2)$) | **Two Pointers (Read/Write)** | Use a `read` pointer to find new values and a `write` pointer to place them. Avoid `Pop`. |
| **Remove Element** | `Pop` inside Loop ($O(N^2)$) | **Two Pointers (Read/Write)** | Similar to Move Zeroes; shift non-target values to the front. |
| **Replace Elements with...** | `Iterating Backwards` | `Iterating Backwards` | Optimal solution ($O(N)$). |
| **Sort Array By Parity** | `Pop` + `Append` ($O(N^2)$) | **Two Pointers (Swap)** | Two pointers moving from ends towards center is efficient. |
| **Squares of a Sorted Array** | `Two Pointers` (Converging) | `Two Pointers` (Converging) | Optimal $O(N)$ solution utilizing the sorted property. |
| **Third Maximum Number** | `Selection Sort` ($O(N^2)$) | **3 Variables** / `Set` | Maintain 3 variables to track top 3 values for $O(N)$ efficiency. |
| **Valid Mountain Array** | `Linear Scan` (State Check) | `Linear Scan` | Single pass checking for increasing then decreasing state transition. |

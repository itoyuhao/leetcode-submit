1# https://leetcode.com/problems/powx-n/description/
2class Solution:
3    def myPow(self, x: float, n: int) -> float:
4        return self.binaryExp(x, n)
5        
6    
7    def binaryExp(self, x: float, n: int) -> float:
8        # base case, to stop recursive calls
9        if n == 0:
10            return 1
11        
12        # Handle case where n < 0.
13        if n < 0:
14            return 1.0 / self.binaryExp(x, -1 * n)
15        
16        # Perform Binary Exponentiation.
17        # If 'n' is odd we perform binary Exponentiation on 'n - 1' and multiply result with 'x'
18        if n % 2 == 1:
19            return x * self.binaryExp(x * x, (n - 1) // 2)
20        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
21        else:
22            return self.binaryExp(x * x, n // 2)
23        
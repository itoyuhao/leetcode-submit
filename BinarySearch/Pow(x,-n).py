# https://leetcode.com/problems/powx-n/description/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
        
    
    def binaryExp(self, x: float, n: int) -> float:
        # base case, to stop recursive calls
        if n == 0:
            return 1
        
        # Handle case where n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)
        
        # Perform Binary Exponentiation.
        # If 'n' is odd we perform binary Exponentiation on 'n - 1' and multiply result with 'x'
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)
        
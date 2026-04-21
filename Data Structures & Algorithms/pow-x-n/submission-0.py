class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n == 0:
            return 1
        elif n > 0: 
            for _ in range(n):
                result *= x
                n -= 1
            return result
        elif n < 0:
            for _ in range(-n):
                result *= 1/x
                n += 1
            return result
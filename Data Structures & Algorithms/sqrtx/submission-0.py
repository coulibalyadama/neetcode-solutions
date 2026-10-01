class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x+1):
            if i*i <= x and (i+1)*(i+1)>x:
                return i
        
        
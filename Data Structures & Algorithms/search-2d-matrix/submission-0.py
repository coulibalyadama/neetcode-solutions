class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        liste = []
        for array in matrix:
            liste += array
        
        l, r = 0, len(liste)

        while l<r:
            m = (l + r)//2
            if liste[m] == target:
                return True
            elif liste[m] > target:
                r = m
            else:
                l = m + 1
        return False
        
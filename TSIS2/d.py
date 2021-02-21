class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi, q = 0, 0
        for i in gain:
            q += i
            if q > maxi:
                maxi = q
        return maxi
        
        
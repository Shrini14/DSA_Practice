class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        count = 0 
        for i in gain:
            count += i
            lst.append(count)
        return max(lst)
        
        
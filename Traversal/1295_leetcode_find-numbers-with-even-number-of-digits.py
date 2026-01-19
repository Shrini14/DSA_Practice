class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0 
        for i in nums:
            m = str(i)
            if len(m)%2==0:
                count+=1
            else:
                continue
        return count

        
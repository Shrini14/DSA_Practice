class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)
        while l < r:
            act = numbers[l-1]+numbers[r-1]
            if act == target:
                h = 0
                return l,r
            elif act < target:
                l+=1
            elif act > target:
                r-=1



        

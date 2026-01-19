class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        for i in nums:
            output.append(i)
        for j in nums:
            output.append(j)

        return output  
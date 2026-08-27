class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return min(set(nums),key=nums.count)

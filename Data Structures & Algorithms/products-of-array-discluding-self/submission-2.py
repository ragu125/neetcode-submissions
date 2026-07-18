from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]

        for i in range(len(nums)):
            sb=[]
            for j in range(len(nums)):
                if i !=j:
                    sb.append(nums[j])
            res.append(prod(sb))
        return res            

        
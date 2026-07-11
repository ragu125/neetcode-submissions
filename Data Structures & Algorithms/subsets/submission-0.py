class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]

        for i in nums:
            temp=[]
            for j in res:
                a=j+[i]
                temp.append(a)
            res+=temp
        return res        
        
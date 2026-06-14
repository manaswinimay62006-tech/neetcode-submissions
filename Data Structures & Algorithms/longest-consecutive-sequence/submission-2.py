class Solution:
    def longestConsecutive(self,nums:List[int])->int:
        res=0
        conset=set(nums)
        for num in nums:
            if (num-1) not in conset:
                add=1
                while (num+add) in conset:
                    add+=1
                res=max(res,add)
        return res
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset=defaultdict()
        res=[]
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in numset:
                res.append(numset[comp])
                res.append(i)
            numset[nums[i]]=i
        return res

                
            
            
                

        
            
        
        
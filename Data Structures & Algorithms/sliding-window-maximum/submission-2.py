class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        final=0
        res=[]
        l=0
        r=l+k-1
        while r<len(nums):
            final=max(nums[l:r+1])
            res.append(final)
            l+=1
            r+=1
        return res
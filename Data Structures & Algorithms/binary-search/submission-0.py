class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=0
        while r<len(nums):
            if nums[r]==target:
                return r
            r+=1
        return -1
            
        
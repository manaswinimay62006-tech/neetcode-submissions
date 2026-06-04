class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storeset=set()
        for num in nums:
            if num in storeset:
                return True
            storeset.add(num)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for x in nums:
            seen.add(x)
        if len(nums) != len(seen):
            return True
        return False
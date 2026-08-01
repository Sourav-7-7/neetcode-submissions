class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        sub=0
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in freq:
                return [freq[sub],i]
            freq[nums[i]]=i
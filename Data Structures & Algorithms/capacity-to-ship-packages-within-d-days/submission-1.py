class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        ans=0
        while l<=r:
            capacity=l+(r-l)//2
            cur_load=0
            cur_day=1
            for weight in weights:
                if cur_load+weight <= capacity:
                    cur_load+=weight
                else:
                    cur_load=weight
                    cur_day+=1
            if cur_day <= days:
                ans=capacity
                r=capacity-1
            else:
                l=capacity+1
        return ans           
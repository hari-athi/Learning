#Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumOf=sum(nums[:k])
        value=sumOf
        index=k
        for i in range (len(nums)-k):
            value=(value - nums[i]) + nums[i+k]
            sumOf=max(sumOf,value)
        return sumOf/k

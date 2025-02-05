class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in l:
                return [l[diff],i]
            l[n]=i
        return []
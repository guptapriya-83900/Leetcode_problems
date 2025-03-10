class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}

        def backtrack(index,s):
            if (index,s) in cache:
                return cache[(index,s)]
            if index==len(nums):
                if s==target:
                    return 1
                else:
                    return 0

            left=backtrack(index+1,s+nums[index])
            right=backtrack(index+1,s-nums[index])

            cache[(index,s)]=left+right

            return cache[(index,s)]

        return backtrack(0,0)


        
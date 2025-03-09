class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
  

        def linearcost(nums):
            first=nums[0]
            second=max(first,nums[1]) if len(nums)>1 else nums[0]

            for i in range(2,len(nums)):
                temp=second
                second=max(first+nums[i],second)
                first=temp

            return second

        return max(linearcost(nums[1:]),linearcost(nums[:-1]))
        
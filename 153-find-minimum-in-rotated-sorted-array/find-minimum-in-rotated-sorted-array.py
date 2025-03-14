class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        res=nums[0]     #First element as smallest. Because if the array is sorted than first element will be minimum
        while l<=r:
            m=(l+r)//2 
            res=min(res,nums[m])        #Suppose Middle Element is minimum for now

            if nums[r]>nums[m]:  # Right half is sorted, min is in left half
                r=m 
            else:               #left half is sorted,Minimum is in right side
                l=m+1

        return res

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxcap=0
        l,r= 0, len(height)-1
        while l<r:
            area = (r-l) * min(height[l],height[r]) 
            maxcap = max(maxcap,area)
            if height[l]<height[r]:
                l+=1
            # elif heights[r]<heights[l]:
            #     r-=1
            else: 
                r-=1
        return maxcap
        
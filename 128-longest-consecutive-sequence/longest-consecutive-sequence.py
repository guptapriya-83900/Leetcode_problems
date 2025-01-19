class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
 """
        # if nums==[]:
        #     return 0
        # else:
        #    l=sorted(nums)
        
        # longest_streak=1
        # current_streak=1
        # for i in range(1,len(l)):
        #     if l[i]==l[i-1]:
        #         continue
        #     elif l[i]==l[i-1]+1:
        #         current_streak+=1
        #     else:
        #         longest_streak = max(longest_streak, current_streak)
        #         current_streak = 1

        # return max(longest_streak, current_streak)


        # for i in range(len(nums)):
        if not nums:
            return 0
        s=set(nums)
        maxc=1
        for i in s:
            if i-1 not in s:
                count=1
                while i+1 in s:
                    count+=1
                    i+=1
                maxc=max(count,maxc)
        return maxc

             
        
        



                

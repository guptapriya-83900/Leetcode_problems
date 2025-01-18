class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_hashset = set()
        for i in nums:
            if i in nums_hashset:
                return True
            else: 
                nums_hashset.add(i)
                
        return False
        
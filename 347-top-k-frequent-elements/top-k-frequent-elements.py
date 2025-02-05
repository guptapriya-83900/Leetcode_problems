class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=1+dic.get(nums[i],0)

        freq=[[] for i in range(len(nums)+1)]

        for key,value in dic.items():
            freq[value].append(key)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
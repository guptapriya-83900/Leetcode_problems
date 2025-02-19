class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def per(p,up):
            if not up:
                res.append(p[:])  
                return

            num = up[0] 
            for i in range(len(p)+1):
                f=p[:i]
                s=p[i:]

                per(f+[num]+s,up[1:])

        per([],nums)
        return res
            



        
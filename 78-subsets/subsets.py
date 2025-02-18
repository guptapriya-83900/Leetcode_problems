class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #p for processed and u for unprocessed numbers
        final=[]
        def dfs(p,u):
            if not u:
                return [p]

            num = u[0]

            left =  dfs(p+[num],u[1:])
            right = dfs(p,u[1:])

            return left+right
        
        return dfs([],nums)

        
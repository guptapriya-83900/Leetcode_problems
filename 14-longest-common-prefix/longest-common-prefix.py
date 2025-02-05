class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        pre=strs[0]
        for i in strs:
            while not i.startswith(pre):
                pre=pre[:-1]
                if not pre:
                    return ""
        return pre

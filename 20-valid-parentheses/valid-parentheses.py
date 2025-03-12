class Solution:
    def isValid(self, s: str) -> bool:
        dic={ ")" : "(", "]" : "[", "}" : "{" }
        stack=[]

        for i in range(len(s)):
            if s[i] in dic:
                if stack and dic[s[i]]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if not stack else False
































        
        
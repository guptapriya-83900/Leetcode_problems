class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    

        def backtrack(index, p):
            if index == len(digits):  
                result.append("".join(p))
                return
            
            letters = digit_to_letters[digits[index]]  
            
            for letter in letters:  # Try each letter
                p.append(letter)  # Add letter
                backtrack(index + 1, p)  # Recur for the next digit
                p.pop()  # Backtrack (remove last letter)

        backtrack(0, [])  # Start with an empty combination
        return result
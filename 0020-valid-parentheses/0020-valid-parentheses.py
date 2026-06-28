class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for i in range(len(s)):
            if s[i] in matches:
                if not stack or stack[-1] != matches[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) == 0: 
            return True
        else: 
            return False
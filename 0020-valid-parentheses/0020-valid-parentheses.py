class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            # opening bracket: push to top of the stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            # closing bracket
            elif s[i] == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else: return False
            elif s[i] == '}' and stack:
                if stack[-1] == '{':
                    stack.pop()
                else: return False
            elif s[i] == ']' and stack:
                if stack[-1] == '[':
                    stack.pop()
                else: return False
            else: return False
        if len(stack) == 0:
            return True
        return False                  

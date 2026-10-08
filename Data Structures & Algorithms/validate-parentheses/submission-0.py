class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for c in s:
            if c in "{ [ (":
                stack.append(c)
            else:
                if stack and stack[-1] == '(' and c == ')':
                    stack.pop()
                elif stack and stack[-1] == '{' and c == '}':
                    stack.pop()
                elif stack and stack[-1] == '[' and c == ']':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
                
            
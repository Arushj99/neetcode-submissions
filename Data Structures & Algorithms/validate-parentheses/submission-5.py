class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', ']': '[', '}':'{'}
        stack = []
        for c in s:
           if stack and c in pair and pair[c] == stack[-1]:
                    stack.pop()
           else:
                stack.append(c)
              
        return not stack
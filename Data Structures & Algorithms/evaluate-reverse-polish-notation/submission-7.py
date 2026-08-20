class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ''' Since we know two values are guarenteed before any operator,
        we can use a stack to keep simplify each value, such that when the
        top element on the stack is an operator, then we perform the calculation 
        and replace the previous elements with that new value. We iterate
        through tokens and append to the stack. '''

        stack = []
        for i in tokens:
            if i in {"/", "+", "-", "*"}:
                b = stack.pop()
                a = stack.pop()
                if i == "/":
                    stack.append(int(a/b)) # // this is floor division, int(a/b) is truncation
                if i == "+":
                    stack.append(a+b)
                if i == "-":
                    stack.append(a - b)
                if i == "*":
                    stack.append(a*b)
            else:
                stack.append(int(i))
        return int(stack[0])

            
            
            
        
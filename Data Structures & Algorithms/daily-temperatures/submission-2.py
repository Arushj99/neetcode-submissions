class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures) - 1]
        res = [0]
        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)
            stack.append(i)

        return res[::-1]
                
            

            


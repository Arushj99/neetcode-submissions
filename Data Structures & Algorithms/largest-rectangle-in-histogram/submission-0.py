class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and height <= stack[-1][1]:
                i, h = stack.pop()
                maxArea = max((idx - i) * h, maxArea)
                start = i
            stack.append((start, height))

        while stack:
            i, h = stack.pop()
            maxArea = max((len(heights) - i) * h, maxArea)


        return maxArea

            


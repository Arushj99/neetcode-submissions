class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            area = min(heights[r], heights[l]) * (r - l)
            maxArea = max(maxArea, area)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea

        
class Solution:
    def trap(self, height: List[int]) -> int:
        mL, mR = height[0], height[-1]
        l, r = 1, len(height) - 2
        total = 0
        while r >= l:
            if mR > mL:
                total += max(min(mR, mL) - height[l], 0)
                mL = max(height[l], mL)
                l += 1
            else:
                total += max(min(mR, mL) - height[r], 0)
                mR = max(height[r], mR)
                r -= 1
                
        return total
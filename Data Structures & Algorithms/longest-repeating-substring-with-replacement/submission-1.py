class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' Can use sliding window to keep track of longest substring
        and keep extending the window until replacements are satisifed. 
        Need to keep track of most frequent character and subtract that from the
        length of the window, and then make sure that difference is <= k so I know
        I can make the correct amt of replacements. Otherwise, I can move the left 
        pointer right once, and then repeat the calculation. '''
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

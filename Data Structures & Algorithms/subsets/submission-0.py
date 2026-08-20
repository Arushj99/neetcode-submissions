class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, track):
            if i >= len(nums):
                res.append(track.copy())
                return

            track.append(nums[i])
            #[1]
            backtrack(i + 1, track)
            track.pop()
            #[]
            backtrack(i + 1, track)
        
        backtrack(0, [])
        return res

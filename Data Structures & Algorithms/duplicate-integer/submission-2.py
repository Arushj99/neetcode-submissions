class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i in count:
            if count[i] > 1:
                return True
        return False
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' I can iterate through nums and take i (for each element), 
        sort the list, and use a two pointer approach where I increment
        the left pointer if the sum of of the left and right pointer is 
        < target and decrement the right pointer if the sum is greater than 
        target. If the sum is equal, then I add it to the result list. '''

        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                 break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
           
            while l < r:
                total = nums[i] + nums[r] + nums[l]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res



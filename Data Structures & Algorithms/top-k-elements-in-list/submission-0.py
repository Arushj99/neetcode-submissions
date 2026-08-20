class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        result = [item[0] for item in d[:k]]
        return result
        
            

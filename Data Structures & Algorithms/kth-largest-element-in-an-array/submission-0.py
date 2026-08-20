class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       '''I want to make a max heap, but typical heap operations support
       min heaps, so I can make all the elements in nums negative then bigger
       numbers will be at the top of the heap because they'll be smaller when 
       made negative, and then when I pop them (which I want to do k times),
       then I can take the last element I pop and convert it back to positive
       and then return it ''' 
       max_heap = [-x for x in nums]
       heapq.heapify(max_heap)
       num = 0
       for i in range(k):
            num = heapq.heappop(max_heap)
       return -1*num


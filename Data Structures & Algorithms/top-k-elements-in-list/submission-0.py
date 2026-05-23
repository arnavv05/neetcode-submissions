import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key,val in count.items():
            heapq.heappush(heap, (-val, key))

        return [heapq.heappop(heap)[1] for x in range(k)]
        
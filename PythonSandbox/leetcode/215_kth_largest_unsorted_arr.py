import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapArr = [-n for n in nums]
        heapq.heapify(heapArr)

        kthLargest = -float('inf')
        for i in range(k):
            kthLargest = heapq.heappop(heapArr)
        return -kthLargest

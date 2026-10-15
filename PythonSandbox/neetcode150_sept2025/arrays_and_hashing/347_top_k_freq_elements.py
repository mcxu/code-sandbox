from typing import List
from collections import Counter
import heapq

class TopKFreqElements:
    """
    Let n = len(nums)
    TC: O(n log n), due to the sorted call. freqMap could have n elements if all elements in nums are unique.
    SC: O(n), both the freqMap and tuples can have n elements
    """
    def topKFrequent_freqMap(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        
        # sort tuples by freq
        tuples = sorted(freqMap.items(), key = lambda t: t[1])
        print("tuples: ", tuples)

        topk = []
        for i in range(len(tuples)-1, len(tuples)-1-k, -1):
            tupNum = tuples[i][0]
            topk.append(tupNum)
        
        return topk

    def test_1(self):
        nums = [1,2,1,2,1,2,3,1,3,2]
        result = self.topKFrequent_freqMap(nums, 2)
        print("result: ", result)
        assert set(result) == set([1,2])
    
    # ======================================================================
    """
    TC: 
    """
    def topKFrequent_minHeap(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)

        min_heap = []
        for (n,f) in freqMap.items():
            heapq.heappush(min_heap, (f,n))
        
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        topk = []
        while min_heap:
            popped = heapq.heappop(min_heap)[1]
            topk.append(popped)
        return topk
    
    def test_2(self):
        nums = [1,2,1,2,1,2,3,1,3,2]
        result = self.topKFrequent_minHeap(nums, 2)
        print("result: ", result)
        assert set(result) == set([1,2])
    
    def test_3(self):
        nums = [1,1,1,2,2,3]
        result = self.topKFrequent_minHeap(nums, 2)
        print(f"{result=}")
        assert set(result) == set([1,2])

if __name__ == "__main__":
    cl = TopKFreqElements()
    #cl.test_1()
    # cl.test_2()
    cl.test_3()

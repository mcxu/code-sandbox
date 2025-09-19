from typing import List
from collections import Counter
import heapq

class TopKFreqElements:
    def topKFrequent_freqMap(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} 
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
        
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

    def topKFrequent_minHeap(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)

        min_heap = []
        for tup in freqMap.items():
            element, freq = tup[0], tup[1]
            heapq.heappush(min_heap, (freq, element))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        while min_heap:
            popped_num = heapq.heappop(min_heap)[1]
            result.append(popped_num)

        return result
    
    def test_2(self):
        nums = [1,2,1,2,1,2,3,1,3,2]
        result = self.topKFrequent_minHeap(nums, 2)
        print("result: ", result)
        assert set(result) == set([1,2])

if __name__ == "__main__":
    cl = TopKFreqElements()
    #cl.test_1()
    cl.test_2() 
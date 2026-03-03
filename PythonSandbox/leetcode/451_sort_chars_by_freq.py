import heapq

class Solution:
    """ 
    With heapify:
        n ~ len(s)
        time complexity: O(n) because the freqMap for loop, heapify, and while loop all take O(n)
        space complexity: O(n), freqMap, heap all take O(n)
    With heappush:
        time complexity: O(n) because the O(nlogn) time complexity of heapush is overpowered by for and while loop
            The O(logn) time of heappop is also overpowered by for and while loop.
        space complexity: O(n)
    """
    def frequencySort(self, s: str) -> str:
        freqMap = {}

        # get freq count
        for i,c in enumerate(s):
            if c in freqMap.keys():
                freqMap[c] += 1
            else:
                freqMap[c] = 1

        # freq is made negative to make max heap
        #tupList = [(-freq, ch) for ch, freq in freqMap.items()]
        #heapq.heapify(tupList) # O(n) time complexity
        
        tupList = []
        for ch in freqMap:
            freq = freqMap[ch]
            heapq.heappush(tupList, (-freq, ch)) #O(nlogn) time complexity

        # rebuild string
        sOut = ""
        while len(tupList) > 0: # O(n) time
            tup = heapq.heappop(tupList) #O(logn) time 
            freq, ch = tup[0], tup[1]
            sOut += ch*(-freq)
        
        return sOut

class Solution2:
    def frequencySort(self, s: str) -> str:
        freqMap = {}

        # get freq count
        for i,c in enumerate(s):
            if c in freqMap.keys():
                freqMap[c] += 1
            else:
                freqMap[c] = 1
        
        # print("freqMap: ", freqMap)

        tupList = [(v,k) for k,v in freqMap.items()]
        # print("tupList: ", tupList)

        tupList = sorted(tupList, key = lambda x: x[0])
        # print("tupList after sort: ", tupList)

        # rebuild string
        sOut = ""
        for i in range(len(tupList)-1, -1, -1):
            tup = tupList[i]
            f, c = tup[0], tup[1]
            sOut += c*f
        
        return sOut
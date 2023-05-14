import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        ratioHeap = []
        # put class on heap by ratio
        for c in classes:
            ratio = (c[0]/c[1]) - ((c[0]+1)/(c[1]+1))
            heapq.heappush(ratioHeap, (ratio, c))
        
        # print("ratioHeap: ", ratioHeap)

        for _ in range(extraStudents):
            # get class with smallest denominator
            _, c = heapq.heappop(ratioHeap) # c: class
            # print('popped class: ', c)

            newClass = [c[0]+1, c[1]+1]
            newRatio = newClass[0]/newClass[1] - (newClass[0]+1)/(newClass[1]+1)
            newTup = (newRatio, newClass)
            # print("newTup: ", newTup)
            heapq.heappush(ratioHeap, newTup)

            # print('heap end of for: ', ratioHeap)

        # print("heap after for: ", ratioHeap)

        avgRatioForClasses = sum([c[0]/c[1] for r,c in ratioHeap])/len(ratioHeap)
        # print("avgRatioForClasses: ", avgRatioForClasses)
        return avgRatioForClasses
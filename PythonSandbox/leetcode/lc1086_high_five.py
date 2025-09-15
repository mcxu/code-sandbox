# https://leetcode.com/problems/high-five/
import heapq

class Solution:
    def highFive(self, items: [[int]]) -> [[int]]:
        scoreMap = {}
        for i,itm in enumerate(items):
            sid = itm[0]
            score = itm[1]
            if sid not in scoreMap.keys():
                scoreMap[sid] = [score]
            else:
                if len(scoreMap[sid]) >= 5:
                    if score > scoreMap[sid][0]:
                        heapq.heappop(scoreMap[sid])
                        heapq.heappush(scoreMap[sid], score)
                else:
                    heapq.heappush(scoreMap[sid], score)
        
        out = []
        for k in sorted(scoreMap.keys()): # k is student id
            avg = sum(scoreMap[k])//len(scoreMap[k])
            out.append([k, avg])
        return out
        
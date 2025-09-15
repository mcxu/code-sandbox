# https://leetcode.com/problems/find-right-interval/
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        m = {}
        for i,v in enumerate(intervals):
            start = v[0]; end = v[1]
            if start not in m.keys():
                m[start] = [end, i]
        
        maxKey = sorted(m.keys())[-1]
        #print("maxKey: ", maxKey)
        
        out = [-1 for _ in intervals]
        for i,v in enumerate(intervals):
            start = v[0]; end = v[1]
            if end > maxKey:
                out[i] = -1
            else:
                j = end
                while j <= maxKey:
                    if j in m.keys():
                        out[i] = m[j][1]
                        break
                    j += 1
            
        return out
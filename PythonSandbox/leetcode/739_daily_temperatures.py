'''
https://leetcode.com/problems/daily-temperatures/
'''
class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        out = [0 for _ in range(len(T))]
        stack=[]
        
        for i,t in enumerate(T):
            while stack and T[stack[-1]]<t:
                poppedIdx = stack.pop()
                out[poppedIdx]=i-poppedIdx
            stack.append(i)
        return out
        
# TLE
# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         idxMap = {}
#         for i,t in enumerate(T):
#             if t in idxMap.keys():
#                 idxMap[t].append(i)
#             else:
#                 idxMap[t] = [i]
                
#         tkSorted = sorted(idxMap.keys())
#         out = []
#         for i,t in enumerate(T):
#             minIdxAfteri = len(T)
#             for _,t2 in enumerate(tkSorted):
#                 if t2 > t:
#                     for k in idxMap[t2]:
#                         if k > i and k < minIdxAfteri:
#                             minIdxAfteri = k
            
#             if minIdxAfteri==len(T):
#                 out.append(0)
#             else:
#                 out.append(minIdxAfteri-i)
            
#         return out
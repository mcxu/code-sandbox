# https://leetcode.com/problems/different-ways-to-add-parentheses/
class Solution:
    def __init__(self):
        self.eval = {
            '+' : lambda a,b: a+b,
            '-' : lambda a,b: a-b,
            '*' : lambda a,b: a*b
        }
        self.m = {}
        
    def diffWaysToCompute(self, input: str) -> [int]:
        return self.ways(input)
    
    def ways(self, input):
        if input in self.m.keys():
            return self.m[input]
        
        ans = []
        for i,ch in enumerate(input):
            if ch in self.eval.keys():
                leftSubstr = input[:i]
                rightSubstr = input[i+1:]
                #print("leftSubstr: {}, rightSubstr: {}".format(leftSubstr, rightSubstr))
                leftWays = self.ways(leftSubstr)
                rightWays = self.ways(rightSubstr)
                #print("leftWays: {}, rightWays: {}".format(leftWays, rightWays))
                
                for a in leftWays:
                    for b in rightWays:
                        if a and b:
                            res = self.eval[ch](int(a),int(b))
                            ans.append(str(res))
        if not ans:
            ans.append(input)
        #print("input: {}, ans: {}".format(input, ans))
        self.m[input]=ans
        #print("map: ", self.m)
        return self.m[input]
                
'''
https://leetcode.com/problems/asteroid-collision/
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''
class Solution:
    def asteroidCollision(self, asteroids: [int]) -> [int]:
        stack = []
        for i,v in enumerate(asteroids):
            #print("v: ", v)
            if not stack:
                stack.append(v)
            else:
                if v>0 or (v<0 and stack[-1]<0):
                    stack.append(v)
                else:
                    if abs(v)>abs(stack[-1]):
                        stack[-1] = v
                    elif abs(v)==abs(stack[-1]):
                        stack.pop()
            
            self.removeCollisions(stack)
        
        return stack
    
    # mutates stack to remove collisions 
    def removeCollisions(self, stack):              
        j = len(stack)-1
        while stack and stack[j-1]>0 and stack[j]<0:
            #print("stack while: ", stack)
            if abs(stack[j-1])>abs(stack[j]):
                stack.pop()
            elif abs(stack[j-1])==abs(stack[j]):
                stack.pop(j-1)
                stack.pop()
                j -= 1
            else:
                stack[j-1]=stack[j]
                stack.pop()
            j -= 1
    
    def test1(self):
        ast = [[5, 10, -5], [8, -8], [10, 2, -5], [-2, -1, 1, 2]]
        exp = [[5,10]     , [],      [10]       , [-2, -1, 1, 2]]
        for a,e in zip(ast,exp):
            res = self.asteroidCollision(a)
            print("test: {}\tres: {}".format(a,res), end="\t")
            if e==res: print("pass") 
            else: print("fail")


sol = Solution()
sol.test1()
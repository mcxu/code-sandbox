'''
https://codeforces.com/blog/entry/67618
input: 1-d array [1, 3, 3, 3, 2, 2, 2, 3, 1]
return: [1, 1] (Explanation:- 133322231->133331->11).
133322231->122231->131 gives answer as [131] which is not the shortest.
'''
class Solution:
    def onedCandyCrush(self, arr):
        stack = []
        i = len(arr)-1
        while i >= 0:
            v = arr[i]
            print("i={}, v: {}".format(i,v))
            print("stack: ", stack)
            if not stack:
                stack.append(v)
            else:
                if stack[-1] == v:
                    stack.append(v)
                    print("stack top same as value. stack: ", stack)
                    if i == 0 and len(stack) >= 3:
                        print("i is 0 and stack >= 3. stack: ", stack)
                        while stack:
                            arr.pop(0)
                            stack.pop()
                else:
                    if len(stack) >= 3:
                        j = i+1
                        print("j=", j)
                        while stack:
                            arr.pop(j)
                            stack.pop()
                        i = len(arr)
                        print("i set to: ", i)
                        print("stack now: ", stack)
                    else:
                        stack.clear()
                        stack.append(v)
                        print("stack cleared, updated: ", stack)
            i -= 1

        print("arr final: ", arr)
        print("stack final: ", stack)
        return arr
    
    def test1(self):
        arr = [1, 3, 3, 3, 2, 2, 2, 3, 1] # expected: [1,1]
        #arr = [3,2,3] # expected: [3,2,3]
        #arr = [3,3,3,1] # expected: [1]
        #arr = [1,3,3,3] # expected: [1]
        #arr = [1,3,3,3,1] # expected: [1,1]
        #arr = [3,3,3] # expected: []
        #arr = [1,1,1] # expected: []
        #arr = [1, 1, 3, 3, 3, 2, 2, 2, 3, 1] # expected: [], 3 1's get removed.
        #arr = [1] # expected: [1]
        #arr = [] # expected: []
        res = self.onedCandyCrush(arr)
        print("res: ", res)

sol = Solution()
sol.test1()

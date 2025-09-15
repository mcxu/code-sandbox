"""
https://leetcode.com/problems/validate-stack-sequences/
"""
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        stack = []
        for i in range(len(pushed)):
            pushNum = pushed[i]
            stack.append(pushNum)

            while pushed and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
        return j == len(popped)

    def test(self):
        pushed = [1,2,3,4,5]
        popped = [4,5,3,2,1]
        expected = True
        result = self.validateStackSequences(pushed, popped)
        print("result: ", result)
        assert expected == result

    def test2(self):
        pushed = [1,2,3,4,5]
        popped = [4,3,5,1,2]
        expected = False
        result = self.validateStackSequences(pushed, popped)
        print("result: ", result)
        assert expected == result

s = Solution()
s.test()
# s.test2()

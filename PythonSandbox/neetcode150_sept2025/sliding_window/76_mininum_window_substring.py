# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter
import json
from typing import Callable

class MinWindowSubstring:
    """
    Time complexity: O(t * s^2) where t and s correspond to the lengths of their respective strings.
    Space complexity: O(s + t), since the Counter objects can have s+t elements at most
    """
    def minWindow_bruteForce(self, s:str, t:str) -> str:
        if s == t:
            return t
        if len(s) < len(t):
            return ""

        scount = Counter()
        # print("scount: ", scount)
        tcount = Counter(t)
        # print("tcount: ", tcount)

        minWindow = (0, len(s)-1)
        # print("minWindow START: ", minWindow)

        s_had_t_at_least_once = False

        for i in range(len(s)):
            ichar = s[i]
            if ichar in tcount:
                for j in range(i, len(s)):
                    # substr = s[i:j+1] # for test
                    # print("---\ni= ", i, "  j= ", j, " substr: ", substr, f"letters: {s[i]}, {s[j]}")
                    jchar = s[j]
                    scount.update(jchar)
                    # print("scount[2]: ", scount)
                    s_has_t = all(scount[k] >= tcount[k] for k in tcount)
                    # print("s_has_t: ", s_has_t)
                    if s_has_t and (j-i) <= (minWindow[1] - minWindow[0]):
                        minWindow = (i, j)
                        # print("xx minWindow set: ", minWindow)
                        s_had_t_at_least_once = True
                scount.clear()
                    
        # print("minWindow FINAL: ", minWindow)

        if not s_had_t_at_least_once:
            return ""
        
        return s[minWindow[0]: minWindow[1]+1]
    
    
    """
    Time complexity: O(s * t), outer for loop iterates through s,
        The all() statement iterates through at most t elements under the hood.
    Space complexity: O(s + t)
    """
    def minWindow_optimized(self, s:str, t:str) -> str:
        scount = Counter()
        tcount = Counter(t)
        #print("tcount: ", tcount)
        minWindow = (0, len(s))
        leftIdx = 0

        for rightIdx in range(len(s)):
            rightChar = s[rightIdx]
            #print("---- rightIdx: ", rightIdx, "   rightChar: ", rightChar)
            scount.update(rightChar)
            #print("scount A: ", scount)
            #print("minWindow curr: ", minWindow)
        
            while leftIdx <= rightIdx and all(scount[k] >= tcount[k] for k in tcount):
                #print("- while loop: leftIdx:", leftIdx, "  rightIdx:", rightIdx)
                if rightIdx-leftIdx+1 < minWindow[1]-minWindow[0]:
                    minWindow = (leftIdx, rightIdx+1)
                    #print("minWindow set to: ", minWindow)

                leftChar = s[leftIdx]
                #print("leftChar: ", leftChar)
                scount[leftChar] -= 1
                if scount[leftChar] == 0:
                    scount.pop(leftChar)
                #print("scount after removing a leftChar: ", scount)

                leftIdx += 1

            #print("scount after while: ", scount)

        # if minWindow never changed from beginning, and leftIdx never incremented, then return empty string
        if minWindow == (0,len(s)) and leftIdx == 0:
            return ""

        return s[minWindow[0] : minWindow[1]]
    

    def test(self):
        FN_TO_TEST: Callable = self.minWindow_optimized

        tests = [
            dict(s="ADOBECODEBANC", t="ABC", expected="BANC"), # 1
            dict(s="a", t="b", expected=""), 
            dict(s="ab", t="b", expected="b"),
            dict(s="ab", t="a", expected="a"),
            dict(s="ab", t="A", expected=""),
            dict(s="abc", t="ac", expected="abc"), # 6
            dict(s="babb", t="baba", expected=""), # 7
        ]

        # test case 8
        with open("PythonSandbox/neetcode150_sept2025/resources/76_min_window_substring_test.json") as file:
            addl_tests = json.load(file)
            # print("addl_tests: ", addl_tests)
            for case in addl_tests:
                tests.append(case)

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["s"], tc["t"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation

if __name__ == "__main__":
    c = MinWindowSubstring()
    c.test()
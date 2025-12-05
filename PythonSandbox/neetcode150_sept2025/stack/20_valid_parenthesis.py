from typing import Callable

class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            schar = s[i]
            
            if stack:
                if stack[-1]=="(" and schar==")":
                    stack.pop()
                elif stack[-1]=="{" and schar=="}":
                    stack.pop()
                elif stack[-1]=="[" and schar=="]":
                    stack.pop()
                else:
                    stack.append(schar)
            else:
                stack.append(schar)
        
        if stack:
            return False
        
        return True
    
    def test(self):
        FN_TO_TEST: Callable = self.isValid
        
        tests = [
            dict(s="()", expected=True),
            dict(s="({[)", expected=False),
            dict(s="(])", expected=False),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["s"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation

if __name__=="__main__":
    c = ValidParenthesis()
    c.test()

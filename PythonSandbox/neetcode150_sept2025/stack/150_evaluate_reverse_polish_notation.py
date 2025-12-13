from typing import List, Callable

class EvaluateRPN:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operationsMap = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(a/b)
        }

        for _,t in enumerate(tokens):
            if t in operationsMap:
                pop1 = stack.pop()
                pop2 = stack.pop()
                result = operationsMap[t](pop2, pop1)
                stack.append(result)
            else:
                stack.append(int(t))
        
        return stack[-1] if stack else 0


    def test1(self):
        FN_TO_TEST: Callable = self.evalRPN

        tests = [
            dict(tokens=["2","1","+","3","*"], expected=9),
            dict(tokens=["4","13","5","/","+"], expected=6),
            dict(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"], expected=22),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i} \nCASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["tokens"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation


if __name__ == "__main__":
    c = EvaluateRPN()
    c.test1()

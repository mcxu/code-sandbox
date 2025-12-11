from typing import List, Callable

class DailyTemps:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in temperatures]
        stack = []

        for i,t in enumerate(temperatures):
            print("=== i=", i, " stack: ", stack)
            while stack and temperatures[stack[-1]] < t:
                idxOfLesserTemp = stack.pop()
                print("idxOfLesserTemp: ", idxOfLesserTemp)
                output[idxOfLesserTemp] = i - idxOfLesserTemp
                print("output so far: ", output)

            stack.append(i)

        return output

    def test1(self):
        FN_TO_TEST: Callable = self.dailyTemperatures

        tests = [
            dict(temperatures=[73,74,75,71,69,72,76,73], expected=[1,1,4,2,1,1,0,0]),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["temperatures"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation


if __name__ == "__main__":
    c = DailyTemps()
    c.test1()


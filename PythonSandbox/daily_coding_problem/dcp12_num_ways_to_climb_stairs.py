"""
Problem #12 [Hard] This problem was asked by Amazon. 
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

class DCP12:
    def get_num_unique_ways(self, N: int):
        if N < 0:
            return 0
        if N == 0:
            return 1
        
        take1 = self.get_num_unique_ways(N-1)
        take2 = self.get_num_unique_ways(N-2)
        num_unique_ways = take1 + take2

        return num_unique_ways
    
    def test(self):
        testcases = [
            {"N": 0, "expected": 1},
            {"N": 1, "expected": 1},
            {"N": 4, "expected": 5},
        ]

        for case in testcases:
            testnum = case["N"]
            expected = case["expected"]
            num_ways = self.get_num_unique_ways(testnum)
            print("--- testnum: ", testnum)
            print("expected: ", expected)
            print("num_ways: ", num_ways)
            assert num_ways == expected
    

if __name__ == "__main__":
    obj = DCP12()
    obj.test()

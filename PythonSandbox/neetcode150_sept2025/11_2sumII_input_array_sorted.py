from typing import List

class TwoSumII:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            iVal = numbers[i]
            jVal = numbers[j]
            total = iVal + jVal

            if total == target:
                return [i+1, j+1]
            elif total > target:
                j -= 1
            else:
                i += 1
        
        return [i+1, j+1]


    def test_1(self):
        test_cases = [
            [[2,7,11,15], 9, [1,2]],
            [[2,3,4], 6, [1,3]],
            [[-1,0], -1, [1,2]]
        ]
        for tc in test_cases:
            numbers = tc[0]
            target = tc[1]
            expected = tc[2]
            output = self.twoSum(numbers, target)
            print("output: ", output)
            assert output == expected

if __name__ == "__main__":
    cl = TwoSumII()
    cl.test_1()
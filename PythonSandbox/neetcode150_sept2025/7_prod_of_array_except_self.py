from typing import List

class ProdOfArrayExceptSelf:
    def prodExceptSelf(self, nums: List[int]) -> List[int]:
        allProd = 1
        zeroIndices = set()
        
        for i,n in enumerate(nums):
            if n == 0:
                zeroIndices.add(i)
            else:
                allProd *= n
        
        # print("allProd: ", allProd)
        # print("zeroIndices: ", zeroIndices)
        # zeroIndices [2]
        output = []
        for i,n in enumerate(nums):
            if i in zeroIndices:
                if len(zeroIndices) > 1:
                    output.append(0)
                else:
                    output.append(allProd)
            else:
                if len(zeroIndices) >= 1:
                    output.append(0)
                else:
                    output.append(int(allProd/n))

        return output

    def test_1(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]

        output = self.prodExceptSelf(nums)
        print("output: ", output)
        assert output == expected

    def test_2(self):
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]

        output = self.prodExceptSelf(nums)
        print("output: ", output)
        assert output == expected

    def test_3(self):
        nums = [-1,1,1,-3,3,1,0,-5,3,1,2]
        expected = [0,0,0,0,0,0,-270,0,0,0,0]

        output = self.prodExceptSelf(nums)
        print("output: ", output)
        assert output == expected

if __name__ == "__main__":
    cl = ProdOfArrayExceptSelf()
    # cl.test_1()
    # cl.test_2()
    cl.test_3()
    
from typing import List, Callable

class Search2DMatrix:
    """
    Time complexity: O(log(m*n)) = O(log(m)) + O(log(n)) [product rule]
    Space complexity: O(max(m, n)): Either searchColumn or searchRow, whichever one's larger
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        searchColumn = [row[-1] for row in matrix]

        lo, hi = 0, len(searchColumn)-1

        while lo <= hi:
            mid = int((lo+hi)/2)
            midVal = searchColumn[mid]

            if target == midVal:
                return True
            elif target < midVal:
                hi = mid-1
            elif target > midVal:
                lo = mid+1

        # print(f"lo: {lo}, mid: {mid}, hi: {hi}")

        if lo > len(matrix)-1:
            return False

        targetRowIdx = lo
        searchRow = matrix[targetRowIdx]
        lo, hi = 0, len(searchRow)-1

        while lo <= hi:
            mid = int((lo+hi)/2)
            midVal = searchRow[mid]

            if target == midVal:
                return True
            elif target < midVal:
                hi = mid-1
            elif target > midVal:
                lo = mid+1
        
        return False
    

    def test1(self):
        FN_TO_TEST: Callable = self.searchMatrix

        tests = [
            dict(nums=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=23, expected=True),
            dict(nums=[[1]], target=2, expected=False),
            dict(nums=[[1,3,5,7],[10,11,16,20],[23,30,34,50]], target=10, expected=True),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["nums"], tc["target"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = (output == tc["expected"])
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation

if __name__ == "__main__":
    c = Search2DMatrix()
    c.test1()
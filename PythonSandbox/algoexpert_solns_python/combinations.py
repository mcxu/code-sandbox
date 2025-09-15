#from utils.number_utils import NumberUtils
class Combinations:
    @staticmethod
    def solve(target, sum, candidates, answer):
        if sum == target:
            print(answer)
            return
    
        if len(candidates) == 0 or sum > target:
            return
    
        print("candidates: ", candidates)
        first = candidates[0]
        print("first: ", first)
        count = candidates.count(first)
        print("count: ", count)
    
        answer.append(first)
        Combinations.solve(target, sum+first, candidates[1:], answer)  #using the current number
        answer.pop()
        Combinations.solve(target, sum, candidates[count:], answer)    #skipping the current number and any duplicates

    @staticmethod
    def test_solve():
        candidates = [10, 1, 2, 7, 6, 1, 5]
        candidates.sort()
        Combinations.solve(8, 0, candidates, [])
    
    """
    find all combinations (order doesn't matter) of size k in array using depth first search
    returns combination lists in sorted order, and values of each list is also sorted.
    """
    @staticmethod
    def arrayCk(inputArray, k):
        return Combinations.arrayCkHelper(inputArray, k, [])
    
    
    #uses DFS to traverse all combinations of size k (TODO: incorrect)
    @staticmethod
    def arrayCkHelper(inputArray, k, visited=[], solns=[]):
        num = inputArray.pop(0)
        print("num: ", num)
        visited.append(num)
        print("    visited:", visited)
        for num in visited:
            print("    inputArray:", inputArray)
            
            combo = [visited[0]]
            combo.append(inputArray[0])
            print("    combo:", combo)
            
            solns.append(combo)
            print("    solns:",solns)
            
            Combinations.arrayCkHelper(inputArray, k, visited, solns)
        return visited
    
                  
    @staticmethod
    def test_arrayCk():
        l = [1,2,3,4,5]
        result = Combinations.arrayCk(l, 3)
        print("test_arrayCk: result: ", result)
        

    # https://stackoverflow.com/questions/12970897/can-you-explain-this-recursive-n-choose-k-code-to-me  
    # n Combination k (finds number of combos, but not the combos themselves)
    @staticmethod
    def nCk_recursive(n, k): 
        if k == 0:
            return 1
        if n == k:
            return 1
        else:
            return Combinations.nCk_recursive(n-1, k-1) + Combinations.nCk_recursive(n-1, k)
    
    @staticmethod
    def test_nCk_recursive():
        numsList = [
            [1,2,3,4],
            [12, 3, 1, 2, -6, 5, -8, 6]
            ]
        k = 3
        for nums in numsList:
            results = Combinations.nCk_recursive(len(nums), k)
            print("test_nCk_recursive: input: {}, k={}".format(nums, k))
            print("test_nCk_recursive: number of combinations: ", results)
            print("")
    
    # @staticmethod
    # def nCk_formula(n, k):
    #     n = NumberUtils.factorial(n)
    #     d = NumberUtils.factorial(n-k)*NumberUtils.factorial(k)
    #     return int(n/d)
    
    @staticmethod
    def test_nCk_formula():
        numsList = [
            [1,2,3,4],
            [12, 3, 1, 2, -6, 5, -8, 6]
            ]
        k = 3
        for nums in numsList:
            results = Combinations.nCk_recursive(len(nums), k)
            print("test_nCk_formula: input: {}, k={}".format(nums, k))
            print("test_nCk_formula: number of combinations: ", results)
            print("")

def main():
    #Combinations.test_solve()
    Combinations.test_arrayCk()
    #Combinations.test_nCk_recursive()
    #Combinations.test_nCk_formula()

main()
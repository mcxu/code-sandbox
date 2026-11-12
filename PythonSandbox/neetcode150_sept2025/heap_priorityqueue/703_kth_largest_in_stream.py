import ast
import heapq
from pathlib import Path

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        print("after heapify:", self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        print("heap at end of init:", self.heap)
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def test1():
    #inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    inputs = [[2,[0]],[-1],[1],[-2],[-4],[3]]
    kl = None
    kthNums = []
    for i in range(len(inputs)):
        print("---- i=", i)
        if i == 0:
            initialInputs = inputs[0]
            print("init:", initialInputs)
            k = initialInputs[0]
            nums = initialInputs[1]
            kl = KthLargest(k, nums)
            print("heap after init:\n", kl.heap)
        else:
            inp = inputs[i][0]
            print("inserting:", inp)
            returnedNum = kl.add(inp)
            print("heap after insert:\n", kl.heap)
            print(f"{returnedNum=}")
            kthNums.append(returnedNum)
    print("kthNums:\n", kthNums)


def test2():
    inputs = [[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
    kl = None
    kthNums = []
    for i in range(len(inputs)):
        if i == 0:
            initialInputs = inputs[0]
            print("init:", initialInputs)
            k = initialInputs[0]
            nums = initialInputs[1]
            kl = KthLargest(k, nums)
        else:
            returnedNum = kl.add(inputs[i][0])
            print(f"{returnedNum=}")
            kthNums.append(returnedNum)
    print("kthNums:\n", kthNums)

def test3():
    input_path = Path(__file__).parent / "kth_largest_in_stream_test2_input.txt"
    inputs = ast.literal_eval(input_path.read_text(encoding="utf-8"))
    kl = None
    returnedNums = []
    for i in range(len(inputs)):
        if i == 0:
            initialInputs = inputs[0]
            print("init: k=", initialInputs[0], " nums len=", len(initialInputs[1]))
            k = initialInputs[0]
            nums = initialInputs[1]
            kl = KthLargest(k, nums)
            print("heap after populating:\n", kl.heap)
        else:
            returnedNum = kl.add(inputs[i][0])
            returnedNums.append(returnedNum)
            if i <= 5 or i == len(inputs) - 1:
                print(f"add #{i} val={inputs[i][0]} {returnedNum=}")
    print(f"finished {len(inputs) - 1} add() calls")
    print("returnedNums:\n", returnedNums)

if __name__ == "__main__":
    test1()
    # test2()
    # test3()

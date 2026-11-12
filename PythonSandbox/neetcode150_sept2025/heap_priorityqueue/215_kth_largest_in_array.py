import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify_max(nums)
        #print("heap after heapify:", nums)
        kthLargest = None
        for _ in range(k):
            kthLargest = heapq.heappop_max(nums)
        return kthLargest
    
    def test1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        result = self.findKthLargest(nums, k)
        print("result:", result)

if __name__ == "__main__":
    s = Solution()
    s.test1()


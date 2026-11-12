import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(f"x={x}, y={y}")
            if x != y:
                newy = abs(y - x)
                heapq.heappush_max(stones, newy)
        
        if stones:
            return stones[0]
        
        return 0

    def test1(self):
        # stones = [2,7,4,1,8,1]
        #stones = [1]
        stones = [1,2]
        result = self.lastStoneWeight(stones)
        print(f"{result=}")

if __name__ == "__main__":
    s = Solution()
    s.test1()
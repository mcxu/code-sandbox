from typing import Callable
import math

class KokoEatingBananas:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        i = 1
        j = max(piles)
        k_min = j

        while i <= j:
            k_eval = (i + j)//2

            hours_for_k_eval = 0
            for p in piles:
                hours_for_k_eval += math.ceil(p/k_eval)
            
            if hours_for_k_eval <= h:
                k_min = k_eval
                j = k_eval - 1
            else:
                i = k_eval + 1
        
        return k_min


    def test1(self):
        FN_TO_TEST: Callable = self.minEatingSpeed

        tests = [
            dict(piles=[3, 6, 7, 11], h=8, expected=4),
            dict(piles=[30, 11, 23, 4, 20], h=5, expected=30),
            dict(piles=[30, 11, 23, 4, 20], h=6, expected=23),
        ]

        for i, tc in enumerate(tests, start=1):
            print(f"\n== RUNNING test{i}  CASE:", str(tc)[:100])
            output = FN_TO_TEST(tc["piles"], tc["h"])
            print(f"RESULTS FOR test{i}:\n{output}")
            evaluation = output == tc["expected"]
            if evaluation == False:
                print("TEST NUMBER FAILED: ", i)
                assert evaluation


if __name__ == "__main__":
    c = KokoEatingBananas()
    c.test1()

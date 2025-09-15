"""
Problem #13 [Hard]
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

class DCP13:
    def get_longest_substring_with_k_distinct_chars(self, s: str, k: int) -> int:
        seen_chars = set()
        i, j = 0, 0
        longest_so_far = 1
        
        while j < len(s):
            jchar = s[j]
            if jchar not in seen_chars:
                seen_chars.add(jchar)

                if len(seen_chars) > k:
                    ichar = s[i]
                    if ichar in seen_chars:
                        seen_chars.remove(ichar)
                    i += 1
            else:
                longest_so_far = max(longest_so_far, j - i + 1)
                seen_chars.remove(jchar)
            j += 1
        
        return longest_so_far
        
    def test1(self):
        testcases = [
            {"s": "abcba", "k": 2, "expected": 3},
            {"s": "abcba", "k": 3, "expected": 5}
        ]

        for tc in testcases:
            s = tc["s"]
            k = tc["k"]
            expected = tc["expected"]
            result = self.get_longest_substring_with_k_distinct_chars(s, k)
            print(f"=== s={s}, k={k}")
            print(f"expected: ", expected)
            print(f"result: ", result)

if __name__ == "__main__":
    dcp = DCP13()
    dcp.test1()

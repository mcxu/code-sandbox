"""
Behind paywall on LC website but not on neetcode:
https://neetcode.io/problems/string-encode-and-decode/question
"""
from typing import List

class EncodeDecodeStr:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # print(f"{i=}, {j=}")
            while s[j] != "#":
                j += 1
                # print(f"j updated: {j}")
            length = int(s[i:j])
            # print(f"{length=}")
            res.append(s[j+1: j+1+length])
            i = j+1+length
        return res

    def test1(self):
        strs = ["Hello", "World"]
        encodedStrs = self.encode(strs)
        print(f"{encodedStrs=}")
        decodedStrs = self.decode(encodedStrs)
        print(f"{decodedStrs}")


if __name__ == "__main__":
    ed = EncodeDecodeStr()
    ed.test1()

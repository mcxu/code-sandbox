class LongestRepeatingCharReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {}
        maxFreq = 0
        maxSubstrLength = 0

        i, j = 0, 0
        while j < len(s):
            print(f"================= i: {i}, j: {j}")
            jChar = s[j]

            freqMap[jChar] = freqMap.get(jChar, 0) + 1

            maxFreq = max(freqMap.values())
            print('maxFreq: ', maxFreq)
            substrLength = j - i + 1
            print('substrLength (init): ', substrLength)
            requiredChanges = substrLength - maxFreq
            print('requiredChanges (init): ', requiredChanges)

            while requiredChanges > k:
                iChar = s[i]
                freqMap[iChar] -= 1
                print('freqMap: ', freqMap)
                
                maxFreq = max(freqMap.values())

                i += 1
                print("i=", i)
                substrLength = j - i + 1
                print('substrLength: ', substrLength)
                requiredChanges = substrLength - maxFreq
                print('requiredChanges set to: ', requiredChanges)

            maxSubstrLength = max(maxSubstrLength, substrLength)
            j += 1
        
        return maxSubstrLength

    def test_1(self):
        testCases = [
            # ("ABAB", 2, 4),
            # ("AABABBA", 1, 4),
            # ("ABAB", 0, 1),
            ("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4, 7)
        ]

        for tc in testCases:
            s, k, expected = tc[0], tc[1], tc[2]
            print(f'test case: s: {s}, k: {k}. Expected: {expected}')
            output = self.characterReplacement(s, k)
            print('output: ', output)

if __name__ == "__main__":
    cl = LongestRepeatingCharReplacement()
    cl.test_1()
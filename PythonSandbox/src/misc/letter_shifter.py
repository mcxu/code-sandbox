"""
Given non-empty string of lower case letters and a non-negative integer, k, 
shift each letter forwards by k position in the alphabet. 
Letters should also wrap around the alphabet.
"""

class LetterShifter:
    @staticmethod
    def shiftLetters(s, k):
        sList = list(s)
        for i,ltr in enumerate(sList):
            inc = ord(ltr) + k
            while inc > ord("z"):
                inc = ord("a") + (inc%ord("z")-1)
            sList[i] = chr(inc)
        return "".join(sList)
    
    @staticmethod
    def test_shiftLetters():
        s = "xyz"; k = 2
        s = LetterShifter.shiftLetters(s, k)
        print("shifted: ", s)
    
    @staticmethod
    def test_shiftLetters2():
        s = "abc"; k = 52
        s = LetterShifter.shiftLetters(s, k)
        print("shifted: ", s)

def main():
    #LetterShifter.test_shiftLetters()
    LetterShifter.test_shiftLetters2()
    
main()
"""
https://www.facebook.com/careers/life/sample_interview_questions

Implement a function that outputs the Look and Say sequence
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
"""

class LAS:
    
    # n: nth number in look and say sequence, starting from 1st number (1)
    @staticmethod
    def lookAndSay(n):
        initNumStr = "1"
        if n == 1:
            return initNumStr
        
        for i in range(n-1):
            nextNumStr = LAS.nextNumber(initNumStr)
            initNumStr = nextNumStr
        #print("initNumStr final: ", initNumStr)
        return initNumStr
    
    # given number, return next look and say number
    @staticmethod
    def nextNumber(nStr):
        nextNumStr = ""
        
        i = 0
        while i < len(nStr):
            #print("nStr[{}]= {}".format(i, nStr[i]))
            countFori = 1
            while i+1 < len(nStr) and nStr[i] == nStr[i+1]:
                #print("inner while: nStr[{}]= {}".format(i, nStr[i]))
                countFori += 1
                i += 1
            #print("countFori: ", countFori)
            nextNumStr += (str(countFori) + str(nStr[i]))
            i += 1
        
        #print("nextNumStr final: ", nextNumStr)
        return nextNumStr

    @staticmethod
    def test_nextNumber():
        nStr = "111221"
        LAS.nextNumber(nStr)
        
        nStr = "31131211131221"
        result2 = LAS.nextNumber(nStr)
        ans2 = "13211311123113112211"
        if result2 == ans2:
            print("2nd result matches")

    @staticmethod
    def test_lookAndSay():
        lasNum = LAS.lookAndSay(10)
        print("lasNum: ", lasNum)
        ans2 = "13211311123113112211"
        if lasNum == ans2:
            print("result matches")

#LAS.test_nextNumber()
LAS.test_lookAndSay()
            
'''
String decompression

Given a compressed string of the format number[string],
return the decompressed string in the form: string written number times.

Input: 3[abc]4[ab]c
Output: abcabcabcababababc

Input: 2[3[a]b]
Output: aaabaaab

https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge
'''

class Prob:
    @staticmethod
    def decompressString(s):
        
        def helper(s, bracketStack):
            nonlocal dcs
            print("s: {}, dcs: {}, bracketStack: {}".format(s, dcs, bracketStack))
            if not s or '[' not in s:
                dcs += s
                return
            
            numStr = s[0]
            i = 1
            charStr = s[i]
            bracketStack.append(charStr)
            joinedStr = ""
            while bracketStack:
                if bracketStack[-1] == '[' and s[i] == ']':
                    bracketStack.pop()
                    #helper(s[:i], bracketStack)
                elif s[i] != '[':
                    joinedStr += s[i]
                print("bracketStack: ", bracketStack)
                i += 1
            print("i final=", i)
            joinedStr *= int(numStr)
            print("joinedStr: ", joinedStr)
            dcs += joinedStr
            print("dcs: ", dcs)
            helper(s[i:], bracketStack)
            

        dcs = "" # decompressed string
        bracketStack = []
        helper(s, bracketStack)
        print("dcs after helper: ", dcs)
    
    @staticmethod
    def test1():
        #s = "3[abc]"
        s = "2[aqf]qwerty"
        Prob.decompressString(s)
        
    @staticmethod
    def test2():
        s = "3[abc]4[ab]c"
        Prob.decompressString(s)
    

Prob.test1()
#Prob.test2()
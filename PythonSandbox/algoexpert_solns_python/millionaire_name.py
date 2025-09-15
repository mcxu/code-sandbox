'''
Millionaire name generator.
Given a name, print the user's millionaire name.
For the aspiring multi-millionaire tech pro.

example:
netWorth: 2000000
name (as a millionaire (as a millionaire))
'''

class Solution:
    '''
    name: string
    netWorth: net worth, in dollars
    '''
    @staticmethod
    def editName(name, netWorth):
        amtMap = {
            10**6:"millionaire",
            10**9:"billionaire",
            10**12:"trillionaire"
        }
        kSorted = sorted(amtMap.keys())
        # [10^6, 10^9, 10^12]

        def editor(suffix, remaining, i):
            if i < 0 or remaining < kSorted[0]:
                return None
            
            if remaining >= kSorted[i]:
                diff = remaining-kSorted[i]
                word = amtMap[kSorted[i]]
                string = "(as a {}".format(word)
                suffRec = editor(suffix, diff, i)
                if suffRec:
                    string += suffRec + ")"
                else:
                    string += ")"
                return string
            
            return editor(suffix, remaining, i-1)

        if netWorth < kSorted[0]:
            return "You are too poor to use this program."
        
        suf = editor("", netWorth, len(kSorted)-1)
        return name + " " + suf
    
    @staticmethod
    def test1():
        name = "Mushu909"
        #netWorth = 5000000     # (as a millionaire (as a millionaire (as a millionaire (as a millionaire (as a millionaire)))))
        #netWorth = 2005000000  # (as a billionaire (as a billionaire (as a millionaire (as a millionaire (as a millionaire (as a millionaire (as a millionaire)))))))
        #netWorth = 2004567890 # (as a billionaire (as a billionaire (as a millionaire (as a millionaire (as a millionaire (as a millionaire))))))
        netWorth = 999999.99       # You are too poor to use this program.
        res = Solution.editName(name, netWorth)
        print("res: ", res)

Solution.test1()
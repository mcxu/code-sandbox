'''
Given huge nubmer of IP's in a list, remove duplicated addresses in list.
ref: https://aonecode.com/amazon-interview-questions-software-engineer 
'''

class Prob:
    @staticmethod
    def removeDuplicateIPs(ipList):
        ipSet = set(ipList) # O(n) time complexity
        return list(ipSet)

    @staticmethod
    def test1():
        ipList = ["1","2","3","1","3"]
        res = Prob.removeDuplicateIPs(ipList)
        print("test1 res: ", res)

Prob.test1()
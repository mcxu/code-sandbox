# https://leetcode.com/problems/reorder-data-in-log-files/
import functools

class Solution:
    def reorderLogFiles(self, logs: [str]) -> [str]:
        letItems = []
        i = 0
        while i < len(logs):
            logsplit = logs[i].split(" ")
            marker = logsplit[0]
            content = logsplit[1:]
            if not self.arrAllNum(content):
                letItems.append((marker, content))
                logs.pop(i)
                i -= 1
            i += 1
        #print("letItems: ", letItems)
        #print("logs after creating letMap: ", logs)
        letItems = sorted(letItems, key=functools.cmp_to_key(self.itemCompare))
        #print("letItems: ", letItems)
        out = []
        for i,item in enumerate(letItems):
            out.append(item[0] + " " + " ".join(item[1]))
        out += logs
        return out
    
    def itemCompare(self, item1, item2):
        iden1 = item1[0]; iden2 = item2[0]
        cont1 = item1[1]; cont2 = item2[1]
        sortedItems = sorted([cont1, cont2])
        if cont1 == cont2:
            sortedIden = sorted([iden1, iden2])
            if iden1 == iden2:
                return 0
            elif sortedIden[0] == iden1:
                return -1
            elif sortedIden[0] == iden2:
                return 1
        elif sortedItems[0] == cont1:
            return -1
        elif sortedItems[0] == cont2:
            return 1
    
    def arrAllNum(self, arr):
        for i in range(len(arr)):
            if not arr[i].isnumeric():
                return False
        return True
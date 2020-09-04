'''
https://leetcode.com/problems/validate-ip-address/
'''

class Solution:
    def validIPAddress(self, IP: str) -> str:
        neither = "Neither"; ipv4 = "IPv4"; ipv6 = "IPv6"
        typ = neither
        for i in range(len(IP)):
            ch = IP[i]
            if ch == ".":
                typ = ipv4
                break
            if ch == ":":
                typ = ipv6
                break
        
        ipSplit = []
        if typ == ipv4:
            ipSplit = IP.split(".")
            if len(ipSplit) != 4:
                return neither
            
            for i,val in enumerate(ipSplit):
                if val.isnumeric():
                    valNum = int(val)
                    if not (0 <= valNum <= 255):
                        return neither
                    if str(valNum) != val:
                        return neither
                else:
                    return "Neither"
            return typ
                    
                
        elif typ == ipv6:
            ipSplit = IP.split(":")
            
            if len(ipSplit) != 8:
                return neither
            #print("ipSplit: ", ipSplit)
            for i,val in enumerate(ipSplit):
                if len(val) > 4:
                    return neither
                
                if not val:
                    return neither
                for j in range(len(val)):
                    if val[j].isalpha() and ord(val[j].upper()) > 70:
                        return neither
            
            return typ
        
        return typ
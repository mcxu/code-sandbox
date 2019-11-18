"""
This problem was asked by Twitter. [Medium]

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

class DCP11:
    def __init__(self):
        self.prefixMap = {
#             "a" : set(["anesthesiologist", "antihypertensive","aminotransferase", "arteriosclerosis",
#                    "anthropomorphism", "accommodationist" ,"archconservative", "atrioventricular"]),
            "d" : set(["dog", "doge", "deer", "deal"]),
            "y" : set(["yell", "yellow", "yes", "yeet", "yesterday"])
            }
    
    def autoComplete(self):
        run = True
        while(run):
            s = input("Query: ")
            if s == "<exit>":
                run = False
                print("exited the program")
            elif s == "<add>":
                #add entry
                entry = input("Add entry: ")
                print("entry to add: ", entry)
                self.addEntry(entry)
            else:
                # do search
                print("doing search")
                if s in self.prefixMap.keys():
                    # check if there's an exact match in prefixMap
                    print("match(a): ", self.prefixMap[s])
                elif s[0] in self.prefixMap.keys():
                    # check if 1st char of query matches anything in prefixMap
                    wordList = self.prefixMap.get(s[0])
                    matches = self.filterByPrefix(wordList, s)
                    # update map
                    if matches:
                        self.prefixMap[s] = matches
                        print("match(b): ", matches)
                    else:
                        print("match for {} not found.".format(s))
                else:
                    # match not found
                    print("match for {} not found.".format(s))
                print("map state: ", self.prefixMap)
    
    # add entry to prefixMap
    def addEntry(self, entry):
        if entry[0] not in self.prefixMap.keys():
            # handles case where 1st char is completely new
            self.prefixMap[entry[0]] = set()
            self.prefixMap[entry[0]].add(entry)
        else: 
            # handles case where 1st char matches a char in the map
            # add entry to all existing prefixes
            for i in range(1, len(entry)+1):
                strToi = entry[0:i]
                if strToi in self.prefixMap.keys():
                    self.prefixMap.get(strToi).add(entry)
            
        print("prefixMap after add:\n", self.prefixMap)
            
                
    # filter list of words by prefix
    def filterByPrefix(self, wordList, pfx):
        matches = set()
        for word in wordList:
            #print("filterByPrefix: word: ", wosrd)
            if pfx == word:
                matches.add(word)
            else:
                i = 0 
                
                # increment limit, determined by shortest term
                lim = len(pfx)
                if len(pfx) > len(word):
                    lim = len(word)
                 
                while(i < len(pfx) and i < lim and pfx[i] == word[i]):
                    i += 1
                
                if i == len(pfx):
                    matches.add(word)
            #print("match added: ", matches)
        return matches
                            
                

def main():
    dcp11 = DCP11()
    dcp11.autoComplete()

main()

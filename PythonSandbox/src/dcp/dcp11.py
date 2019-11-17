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
            "d" : ["dog", "deer", "deal"],
            "y" : ["yell", "yellow", "yes"]
            }
    
    def autoComplete(self):
        run = True
        while(run):
            query = input("Query: ")
            if query == "<exit>":
                run = False
                print("exited the program")
            else:
                # do search
                print("doing search")
                if query in self.prefixMap.keys():
                    # check if there's an exact match in prefixMap
                    print("match(a): ", self.prefixMap[query])
                elif query[0] in self.prefixMap.keys():
                    # check if 1st char of query matches anything in prefixMap
                    wordList = self.prefixMap.get(query[0])
                    matches = self.filterByPrefix(wordList, query)
                    # update map
                    if matches:
                        self.prefixMap[query] = matches
                        print("match(b): ", matches)
                    else:
                        print("match for {} not found.".format(query))
                else:
                    # match not found
                    print("match for {} not found.".format(query))
                print("map state: ", self.prefixMap)
                        
    # filter list of words by prefix
    def filterByPrefix(self, wordList, pfx):
        matches = []
        for word in wordList:
            print("filterByPrefix: word: ", word)
            if pfx == word:
                print("A")
                matches.append(word)
            else:
                print("B")
                i = 0 
                
                # increment limit, determined by shortest term
                lim = len(pfx)
                if len(pfx) > len(word):
                    lim = len(word)
                 
                while(i < len(pfx) and i < lim and pfx[i] == word[i]):
                    i += 1
                
                if i == len(pfx):
                    matches.append(word)
            #print("match added: ", matches)
        return matches
                            
                

def main():
    dcp11 = DCP11()
    dcp11.autoComplete()

main()

"""
Query: y
doing search
match(a):  ['yell', 'yellow', 'yes']
map state:  {'d': ['dog', 'deer', 'deal'], 'y': ['yell', 'yellow', 'yes']}
Query: ye
doing search
match(b):  ['yell', 'yellow', 'yes']
map state:  {'d': ['dog', 'deer', 'deal'], 'y': ['yell', 'yellow', 'yes'], 'ye': ['yell', 'yellow', 'yes']}
Query: yell
doing search
match(b):  ['yell', 'yellow']
map state:  {'d': ['dog', 'deer', 'deal'], 'y': ['yell', 'yellow', 'yes'], 'ye': ['yell', 'yellow', 'yes'], 'yell': ['yell', 'yellow']}
Query: yes
doing search
match(b):  ['yes']
map state:  {'d': ['dog', 'deer', 'deal'], 'y': ['yell', 'yellow', 'yes'], 'ye': ['yell', 'yellow', 'yes'], 'yell': ['yell', 'yellow'], 'yes': ['yes']}
Query: yellow
doing search
match for yellow not found.
map state:  {'d': ['dog', 'deer', 'deal'], 'y': ['yell', 'yellow', 'yes'], 'ye': ['yell', 'yellow', 'yes'], 'yell': ['yell', 'yellow'], 'yes': ['yes']}
"""
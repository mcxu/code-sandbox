'''
https://leetcode.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).
Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. 
You must return the indices in increasing order.
'''

class Solution:
    def peopleIndexes(self, favoriteCompanies):
        subsetMap = {} # for some person's index, list the indices of the other sets for which they are a subset.
        for i,person in enumerate(favoriteCompanies):
            compSet = set(person)
            for j,otherperson in enumerate(favoriteCompanies):
                if i != j:
                    otherCompSet = set(otherperson)
                    if compSet.issubset(otherCompSet):
                        if i in subsetMap.keys():
                            subsetMap[i].append(j)
                        else:
                            subsetMap[i] = [j]
        #print("subsetMap: ", subsetMap)
        
        exclusives = []
        for i,person in enumerate(favoriteCompanies):
            if i not in subsetMap.keys():
                exclusives.append(i)
        #print("exclusives: ", exclusives)
        return exclusives
    
    def test1(self):
        favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
        res = self.peopleIndexes(favoriteCompanies)
        print("res: ", res)
    
prob = Solution()
prob.test1()
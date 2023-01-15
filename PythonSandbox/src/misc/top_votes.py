'''
Given a list of votes and the times the votes were cast in the format ('candidate',time),
return the top k most popular candidates up to some given timestamp.

Example:
votes = [('b',17), ('a',3), ('c',7), ('c',21), ('d',23), ('b',15), ('c',16)]
timestamp = 17
k = 2
'''
from collections import OrderedDict

class TopVotes:
    def getTopVotes(self, votes, timestamp, k, includeEqualCandidates=False):
        voteCount = {}
        for i,v in enumerate(votes):
            vc = v[0]; vt = v[1]
            if vt <= timestamp:
                if vc in voteCount.keys():
                    voteCount[vc] += 1
                else:
                    voteCount[vc] = 1
        #print("voteCount: ", voteCount)
        voteTups = sorted(voteCount.items(), key=lambda item: item[1], reverse=True)
        #print("voteTups sorted: ", voteTups)
        if k >= len(voteTups):
            return [x[0] for x in voteTups]
        
        out = []
        for i in range(k):
            out.append(voteTups[i][0])
        
        # handles equally popular candidates
        if includeEqualCandidates:
            i = k
            while i < len(voteTups):
                if voteTups[i][1] == voteTups[i-1][1]:
                    out.append(voteTups[i][0])
                else:
                    break
                i += 1
        return out
        
    def test1(self):
        votes = [('b',17), ('a',3), ('c',7), ('c',21), ('d',23), ('b',15), ('c',16)]
        timestamp = 30
        k = 3
        res = self.getTopVotes(votes, timestamp, k, True)
        print("res: ", res)

tv = TopVotes()
tv.test1()
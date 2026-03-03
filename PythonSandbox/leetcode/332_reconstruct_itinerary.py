# https://leetcode.com/problems/reconstruct-itinerary/
class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        if not tickets: 
            return []
        
        adjList = {}
        for ticket in tickets:
            fr = ticket[0]
            to = ticket[1]
            if fr not in adjList.keys():
                adjList[fr] = [to]
            else:
                adjList[fr].append(to)
                
            if to not in adjList.keys():
                adjList[to] = []
        
        for k in adjList.keys():
            adjList[k].sort(reverse=True)
        
        print("adjList: ", adjList)
        
        # use stack to evaluate
        stack = ['JFK']
        output = []
        while stack:
            curr = stack[-1]
            print("stack: ", stack)
            print("adjList: ", adjList)
            if len(adjList[curr]) == 0:
                output.append(stack.pop())
                #print("output updated: ", output)
            else:
                nbr = adjList[curr].pop()
                stack.append(nbr)
        #print("output final: ", output)
        return output[::-1]
"""
Given intervals for when meetings are taking place, find the earliest time 
a new meeting of duration d can take place.

meetings = [[10, 50], [35, 70], [150, 170], [250, 300]]

If d = 80
expected: 70
because the meeting of duration 80 can fit between 70 and 150.

If d = 10
expected: 0
because the meeting of duration 10 can be placed as the first meeting. 

If d = 500
expected: 300
because the meeting of duration 500 can only go after the last meeting.


meetings = [[0,30], [10,20], [20,40],[60,80]]

"""

def findEarliestTime(meetings, d):
    earliestTimeSoFar = 0

    i = 0
    n = meetings[i]
    if d <= n[0]:
        return earliestTimeSoFar

    while i < len(meetings)-1:
        currMeeting = meetings[i]        
        nextMeeting = meetings[i+1]
        
        if currMeeting[1] + d <= nextMeeting[0]:
            earliestTimeSoFar = currMeeting[1]
            # print("earliestTimeSoFar updated: ", earliestTimeSoFar)

        i += 1

    if earliestTimeSoFar == 0:
        return meetings[-1][1]

    return earliestTimeSoFar

def test2():
    meetings = [[0,30], [10,20], [20,40],[60,80]]
    #d = 20 # expected res: 40
    #d = 10 # expected res: 40
    #d = 0 # expected res: 0 
    #d = 100 # expected res: 80
    #d = 30 # expected res: 80
    res = findEarliestTime(meetings, d)
    print("res: ", res)

test2()

def test():
    meetings = [[10, 30], [35, 70], [150, 170], [250, 300]]
    d = 10
    res = findEarliestTime(meetings, d)
    print("res:" , res)

#test()


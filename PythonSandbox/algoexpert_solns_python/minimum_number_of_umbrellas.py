'''
https://gist.github.com/lubien/1f09a53a4b5607377166c58a7eb49ae0

Given a number of people N and an array of integers, each one representing the amount of people a type of umbrella can handle, 
output the minimum number of umbrellas needed to handle N people.
No umbrella could have left spaces. Which means if a umbrella can handle 2 people, there should be 2 people under it.
If there's no solution, return -1.

Examples
solve(3, [1, 2]) means that we have 3 people and two kinds of umbrellas, one that hanled one person and one that handles 2. 
We can give one two-sized umbrella to 2 of them and the other to the last person. Therefore the solution is 2 (umbrellas). 
You could give 3 one-sized umbrellas, but we want the minimum number.

solve(10, [3, 1]). You can give 3 three-sized umbrellas and 1 one-sized. This means the solution is 4.

solve(3, [2]). There's no solution since one umbrella would have empty space. Return -1.
'''

def minNumOfUmbrellas(N, arr):
    # mininum number of umbrellas up to number of people
    mnuUpToNumPpl = [float('inf')] * (N+1)
    mnuUpToNumPpl[0] = 0 # min number of umbrellas for 0 people (index) is 0.

    for i in range(1, len(mnuUpToNumPpl)):
        for j in range(len(arr)):
            capacity = arr[j]
            if i-capacity >= 0:
                mnuUpToNumPpl[i] = min(mnuUpToNumPpl[i], mnuUpToNumPpl[i-capacity]+1)
            else:
                break
    if mnuUpToNumPpl[N]==float('inf'):
        return -1
    return mnuUpToNumPpl[N]

def test():
    #N=3; arr =[1,2]
    #N=10; arr=[3,1]
    N=3; arr=[2]
    res = minNumOfUmbrellas(N, arr)
    print("res: ", res)
test()

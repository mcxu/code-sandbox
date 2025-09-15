"""
This problem was asked by Facebook.
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, 
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.
"""
import time

"""
Dynamic Programming solution:
Time complexity: O(n*S), n~len(multiset), S~sum(multiset)
Space complexity: O(S)
"""
def canPartitionMultiset_DP(multiset):
    S = sum(multiset)
    print("S: ", S)
    if S % 2 != 0:
        return False
    
    print("S//2: ", S//2)

    dp = [False] * ((S//2) + 1)
    print("dp: ", dp)

    dp[0] = True # IF the total sum is 0, then this means there can be 2 partitions of 0 elements.

    for e in multiset:
        for j in range(S//2, e-1, -1):
            print(f"-- e: {e}, j: {j}")
            print(f"dp[j]={dp[j]}, dp[j-e]={dp[j-e]}")
            dp[j] = dp[j] or dp[j-e]
            print(f"dp[j] set to: ", dp[j])
    return dp[S//2]

def test1():
    s = [15, 5, 20, 10, 35, 15, 10] # expected: True
    # s = [15, 5, 20, 10, 35] # expected: False
    res = canPartitionMultiset_DP(s)
    print("res: ", res)

#test1()

# ==========================================================

def canPartitionMultiset_Recursive(s):
    # sList = sorted(s)
    # print("sList: ", sList)

    l1 = s
    l2 = []
    res = canPartitionSubsets(l1, l2)
    return res

def canPartitionSubsets(l1, l2):
    l1Sum = sum(l1)
    l2Sum = sum(l2)

    res = True
    if l1Sum == l2Sum:
        return res
    else:
        res = False

    for i,_ in enumerate(l1):
        popn = l1.pop(i)
        l2.append(popn)

        res |= canPartitionSubsets(l1, l2)

        if res == True:
            return True
        
        l1.insert(i, popn)
        l2.pop(-1)

    return res

def test2():
    s = [15, 5, 20, 10, 35, 15, 10] # expected: True
    # s = [15, 5, 20, 10, 35] # expected: False
    res = canPartitionMultiset_Recursive(s)
    print("res: ", res)

test2()

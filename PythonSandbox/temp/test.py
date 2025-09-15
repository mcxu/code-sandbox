# from collections import Counter

# s = "ffdafsdasdsddfsddade"

# freq = Counter(s)
# print("freq: ", freq)


# keys = freq.keys()
# print("keys: ", keys)

# x = 12
# xb = bin(x)
# print("xb: ", xb)
# y = 18
# yb = bin(y)
# print("yb: ", yb)

# print("OR: ", x|y)

def getBitwiseOr(nums):
    bitwiseOr = 0
    for n in nums:
        bitwiseOr |= n
    return bitwiseOr

nums = [8,1,2] 
k = 2
bo = getBitwiseOr(nums)
print("nums bo: ", bo)

newNums = [32,1,2]
nbo = getBitwiseOr(newNums)
print("newNums bo: ", nbo)

print(3593/16005)
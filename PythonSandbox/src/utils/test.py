def solution(S):
    max_sum = 0
    current_sum = 0
    positive = False
    n = len(S)
    for i in range(n):
        item = S[i]
        print("--- item: {}, pos: {}".format(item, positive))
        if item < 0:
            if current_sum > max_sum: # TODO
                max_sum = current_sum
            current_sum = 0
            print("A max_sum: ", max_sum)
            print("A curr_sum: ", current_sum)
        else:
            positive = True
            current_sum += item
            print("B pos changed: ", positive)
            print("B max_sum: ", max_sum)
            print("B curr_sum: ", current_sum)
    print("C pos: ", positive)
    print("C max_sum: ", max_sum)
    print("C curr_sum: ", current_sum)
    if (current_sum > max_sum):
        max_sum = current_sum
    if (positive):
        return max_sum
    return -1

def test():
    A=[1,2,-3,4,5,-6] # expected 9
    res = solution(A)
    print("res: ", res)
test()
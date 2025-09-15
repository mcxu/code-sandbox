def solution(s):
    count = 0
    rightlist = [None for _ in s]
    for i,ch in enumerate(s):
        if ch==">":
            rightlist[i] = ch
    
    while ">" in rightlist:
        for i in range(len(rightlist)):
            if s[i]=="<" and rightlist[i]==">":
                count += 1
        
        # shift > to the right in rightlist
        rightlist.insert(0, None)
        rightlist.pop()
        
    return count*2

def test_solution():
    #s = ">><<"
    #s = ">----<" # 2
    #s = "<<>><" # 4
    s = "--->-><-><-->-" # 10
    res = solution(s)
    print('res: ', res)
test_solution()
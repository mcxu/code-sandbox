def arrayManipulation(n, queries):
    aux = [0]*(n+1)
    
    for query in queries:
        f = query[0]; t = query[1]; d = query[2]
        aux[f-1] += d
        aux[t] += -d

    maxVal = aux[0]
    runSum = maxVal
    for i in range(1, len(aux)):
        runSum += aux[i]
        if runSum > maxVal:
            maxVal = runSum
    return maxVal
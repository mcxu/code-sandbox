import urllib3
import json

def getArticleTitles(author):
    titles = [] # stores string elements
    http = urllib3.PoolManager()
    q = getQuery(author, None)
    print("q: ", q)
    r = http.request('GET', q)
    print("r data: ", str(r.data))
    jsonObj = json.loads(r.data.decode('utf-8'))
    print("jsonObj: ", jsonObj)
    totalPages = int(jsonObj['total_pages'])
    jsonObjData = jsonObj['data']
    step3(jsonObjData, titles)

    print("**** totalPages: ", totalPages)
    for pg in range(2, totalPages+1):
        q = getQuery(author, pg)
        r = http.request('GET', q)
        jsonObj = json.loads(r.data.decode('utf-8'))
        jsonObjData = jsonObj['data']
        step3(jsonObjData, titles)
    
    print("titles final: ", titles)
    http.clear()
    return titles

def step3(jsonObjData, titles):
    for i,dataObj in enumerate(jsonObjData):
        print("i: {}, data: {}".format(i, dataObj))
        title = dataObj['title']
        print("TITLE: ", title)
        st = dataObj['story_title']
        print("STORY TITLE: ", st)
        if title != None:
            print("A")
            titles.append(title)
        elif title == None and st != None:
            print("B")
            titles.append(st)

def getQuery(authorName, num):
    q = "https://jsonmock.hackerrank.com/api/articles"

    if authorName:
        q += "?author={}".format(authorName)
    else:
        q += "?author=somedefaultauthor"
        if num and int(num) > 0:
            q += "&page={}".format(num)
        return q
    
    if num and int(num) > 0:
        q += "&page={}".format(num)
    return q

def testGet():
    author = "epaga"
    #author = "saintamh"
    getArticleTitles(author)

testGet()

# def testQuery():
#     #q = getQuery("asdf","33")
#     #q = getQuery("asdf", None)
#     #q = getQuery("", None)
#     q = getQuery("thomas", "234")
#     print("q: ", q)
# testQuery()

# def isOverlap(i1, i2):
#     if i1[1] >= i2[0] and i1[0] <= i2[1]:
#         return True
#     return False

# i1 = [5,7]
# i2 = [10,13]

# print(isOverlap(i1,i2))

# def test1():
#     cy = ['a','b']
#     print(list(enumerate(cy,2019)))

#     x = 202
#     def myfunc():
#         #global x 
#         x = 404

#     myfunc()
#     print(x)

# def test2():
#     x = {"foo":"bar"}
#     y = {"baz":x}
#     z = y['baz']['foo']
#     print("z:", z)

# def test3():
#     pass

# # test1()
# # test2()
# #test3()


# def findGCD(n1, n2):
#     while n2 != 0:
#         tmp = n1
#         n1 = n2
#         n2 = tmp%n2
#     return n1


# # def findCDInArr(arr):
# #     d = float('inf')
# #     for i in range(len(arr)-1):
# #         for j in range(i+1, len(arr)):
# #             n1 = arr[i]
# #             n2 = arr[j]
# #             gcd = findGCD(n1, n2)
# #             print("n1:{}, n2:{}, gcd: {}".format(n1, n2, gcd))
# #             if 1 < gcd < d:
# #                 d = gcd
# #     #print("d: ", d)
# #     return d


# def findCDInArr(arr):
#     d = float('inf')
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             n1 = arr[i]
#             n2 = arr[j]
#             gcd = findGCD(n1, n2)
#             print("n1:{}, n2:{}, gcd: {}".format(n1, n2, gcd))
#             if gcd == 1:
#                 return 1
#             elif 1 < gcd < d:
#                 d = gcd
#     return d

# #a = findGCD(45,10)
# #print("a: ", a)

# b = findCDInArr([40,10,25,36,55,75])
# print("b: ", b)


# def isValidSudoku(puzzle):
#     # check rows
#     allRowsValid = True
#     for i,row in enumerate(puzzle):
#         cd = findCDInArr(row)
#         if cd == 1:
#             return False

#     # check cols
#     for x in range(len(puzzle[0])):
#         currCol = []
#         for y in range(len(puzzle)):
#             currCol.append(puzzle[y][x])
        
#         cd = findCDInArr(currCol)
#         if cd == 1:
#             return False
    
#     return True

# # If this returns 1, then you know there is not a common divisor > 1
# def findCDInArr(arr):
#     d = float('inf')
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             n1 = arr[i]
#             n2 = arr[j]
#             gcd = findGCD(n1, n2)
#             if gcd == 1:
#                 return 1
#             elif 1 < gcd and gcd < d:
#                 d = gcd
#     #print("d: ", d)
#     return d

# def findGCD(n1, n2):
#     while n2 != 0:
#         tmp = n1
#         n1 = n2
#         n2 = tmp%n2
#     return n1
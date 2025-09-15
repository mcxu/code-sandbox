root = {
    "A": {
        "alpha": {
            "hello": 12,
            "goodbye": 35,
            "whatever": 45
        }
    },
    "B": {
        "nodeA": 70,
        "nodeB": {
            "gateA": 30,
            "gateB": 50
        }
    },
    "C": 10
}

def getSum(root):
    #print("root: ", root)
    
    if not isinstance(root, dict):
        return root

    currSum = 0
    for k in root.keys():
        #print("key: ", k)
        child = root[k]
        if isinstance(child, dict):
            currSum += getSum(child)
        else:
            currSum += child
    
    return currSum
    
# totSize = getSum(root)
# print("totSize: ", totSize)

def searchRoot(root, currPath, targetPath, targetNode):
    # print(f"root:{root}, currPath:{currPath}, targetPath:{targetPath}")
    if currPath == targetPath:
        targetNode[0] = root
        return
    
    for k in root.keys():
        childNode = root[k]
        updatedPath = currPath + "." + k
        if updatedPath == targetPath:
            targetNode[0] = childNode # childNode is number, not dict
            return
        elif isinstance(childNode, dict):
            searchRoot(childNode, updatedPath, targetPath, targetNode)
    return

def searchRoot_v2(root, targetPathList):
    if not targetPathList:
        return root

    currentFolder = targetPathList.pop(0)

    if currentFolder in root.keys():
        childNode = root[currentFolder]
        return searchRoot_v2(childNode, targetPathList)
    return None

def test_searchRoot():
    print("root: ", root)
    currPath = ""
    targetNode = [None]
    
    targetPath = ".A.alpha" # {'hello': 12, 'goodbye': 35, 'whatever': 45}
    #targetPath = ".B.nodeB" # {'gateA': 30, 'gateB': 50}
    #targetPath = ".B.nodeA" # 70
    #targetPath = ".C" # 10
    #targetPath = ".A.beta" # None
    #targetPath = ".Z" # None

    searchedNode = None
    SEARCH_SELECTOR = 1

    if SEARCH_SELECTOR == 0:
        searchRoot(root, currPath, targetPath, targetNode)
        print("targetNode: ", targetNode)
        searchedNode = targetNode[0]
    elif SEARCH_SELECTOR == 1:
        targetPathList = targetPath.split(".")[1:]
        print("targetPathList: ", targetPathList)
        searchedNode = searchRoot_v2(root, targetPathList)
        print("searchedNode from v2: ", searchedNode)

    searchedNodeSize = getSum(searchedNode)
    print("sum of searchedNode: ", searchedNodeSize)

test_searchRoot()


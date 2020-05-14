'''
A.py
import B,C,D

B.py
import C,D

C.py
import D

D.py
no imports
'''

files = ["A", "B", "C", "D"]
fileToImportMap = {
    files[0]: ["B", "C", "D"],
    files[1]: ["C", "D"],
    files[2]: ["D"],
    files[3]: []
}
ext = ".py"

# get dependencies
def getDepsForFile(fileName):    
    # if fileName[-len(ext):] != ext:
    #     fileName += ext
    deps = fileToImportMap[fileName]
    return deps

def orderOfImports(fileList):
    order = []
    stack = [fileList[0]]
    
    # init this map to keep track of what's already been imported
    alreadyImported = {}
    for f in fileList:
        alreadyImported[f] = False
    print("alreadyImported: ", alreadyImported)

    while stack:
        print("-----")
        print("stack: ", stack)
        currFile = stack[-1]
        print("currFile: ", currFile)

        
            
        print("alreadyImported: ", alreadyImported)
        print("stack end: ", stack)
        print("order: ", order)

def testGetDepsForFile():
    files = ["A.py", "B.py", "C.py", "D.py"]
    filesNoExt = ["A","B","C","D"]
    for i in range(len(files)):
        f = files[i]
        deps = getDepsForFile(f)
        print("deps: ", deps)
    
    for i in range(len(filesNoExt)):
        f = filesNoExt[i]
        deps = getDepsForFile(f)
        print("deps: ", deps)

def test1():
    result = orderOfImports(files)
    print("result: ", result)

#testGetDepsForFile()
test1()
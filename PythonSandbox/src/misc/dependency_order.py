'''
Given files and their dependencies. Return list of imports so that
each file has their dependencies imported before the file itself is imported.
File: A: import B,C,D
File: B: import C,D
File: C: import D
File: D: no imports
'''

class DepOrder:
    def getDepOrder(self, importsMap):
        stack = [] # stores the order of files, and gets returned
        visited = set() # keep track of visited files
        files = list(importsMap.keys())
        for i in range(len(importsMap)):
            initFile = files[i]
            print("initFile: ", initFile)
            if initFile not in visited:
                self.depOrderToposort(importsMap, initFile, visited, stack)
        return stack

    def depOrderToposort(self, importsMap, currFile, visited, stack):
        visited.add(currFile)
        print("visited:", visited)
        for _,depFile in enumerate(importsMap[currFile]):
            if depFile not in visited:
                self.depOrderToposort(importsMap, depFile, visited, stack)
        stack.append(currFile)

    def importsMap1(self):
        importsMap = {
            "A": ["B", "C", "D"],
            "B": ["C", "D"],
            "C": ["D"],
            "D": []
        }
        return importsMap

    def test1(self):
        im = self.importsMap1()
        result = self.getDepOrder(im)
        print("result: ", result)

do = DepOrder()
do.test1()
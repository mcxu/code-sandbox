from typing import Dict, List, Tuple

class TimeMap:

    def __init__(self):
        self.keyToTsV: Dict[str, List[Tuple[int, str]]] = {} # key -> (ts, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        print("[set init] keyToTsV: ", self.keyToTsV)
        if key in self.keyToTsV:
           self.keyToTsV[key].append((timestamp, value))
        else:
           self.keyToTsV[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        print("[get init] keyToTsV: ", self.keyToTsV)
        if key in self.keyToTsV:
            tsValTups = self.keyToTsV[key]
            lowestTsValTup = tsValTups[0]
            if timestamp < lowestTsValTup[0]:
                return ""
            
            lo = 0
            hi = len(tsValTups)
            while lo < hi:
                mid = (lo+hi)//2
                midTup = tsValTups[mid]
                if midTup[0] <= timestamp:
                    lo = mid + 1
                else:
                    hi = mid
            
            print(f"lo: {lo}, hi: {hi}")
            return tsValTups[lo-1][1]

        return ""

def test1():
    # Your TimeMap object will be instantiated and called as such:
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    g1 = obj.get("foo", 1)
    print("g1: ", g1)
    g2 = obj.get("foo", 3)
    print("g2: ", g2)
    obj.set("foo", "bar2", 4)
    g3 = obj.get("foo", 4)
    print("g3", g3)
    g4 = obj.get("foo", 5)
    print("g4", g4)

def test2():
    input = {
        "fn": ["TimeMap","set","set","get","get","get","get","get"],
        "vals": [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
    }
    runTest(input)

def test3():
    input = {
        "fn": ["TimeMap","set","set","set","get"],
        "vals": [[],["assem","fat",20],["assem","thin",40],["hamza","thin",41],["hamza",20]]
    }
    runTest(input)

def runTest(input):
    obj = TimeMap()

    outputs = [None]
    for i in range(1, len(input["fn"])):
        print("============== i=", i)
        inputFn = input["fn"][i]
        print("inputFn: ", inputFn)
        inputVals = input["vals"][i]
        print("inputVals: ", inputVals)
        outputVal = None
        if inputFn == "set":
            obj.set(*inputVals)
        elif inputFn == "get":
            gottenVal = obj.get(*inputVals)
            print("gotten value: ", gottenVal)
            outputVal = gottenVal
        outputs.append(outputVal)
        print("[AFTER] keyToTsV: ", obj.keyToTsV)

    print("outputs: ", outputs)

if __name__=="__main__":
    # test1()
    test2()
    # test3()
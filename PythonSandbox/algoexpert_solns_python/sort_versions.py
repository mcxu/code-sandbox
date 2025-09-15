'''
Given version numbers:
versions = ['0.2.0', '3.1.2', '0.1.6', '5.0.0'];
output = ['5.0.0', '3.1.2', '0.2.0', '0.1.6'];
'''
import functools

def compareVersions(vList1, vList2):
    minLen = min(len(vList1), len(vList2))
    for i in range(minLen):
        n1 = int(vList1[i])
        n2 = int(vList2[i])
        if n1 > n2:
           return -1
        elif n1 < n2:
            return 1
    
    if len(vList1) < len(vList2):
        return 1
    return -1

def sortVersions(unsortedVersions):
    vSplits = [v.split(".") for v in unsortedVersions]
    print("vSplits: ", vSplits)
    sortedVersions = sorted(vSplits, key=
        functools.cmp_to_key(compareVersions)) 
    print("sortedVersions: ", sortedVersions)
    for i in range(len(sortedVersions)):
        sortedVersions[i] = ".".join(sortedVersions[i])
    return sortedVersions

def test1():
    versions = ['0.2.0', '3.1.2', '0.1.6', '5.0.0']
    output = ['5.0.0', '3.1.2', '0.2.0', '0.1.6']
    res = sortVersions(versions)
    print("res: ", res)
    if res==output:
        print('test1 pass')
    else:
        print('test1 fail')
test1()

def test2():
    versions = [
    '1.3.0.9',
    '0.2.0',
    '3.1.2',
    '0.1.6',
    '5.0.0',
    '3.3.3.3',
    '3.3.3.3.3',
    '3.10',
    '0.2.0',
    ]

    output = [
    '5.0.0',
    '3.10',
    '3.3.3.3.3',
    '3.3.3.3',
    '3.1.2',
    '1.3.0.9',
    '0.2.0',
    '0.2.0',
    '0.1.6',
    ]

    res = sortVersions(versions)
    print("res: ", res)   
    if res==output:
        print('test2 pass')
    else:
        print('test2 fail')
test2()
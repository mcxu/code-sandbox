import sys
# from os import path
# abspath = path.abspath(__file__)
# print("abspath: ", abspath)
# p1 = path.dirname(abspath)
# print("p1: ", p1)
# p2 = path.dirname(p1)
# print("p2: ", p2)
# sys.path.append(p2)
# print("syspath: ", sys.path)

import os
print ("cwd: ", os.getcwd())

from ..utils.number_utils import NumberUtils

def test1():
    a = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
    result = NumberUtils.isolateNegatives(a)
    print("test_isolateNegatives:", result)

test1()

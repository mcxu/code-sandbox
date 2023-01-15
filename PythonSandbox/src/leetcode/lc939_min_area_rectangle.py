# https://leetcode.com/problems/minimum-area-rectangle/

class Solution:
    def minAreaRect(self, points: [[int]]) -> int:
        colMap = {}
        for p in points:
            x=p[0]; y=p[1]
            if x in colMap.keys():
                colMap[x].append(y)
            else:
                colMap[x] = [y]
        print("colMap: ", colMap)
        minArea = float('inf')
        lastx = {}
        for x in sorted(colMap.keys()):
            yvals = colMap[x]
            yvals.sort()
            print("-- x:{}, yvals:{}".format(x,yvals))
            for j,y2 in enumerate(yvals):
                for i in range(j):
                    y1 = yvals[i]
                    print("y1:{}, y2:{}, lastx: {}".format(y1, y2, lastx))
                    if (y1, y2) in lastx:
                        currArea = (x-lastx[(y1,y2)]) * (y2-y1)
                        print("currArea: ", currArea)
                        minArea = min(minArea, currArea)
                        print('minArea updated: ', minArea)
                    lastx[(y1,y2)] = x
                    print("lastx updated: ", lastx)
        if minArea==float('inf'):
            return 0
        return minArea
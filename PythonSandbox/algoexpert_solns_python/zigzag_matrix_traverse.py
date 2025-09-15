'''
Zigzag Matrix Traverse

Given nxn matrix, return list of values in a zigzag pattern
where 1st value starts at top-left, then down, then diagonal up, ...

Sample input: 
[[1,3,4,10],
 [2,5,9,11],
 [6,8,12,15],
 [7,13,14,16]]
Sample output: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
'''

class Prob:
    
    """
    This works for generalized matrix dimensions (n rows x m columns)
    Time complexity: O(n*m), where n,m are dimensions of the matrix.
    Space complexity: O(n*m), need to store n*m traversed values.
    """
    @staticmethod
    def zigzagTraverse(array):
        traversed = []
        i = 0 # not needed, just to count
        y = 0
        x = 0
        direction = False # True = going right up, False = going left down
        while 0 <= y < len(array) and 0 <= x < len(array[0]):
            currVal = array[y][x]
            print("i: {}, y: {}, x: {}, currVal: {}, direction: {}".format(i, y, x, currVal, direction))
            traversed.append(currVal)
            
            if direction==True:
                if y > 0 and x < len(array[0])-1:
                    print("A")
                    y = y-1 # up 
                    x = x+1 # right
                elif y == 0:
                    print("B")
                    x = x+1
                    direction = False
                elif x == len(array[0])-1:
                    print("C")
                    y = y+1
                    direction = False
            else:
                if x > 0 and y < len(array)-1:
                    print("D")
                    x = x-1 # left
                    y = y+1 # down
                elif x == 0:
                    print("E")
                    y = y+1
                    direction = True
                elif y == len(array)-1:
                    print("F")
                    x = x+1
                    direction = True
            
            # reverse direction when the largest diagonal (1/2 of matrix) is covered
            if x > len(array[0])-1:
                print("G")
                x -= 1
                y += 1
                direction = False
            elif y > len(array)-1:
                print("H")
                y -= 1
                x += 1
                direction = True
            
            i+=1
            
        print("traversed: ", traversed)
        return traversed
            
    @staticmethod
    def test1():
#         array = [[1]]
#         array = [[1,2,3,4,5]]
#         array = [1, 3, 4, 7, 8], [2, 5, 6, 9, 10]
#         array = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 10]]
#         array= [[1,3],[2,4]]
#         array = [[1,3,4,10],
#                  [2,5,9,11],
#                  [6,8,12,15],
#                  [7,13,14,16]]
        array = [[1, 3, 4, 10, 11], 
                 [2, 5, 9, 12, 19], 
                 [6, 8, 13, 18, 20], 
                 [7, 14, 17, 21, 24], 
                 [15, 16, 22, 23, 25]]

        Prob.zigzagTraverse(array)
        
    
Prob.test1()
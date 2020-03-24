
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Prob:
    # construct tree using array
    @staticmethod
    def btFromArray(arr, i, root):
        if i < len(arr):
            if i < 0 or arr[i] == -1:
                return root
            newNode = Node(arr[i])
            root = newNode
            root.left = Prob.btFromArray(arr, i*2+1, root.left)
            root.right = Prob.btFromArray(arr, i*2+2, root.right)
        return root
    
    @staticmethod
    def treeSum(root):
        if root == None:
            return 0
        ls = Prob.treeSum(root.left)
        rs = Prob.treeSum(root.right)
        return root.val + ls + rs
    
    @staticmethod
    def getLargestBranch(arr):
        if not arr:
            return ""
        if len(arr) == 1:
            return ""
        
        # construct tree from array
        root = Prob.btFromArray(arr, 0, None)
        print("root: ", root.val)
        tmp = root
        #print("A: ", tmp.right.left.val)
        lbs = Prob.treeSum(tmp.left)
        rbs = Prob.treeSum(tmp.right)
        print("lbs: {}, rbs: {}".format(lbs, rbs))
        
        if lbs == rbs:
            return ""
        elif lbs > rbs:
            return "Left"
        else:
            return "Right"
    
def main():
    testArr = [3,6,2,9,-1,10]
    Prob.getLargestBranch(testArr)
    
main()

    
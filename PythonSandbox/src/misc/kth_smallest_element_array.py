'''
Find kth smallest/largest element in unsorted array

Sample input: [7, 10, 4, 3, 20, 15], k=3, find kth smallest
Sample output: 7

Sample input: [7, 10, 4, 3, 20, 15], k=4, find kth smallest
Sample output: 10

https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
'''

class Prob:
    '''
    smallest = True means kths smallest, if smallest = False, then kth largest
    '''
    @staticmethod
    def kthSmLg(array, k, smallest=True):
        # O(m) time, O(m) space, where m = max(array)
        aux = [None for _ in range(max(array)+1)] 
        
        # O(n) time
        for i in range(len(array)):
            val = array[i]
            if aux[val] != None:
                aux[val] += 1
            else:
                aux[val] = 1
        print("aux filled: ", aux)
        
        c = 0 
        i = 0
        if smallest == True:
            while c < k: # O(m) time
                if aux[i] != None:
                    c += aux[i]
                i += 1
            return i-1
        
        else:
            i = len(aux)-1
            while c < k: # O(m) time
                if aux[i] != None:
                    c += aux[i]
                i -= 1
            return i+1
 
    @staticmethod
    def test1():
        array = [7, 10, 4, 3, 20, 15]
        k = 3
        ans = Prob.kthSmLg(array, k, smallest=True)
        print("test1 ans: ", ans)

    @staticmethod
    def test2():
        array = [7, 10, 7, 3, 20, 15]
        k = 6
        ans = Prob.kthSmLg(array, k, smallest=False)
        print("test1 ans: ", ans)

#Prob.test1()
Prob.test2()

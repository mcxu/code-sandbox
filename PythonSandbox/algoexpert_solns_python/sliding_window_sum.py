'''
Sliding windows sum.

Example: Given array:
arr=[4,6,3,8,2,5,6], k=3 (for sliding window size)
output: [13,17,13,15,13]
'''
class SWS:
    def slidingWindowSum(self, arr, k):
        if len(arr) < k:
            return []

        s = sum(arr[:k])
        out = [s]
        for i in range(k, len(arr)):
            s += (-arr[i-k] + arr[i])
            out.append(s)
        return out

    def test(self):
        #arr=[4,6,3,8,2,5,6] # [13,17,13,15,13]
        #arr = [4,6,3] # [13]
        arr = [4,6] # []
        k=3
        res = self.slidingWindowSum(arr,k)
        print("res: ", res)
    
    def slidingWindowProduct(self, arr, k):
        if len(arr) < k:
            return []
        
        p = 1
        pIfNot0 = p
        for n in arr[:k]:
            p *= n
            if n == 0:
                pIfNot0 *= 1
            else:
                pIfNot0 *= n
        print("p: {}, pIfNot0: {}".format(p, pIfNot0))
        out = [p]
        for i in range(k, len(arr)):
            if arr[i-k] == 0:
                p = pIfNot0
            else:
                p /= arr[i-k]
                pIfNot0 /= arr[i-k]
            
            if arr[i] == 0:
                p = 0
            else:
                p *= arr[i]
                pIfNot0 *= arr[i]
            print("i={}, p: {}, pIfNot0: {}".format(i, p, pIfNot0))
            out.append(p)
        return out

    def test2(self):
        #arr=[4,6,3,8,2,5,6]
        arr = [0,2,3,4,5,0,3,2,5,6]
        k = 3
        res = self.slidingWindowProduct(arr, k)
        print("res: ", res)


s = SWS()
#s.test()
s.test2()
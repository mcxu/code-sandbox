"""
This problem was recently asked by Google. [Easy]

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

class P1:
    l1 = [10, 15, 3, 7]
    l2 = [10, 5, 15, 3, 2, 7, 4, 6, 5, 1, 8]
    
    def __init__(self):
        self.output_dict = {
            "valid" : False,  #False: no 2 numbers add up to k.
            "result" : []
        }
        

    # result will be list of lists
    def eval(self, given_list, k):
        if(given_list == None):
            return self.output_dict
        
        for i in range(len(given_list)):
            ival = given_list[i]
            print("i = {}".format(ival))
            for j in range(i+1, len(given_list)):
                jval = given_list[j]
                print("\tj = {}".format(jval))
                if(ival + jval == k):
                    if self.output_dict["valid"] == False: 
                        self.output_dict["valid"] = True
                    self.output_dict["result"].append([ival,jval])

        return self.output_dict
    
    
    def eval_single_pass(self, given_list, k):
        if(given_list == None):
            return False
        
        out_set = set({})
        
        for i in range(len(given_list)):
            diff = k - given_list[i]
            if diff in out_set:
                return True
            out_set.add(given_list[i])
        return False
        

    def test1(self):
        test1 = self.eval(P1.l1, 17) 
        print("test1: {}".format(test1))
    
    def test2(self):
        test2 = self.eval(P1.l2, 10) 
        print("test2: {}".format(test2))
        
    def test3(self):
        test3 = self.eval([], 10)
        print("test3: {}".format(test3))
    
    def test4(self):
        test4 = self.eval_single_pass(P1.l1, 17)
        print("test4: {}".format(test4))
        
        test4 = self.eval_single_pass(P1.l1, 10)
        print("test4.1: {}".format(test4))
        
def main():
    p1 = P1()
#     p1.test1()
#     p1.test2()
#     p1.test3()
    p1.test4()
    
if __name__ == "__main__":
    main()
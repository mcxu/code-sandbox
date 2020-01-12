"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""

class FB:
    @staticmethod
    def fizzBuzz1():
        for i in range(1,101,1):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    
    @staticmethod
    def fizzBuzz2():
        for i in range(1, 101, 1):
            msg = ""
            if i % 3 == 0:
                msg += "Fizz"
            
            if i % 5 == 0:
                msg += "Buzz"
            
            if not msg:
                print(i)
            else:
                print(msg)

#FB.fizzBuzz1()
FB.fizzBuzz2()
#!/usr/bin/python3

#Este codigo fue recuperado de:
#https://www.geeksforgeeks.org/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python/

class eval_equations:
    # Single constructor to call other methods
    def __init__(self, *inp):

        # When 2 arguments are passed
        if len(inp) == 2:
            self.ans = self.eq2(inp)

        # When 3 arguments are passed 
        elif len(inp) == 3:
            self.ans = self.eq1(inp)

        # When more than 3 arguments are passed
        else:
            self.ans = self.eq3(inp)

    def eq1(self, args):
        x = (args[0]*args[0])+(args[1]*args[1])-args[2]
        return x

    def eq2(self, args):
        y = (args[0]*args[0])-(args[1]*args[1])
        return y

    def eq3(self, args):
        temp = 0
        for i in range(0, len(args)):
            temp += args[i]*args[i]
        
        temp = temp/max(args)
        z = temp
        return z

inp1 = eval_equations(1, 2)
inp2 = eval_equations(1, 2, 3)
inp3 = eval_equations(1, 2, 3, 4, 5)

print("equation 2: ", inp1.ans)
print("equation 1: ", inp2.ans)
print("equation 3: ", inp3.ans)

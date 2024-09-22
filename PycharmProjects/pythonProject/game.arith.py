import random
operators =["+","-","*","/"]

class problem:
    def __init__(self):
             self.ans = None
    def generate_problem(self):
        symbol = random.choice(operators)
        left = random.randint(1,30)
        right = random.randint(1,30)
        expr = str(left) +" "+ symbol+" " + str(right)
        self.ans = eval(expr)
        answer = float(input(f" what is {left} {symbol} {right} = "))
        if answer == self.ans:
           print(" you have won!")
        else:
           print(f" you got it wrong!{self.ans}")



problem =problem()

problem.generate_problem()

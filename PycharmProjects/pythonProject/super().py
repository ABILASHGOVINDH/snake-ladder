class Fact:
    def __init__(self):
        pass
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Fact.factorial(n - 1)
    @staticmethod
    def sum_of_factorial(num):
        if num==0 :
            return 0
        elif num ==1:
            return 1
        else:
            return Fact.factorial(num % 10) +  Fact.sum_of_factorial(num // 10)
class refact(Fact):
    def __init__(self):
        super().__init__()
        self.limit = int(input("enter your number for range of   calculation: "))
        self.strongest = self.find_strongest()

    def find_strongest(self):
        strongest =[]
        for num in range(1,self.limit):
            if num == self.sum_of_factorial(num):
                strongest.append(num)
        return strongest
    def __call__(self):
       return self.find_strongest()

my_class = refact()
print(my_class.strongest)
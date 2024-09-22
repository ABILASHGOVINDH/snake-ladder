from  fractions import Fraction

expression = "-1/2+1/2"
fraction = expression.replace('-','+-').split('+')
result = sum(Fraction(frac) for frac in fraction if frac)

print(f'{result.numerator}/{result.denominator}')

fraction1 = Fraction(numerator=-1,denominator=2)
fraction2 = Fraction(numerator=1,denominator=2)
fraction = fraction1+fraction2
print(fraction.numerator,fraction.denominator)

# expression = [1/3-1/2]
#
# aver = sum(expression)/len(expression)
# aver_frac = Fraction(aver).limit_denominator()
# print(f'{aver_frac.numerator}/{aver_frac.denominator}')
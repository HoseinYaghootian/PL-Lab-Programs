#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Fraction:
    def __init__(self, numer, denomin):
        self.numer = numer
        self.denomin = denomin
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Calc(Fraction):

    def __init__(self, result):
        self.result = result

    def sum(self, frac1, frac2):
        self.result.numer = (frac1.numer * frac2.denomin) + (frac2.numer *
                                                             frac1.denomin)
        self.result.denomin = frac1.denomin * frac2.denomin
        return self

    def sub(self, frac1, frac2):
        self.result.numer = (frac1.numer * frac2.denomin) - (frac2.numer *
                                                             frac1.denomin)
        self.result.denomin = frac1.denomin * frac2.denomin
        return self

    def mul(self, frac1, frac2):
        self.result.numer = frac1.numer * frac2.numer
        self.result.denomin = frac1.denomin * frac2.denomin
        return self

    def div(self, frac1, frac2):
        self.result.numer = frac1.numer * frac2.denomin
        self.result.denomin = frac1.denomin * frac2.numer
        return self

    def simplification(self):
        while (True):
            if self.result.numer % 2 == 0 and self.result.denomin % 2 == 0:
                self.result.numer //= 2
                self.result.denomin //= 2
                return self

            elif self.result.numer % 3 == 0 and self.result.denomin % 3 == 0:
                self.result.numer //= 3
                self.result.denomin //= 3
                return self

            elif self.result.numer % 5 == 0 and self.result.denomin % 5 == 0:
                self.result.numer //= 5
                self.result.denomin //= 5
                return self

            elif self.result.numer % 7 == 0 and self.result.denomin % 7 == 0:
                self.result.numer //= 7
                self.result.denomin //= 7
                return self

            else:
                return self

    def show(self):
        print(f"result: {self.result.numer}/{self.result.denomin}")
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
numer1 = int(input('enter your numer1: '))
denomin1 = int(input('enter  your denomin1: '))
numer2 = int(input('enter your numer2: '))
denomin2 = int(input('enter your denomin2: '))
print(f"number 1 is {numer1}/{denomin1} & number 2 is {numer2}/{denomin2}")
frac1 = Fraction(numer1, denomin1)
frac2 = Fraction(numer2, denomin2)
result = Fraction(1, 1)

calc = Calc(result)

while True:
    #- - - - - - - - - - - - - - - - - - - - - -
    is_correct_op = 0
    while is_correct_op == 0:
        op = input("""
- - - - - - - - - - -
Enter a number to select a function:
0:exit
1: +  
2: -
3: *
4: /
- - - - - - - - - - -
""")
        is_correct_op = 1
        if not ("0" <= op <= "4" or op == "+" or op == "-" or op == "*"
                or op == "/"):
            is_correct_op = 0
            print("---------Enter valid string!---------")
    #- - - - - - - - - - - - - - - - - - - - - -
    if op == "0" or op == "exit":
        quit()

    elif op == "1" or op == "+":
        result = calc.sum(frac1, frac2)

    elif op == "2" or op == "-":
        result = calc.sub(frac1, frac2)

    elif op == "3" or op == "*":
        result = calc.mul(frac1, frac2)

    elif op == "4" or op == "/":
        result = calc.div(frac1, frac2)

    result.simplification().show()

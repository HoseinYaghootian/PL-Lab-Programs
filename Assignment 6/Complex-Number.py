#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Complex:

    def __init__(self, real, image):
        self.r = real
        self.i = image


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class Calc:

    def __init__(self, result):
        self.result = result

    def sum(self, comp1, comp2):
        self.result.r = comp1.r + comp2.r
        self.result.i = comp1.i + comp2.i
        return self

    def sub(self, comp1, comp2):
        self.result.r = comp1.r - comp2.r
        self.result.i = comp1.i - comp2.i
        return self

    def mul(self, comp1, comp2):
        self.result.r = comp1.r * comp2.r - comp1.i * comp2.i
        self.result.i = comp1.r * comp2.i + comp1.i * comp2.r
        return self

    def show(self):
        print(f"{self.result.r}+{self.result.i}i")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
real1 = int(input('enter your Complex number1 real: '))
image1 = int(input('enter  your Complex number2 image: '))
real2 = int(input('enter your Complex number2 real: '))
image2 = int(input('enter your Complex number2 image: '))
print(f"number 1 is {real1}+{image1}i & number 2 is {real2}+{image2}i")
comp1 = Complex(real1, image1)
comp2 = Complex(real2, image2)
result = Complex(1, 1)

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
- - - - - - - - - - -
""")
        is_correct_op = 1
        if not ("0" <= op <= "3" or op == "+" or op == "-" or op == "*"):
            is_correct_op = 0
            print("---------Enter valid string!---------")
    #- - - - - - - - - - - - - - - - - - - - - -
    if op == "0" or op == "exit":
        quit()

    elif op == "1" or op == "+":
        result = calc.sum(comp1, comp2)

    elif op == "2" or op == "-":
        result = calc.sub(comp1, comp2)

    elif op == "3" or op == "*":
        result = calc.mul(comp1, comp2)

    calc.show()
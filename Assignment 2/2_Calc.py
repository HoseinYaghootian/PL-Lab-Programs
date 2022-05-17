import math

while True:
    is_correct_op = 0
    while is_correct_op == 0:
        op = input(
"""
- - - - - - - - - - -
Enter a number to select a function:
0:exit

1: +  
2: -
3: *
4: /
5: %
6: ^

7: sin
8: cos
9: tan
10: cot
11: log
12: !
- - - - - - - - - - -
""" 
        )

        if op=="0" or op=="exit":
            quit()

        print("\n")

        is_correct_op = 1

        if not(1<=int(op)<=12 or op=="+" or op=="-" or op=="*" or op=="/" or op=="%" or op=="^" or op=="sin" or op=="cos" or op=="tan" or op=="cot" or op=="log" or op=="!"):
            is_correct_op = 0
            print("---------Enter valid string!---------")

        
    num_1 = int(input("Enter number: "))
    if 1<=int(op)<=6 or op=="+" or op=="-" or op=="*" or op=="/" or op=="%" or op=="^":
        num_2 = int(input("Enter number: "))


    if op=="1" or op=="+" :
        result = num_1 + num_2

    elif op=="2" or op=="-" :
        result = num_1 - num_2

    elif op=="3" or op=="*" :
        result = num_1 * num_2

    elif op=="4" or op=="/" :
        result = num_1 / num_2

    elif op=="5" or op=="%" :
        result = num_1 % num_2

    elif op=="6" or op=="^" :
        result = num_1 ** num_2


    elif op=="7" or op=="sin" :
        result = math.sin(num_1)

    elif op=="8" or op=="cos" :
        result = math.cos(num_1)

    elif op=="9" or op=="tan" :
        result = math.tan(num_1)

    elif op=="10" or op=="cot" :
        result = math.cot(num_1)

    elif op=="11" or op=="log" :
        result = math.log10(num_1) 

    elif op=="12" or op=="!" :
        result = math.factorial(num_1)
    

    print(result)

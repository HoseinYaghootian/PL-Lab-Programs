import random
numbers= []

i = 0
length = int(input("Please enter your length: "))

start = 0
end = start + length + 100 #auto debug :)

while i < length:
    number = random.randint(start, end)
    if number not in numbers:
        numbers.append(number)
        i += 1
print(numbers)

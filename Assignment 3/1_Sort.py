numbers = []
r = int(input("Please enter your numbers range: "))
for i in range (r):
    number = int(input(f"Please enter your {i+1} number: "))
    numbers.append(number)
    if numbers != numbers.sort():
        numbers.sort()
print(numbers)
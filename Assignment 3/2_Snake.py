length = int(input("Please enter the length of your snake: "))
i = 0
while i < length:
    if i%2 == 0:
        print("🟩", end ="")
    else:
        print("🟨", end ="")
    i += 1
print("-")
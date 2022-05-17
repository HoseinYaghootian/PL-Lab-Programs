weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

print(f"BMI is {round(weight / (height**2), 2)}")
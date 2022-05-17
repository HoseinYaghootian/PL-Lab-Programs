def Ave(x): 
    avg = sum(x) / len(x) 
    return avg
  
scores = []

i = 0 
while i < 3:
    scores.append(float(input(f'Enter your {i+1} number: ')))
    i+= 1

avg = Ave(scores)  
print(f"Average of scores is {round(avg, 2)}")
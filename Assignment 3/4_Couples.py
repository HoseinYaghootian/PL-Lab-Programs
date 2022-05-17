import random

boys = ["ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"]
girls = ["sara", "zari", "neda", "homa", "eli", "goli", "mary"]
couples = []
singles = []

i = 0
boysNumber = len(boys)
girlsNumber = len(girls)
isBoysSingle = 0
if boysNumber>girlsNumber:
    length=girlsNumber
    isBoysSingle = 1
else:
    length=boysNumber
 
while i < length:
    boy = random.choice(boys)
    girl = random.choice(girls)
    boys.remove(boy)
    girls.remove(girl)

    couples.append((boy, girl)) #mobarak bashe :)
    i += 1
print (f"couples: {couples}" )

if isBoysSingle:
    singles = boys
else:
    singles = girls
print (f"singles: {singles}")

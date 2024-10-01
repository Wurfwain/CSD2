#Hoe functies werken in de basis:

def rekensom(x):
    y = x + 3
    return y

for i in range(4):
    print(rekensom(i))


#Hetzelfde maar dan korter:

def rekensom(x):
    return x + 3

for i in range(4):
    print(rekensom(i))


#Nu met 2 argumenten:

def rekensom(x, y):
    return x + y

for i in range(4):
    print(rekensom(i, i))
number = int(input("Geben sie eine Zahl ein:"))

for (x) in range(1, number + 1):
    if x % 5 == 0 and x % 3 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

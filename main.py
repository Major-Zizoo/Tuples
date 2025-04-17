fruits=("apple","banana","cherry","apple","pineapple")

print("Fruits tuple:",fruits)

print("First fruit:",fruits[0])
print("Second fruit:",fruits[1])

print("Last fruit:",fruits[-1])

print("First two fruits:", fruits[0:2])

for x in fruits:
    print(x)

print("Apple count:", fruits.count("apple"))

print("Index of banana:",fruits.index("banana"))
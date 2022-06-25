rows   = int(input("Enter how many rows "))
columns = int(input("Enter how many columns "))
symbol = input("Enter a symbol ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
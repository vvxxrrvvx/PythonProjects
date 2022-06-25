def x(**zx):
    print("Hello", end=" ")
    for key,value in zx.items():
        print(value,end=" ")

x(dua="timotius",tiga="exavier",empat="taroreh")
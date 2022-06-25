#def v(*x):
    #hasil = 0
    #for i in x:
        #hasil += i
    #return hasil

def v(*i):
    hasil = 0
    i = list(i)
    i[0] = 0
    for i in i:
        hasil += i
    return hasil

print(v(5,5,7,7))
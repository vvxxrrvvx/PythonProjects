import os

sumber = "v"
tujuan = "C:\\Users\\user\\Desktop\\v"

try:
    if os.path.exists(tujuan):
        print("Sudah ada file tersebut di "+ str(tujuan))
    else:
        os.replace(sumber,tujuan)
        print(str(sumber) +" berhasil dipindahkan")

except FileNotFoundError:
    print(str(sumber)+" tidak ada")
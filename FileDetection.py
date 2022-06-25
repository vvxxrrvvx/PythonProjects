import os

path = "C:\\Users\\user\\Desktop\\New folder"

if os.path.exists(path):
    print("Lokasi file itu ada")
    if os.path.isfile(path):
        print("Itu adalah file")
    elif os.path.isdir(path):
        print("Itu adalah directory")
else:
    print("Lokasi file itu tidak ada")
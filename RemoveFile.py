import os
import shutil

file = "C:\\Users\\user\\vmlogs"

try:
    #os.rmdir(file)
    #shutil.rmtree(file)
except FileNotFoundError:
    print("file tidak ditemukan")
else:
    print(str(file)+" berhasil dihapus")
# exception

try:
    numerator = int(input("Masukkan bilangan yang ingin dibagi "))
    denominator = int(input("Masukkan bilangan yang ingin dibagi dengan "+ str(numerator) +" : "))
    hasil = numerator / denominator

except ZeroDivisionError as x:
    print(x)
    print("Kamu tidak bisa membagi "+ str(numerator) +" dengan 0")
except ValueError as x:
    print(x)
    print("Kamu hanya bisa membagi "+ str(numerator) +" dengan angka bukan huruf")
except Exception as x:
    print(x)
    print("Ada yang salah:(")
else:
    print(hasil)
finally:
    print("ini akan selalu di execute")
nama = input("Siapa nama kamu : ")
umur = int(input("Berapa umur kamu "+ str(nama) +"? "))
tinggi = float(input("Berapa tinggi badan kamu "+ str(nama) +"? "))

if umur >= 18 and tinggi >= 170.0:
    print("\nUmur dan tinggi kamu sesuai persyaratan")
    print("Kamu boleh mendaftar!")
elif umur >= 18 and tinggi < 170.0:
    print("\nUmur kamu sudah mencukupi untuk mendaftar "+ str(nama))
    print("Tetapi maaf tinggi kamu hanya "+ str(tinggi) +"cm")
    print("Coba lagi ya tahun depan:)")
elif umur <= 12:
    print("\nMaaf "+ str(nama) +" kamu dilarang untuk mendaftar")
    print("Kamu masih anak-anak")
    print("Kamu baru berumur "+ str(umur) +" tahun!")
elif umur < 17 and tinggi < 170.0:
    print("\nUmur dan tinggi badan kamu belum mencukupi persyaratan")
    print("tinggi kamu adalah "+ str(tinggi) +"cm")
    print("umur kamu adalah " + str(umur) +" tahun")
    print("Kamu masih remaja")
else:
    print("\nTinggi kamu sudah mencukupi untuk mendaftar "+ str(nama))
    print("Tetapi umur kamu masih "+ str(umur) +" tahun")
    print("Kamu masih remaja!")
    print("Jika umur kamu lebih dari atau sama dengan 18 (>=18) tahun, kamu baru boleh mendaftar")

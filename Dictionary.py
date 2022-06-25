ibu_kota = {"USA":"Washington Dc",
            "Jepang":"Tokyo",
            "India":"New Delhi",
            "Russia":"Moskow",
            "China":"Beijing"}

ibu_kota.update({"Indonesia":"Jakarta"})
#ibu_kota.pop("China")

#print(ibu_kota.get("Indonesia"))
#print(ibu_kota.keys())
#print(ibu_kota.values())
#print(ibu_kota.items())

for key,value in ibu_kota.items():
    print(key,value)
nama = "exavier"  # GLOBAL SCOPE

def display_nama():
    nama = "taroreh"
    print(nama)   # LOCAL SCOPE


print(nama)
display_nama()

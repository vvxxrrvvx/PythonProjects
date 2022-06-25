import random

x = random.randint(1,10)
y = random.random()

daftar = ['kertas','batu','gunting']
z = random.choices(daftar)

kartu = [1,2,3,4,5,6,7,8,9,10,'j','as','king','queen']
random.shuffle(kartu)

print(z)
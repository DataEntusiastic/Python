"""
    Perulangan while disebut sebagai uncounted loop, atau perulangan yang tak terhitung, hal ini dikarenakan 
    perulangan while digunakan pada perulangan yang mempunyai syarat dan tidak tahu berapa banyak perulangannya.

"""

jawab = "ya"
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? :")
    if jawab == 'tidak':
        break

print("Total perulangan", hitung)

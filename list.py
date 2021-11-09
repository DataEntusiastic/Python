"""
    List merupakan struktur data untuk menyimpan data lebih dari satu, hal ini seperti array

"""
# list Kosong
uang = []

# list string
warna = ["merah", "kuning", "Hijau", "kelabu", "biru"]

# list campuran
campur = ["hijau", 20, 2.0, True]
"""
    hijau merupakan tipe data string,
    20 bertipe integer,
    2.0 memiliki tipe data float, lalu
    True memiliki tipe data boolean

"""
# mengambil nilai dari list
print(warna[1])

# menampilkan semua isi dari list

print("Jumlah warna ada : ", len(warna))
print(warna)

""" 
    list bersifat mutable, yang artinya isi dari list dapat dirubah-rubah
    dengan cara memasukkan nomor indeks dari nilai yang akan dirubah

"""
# mengganti isi dari list
campur[2] = "pojok"
print(campur)

"""
    karena list bersifat mutable, isinya juga bisa ditambahkan dengan beberapa cara, yaitu:
    1. append : menambahkan nilai dari akhri isi list
    2. inset : menambahkan isi suatu list menggunakan nomor indeks
"""

# Append
warna.append("pink")
print(warna)

# insert
warna.insert(0, "orange")
print(warna)

# menghapus data dari list
"""
    untuk menghapus data dari list bisa menggunakan fungsi 'del' lalu diikuti dengan nama list dan indeks data yang ingin dihapus
"""
del warna[2]
print(warna)

"""
    slicing data pada list
    
"""

print("=" * 10)

angka = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# indeks positive = dimulai dari kiri dengan indeks 0
print(angka[1])

# indeks negative = dimulai dari kanan dengan indeks -1
print(angka[-1])

# slicing backward
print(angka[::-1])

# slicing menampilkan indeks genap
print(angka[::2])

"""
    list multi dimensi
"""

list_minuman = [["kopi", "susu", "teh"],
                ["jus apel", "jus jeruk", "jus sirsak"],
                ["es teh", "es jeruk", "es batu"]]

print(list_minuman[2][1])

# print semua isi dari list multidimensi dengan nested looping
for menu in list_minuman:
    for minuman in menu:
        print(minuman)

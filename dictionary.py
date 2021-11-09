"""
    Dictionary adalah struktur data yang bentuknya seperti kamus, ada kata kunci dan nilainya. kunci harus berbentuk uniqe dan isinya boleh duplikat.

"""

# Example

data = {
    "Nama": "Tri Susilo",
    "Umur": 21,
    "Hobi": ["membaca", "main game"],
    "Jenis Kelamin": "Laki-laki",
    "Sosmed": {
        "facebook": "Trisusilo/fb",
        "instagram": "trisusilo_17"
    },
    "Alamat": "Jl.Mancasan indah III, Condongcatur, Sleman, Yogyakarta"
}
# akses dictionary
print(data["Nama"])

# akses list pada dictionary
print(data["Hobi"][1])

# akses nested dictitonary
print(data["Sosmed"]["instagram"])

# Menggunakan perulangan
for key in data:
    print(data[key])

print("\n")

# Mengubah nilai dictionary
print(data["Hobi"])

data["Hobi"][1] = "Jalan-jalan"
print(data["Hobi"])

# menghapus nilai dictionary

tri = {
    "makanan": ["sate", "soto", "daging"],
    "minuman": ["es teh", "es Jeruk"],
    "hobi": "belajar"
}

# menggunakan del
del tri["hobi"]
print(tri)

# atau bisa menggunakan clear, bila ingin menghapus seluruh dictionary
# tri.clear()
# print(tri)

# menambahkan item ke dictionary

komik = {
    "judul": ["detektiv conan", "one piece", "Aphoteosis"],
    "penulis": ["asdf", "ddfe" "asdfe"]
}

print(komik["judul"])
print("\n")

komik.update({"tahun_terbit": "1990"})
print(komik)

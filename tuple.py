"""
    Tuple merupakan struktur data pada  python yang hampir sama dengan list, bedanya tuple bersifat immutable
    yang artinya isi dari tuple tidak bisa kita rubah maupun kita hapus. tuple dibuat dengan tanda kurung biasa ()

"""
# tuple integer
angka = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(angka[2])

# tuple kosong
kosong = ()

# tuple tanpa kurung

x = "biji", 1, "karung"

# singleton, pada saat membuat tuple yang hanya berisi satu data haru dikasih tanda kom ',' supaya tidak diangap sebagai string
s = ("a",)

print(x)
print(type(s))

# nested tuple

angka_1 = (1, 3, 5, 7, 9)
angka_2 = (2, 4, 6, 8, 10)
angka_3 = (angka_1, angka_2)  # nested tuple

print(angka_3)

for i in angka_3:
    for j in i:
        print(j)

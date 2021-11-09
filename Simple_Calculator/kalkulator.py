print("=" * 20)
print("Operasi Matematika")
print(" 1. Jumlah     [+]")
print(" 2. Kurang     [-]")
print(" 3. Kali       [x]")
print(" 4. Bagi       [/]")
print("=" * 20)

operasi = input("Pilih Operasi Matematika: ")
# saat mengkonversi dari string ke integer, bisa menggunakna function build in eval()
bilangan_1 = int(input("Masukkan Bilangan Pertama: "))
bilangan_2 = int(input("Masukkan Bilangan Kedua: "))
print("=" * 20)
print("\n")

if operasi == "1":
    print("Operasi Penjumlahan")
    hasil = bilangan_1 + bilangan_2
    print(f"Hasil penjumlahan {bilangan_1} + {bilangan_2} = {hasil}")
    print("\n")
elif operasi == "2":
    print("Operasi Pengurangan")
    hasil = bilangan_1 - bilangan_2
    print(f"Hasil pengurangan {bilangan_1} - {bilangan_2} = {hasil}")
    print("\n")
elif operasi == "3":
    print("Operasi Perkalian")
    hasil = bilangan_1 * bilangan_2
    print(f"Hasil perkalian {bilangan_1} * {bilangan_2} = {hasil}")
    print("\n")
elif operasi == "4":
    print("Operasi Pembagian")
    hasil = bilangan_1 / bilangan_2
    print(f"Hasil pembagian {bilangan_1} / {bilangan_2} = {hasil}")
    print("\n")
else:
    print("Operasi yang anda pilih tidak ada!!!")
    print("\n")

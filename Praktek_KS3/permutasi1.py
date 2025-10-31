import itertools

def permutasi_menyeluruh():
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    hasil = list(itertools.permutations(data))
    print("Permutasi Menyeluruh:")
    for p in hasil:
        print(p)

def permutasi_sebagian():
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    k = int(input("Masukkan jumlah elemen yang diambil (k): "))
    hasil = list(itertools.permutations(data, k))
    print(f"Permutasi Sebagian (k={k}):")
    for p in hasil:
        print(p)

def permutasi_keliling():
    data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
    pertama = data[0]
    hasil = list(itertools.permutations(data[1:]))
    print("Permutasi Keliling:")
    for p in hasil:
        print([pertama] + list(p))

# ====== MENU ======
print("=== PROGRAM PERMUTASI ===")
print("1. Permutasi Menyeluruh")
print("2. Permutasi Sebagian")
print("3. Permutasi Keliling")

pilih = input("Pilih jenis permutasi (1/2/3): ")

if pilih == "1":
    permutasi_menyeluruh()
elif pilih == "2":
    permutasi_sebagian()
elif pilih == "3":
    permutasi_keliling()
else:
    print("Pilihan tidak valid.")

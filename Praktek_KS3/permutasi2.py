import itertools

def atur_buku():
    n = int(input("Masukkan jumlah buku: "))
    r = int(input("Masukkan jumlah bagian rak: "))

    buku = [f"B{i+1}" for i in range(n)]
    rak = [f"Rak{i+1}" for i in range(r)]

    kombinasi = list(itertools.product(rak, buku))
    print(f"\nSemua kemungkinan penempatan {n} buku ke {r} bagian rak:")
    for penempatan in kombinasi:
        print(penempatan)

atur_buku()

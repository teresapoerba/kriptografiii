def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

hasil = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) adalah: {hasil}")

huruf = input("Masukkan inisial huruf objek (pisahkan dengan spasi): ").split()
from itertools import combinations

if len(huruf) >= n:
    print(f"\nSemua kombinasi huruf dari {r} huruf yang dipilih:")
    for c in combinations(huruf[:n], r):
        print(c)
else:
    print("Jumlah huruf tidak mencukupi.")

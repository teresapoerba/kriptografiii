# latihan3.py
# Konversi bilangan Hexadesimal ke Desimal, Biner, dan Oktal

print("=== Konversi Bilangan Hexadesimal ke Desimal, Biner, dan Oktal ===")

heksa = input("Masukkan bilangan hexadesimal: ")

try:
    desimal = int(heksa, 16)
    biner = bin(desimal)[2:]
    oktal = oct(desimal)[2:]
    print(f"Bilangan hexadesimal: {heksa}")
    print(f"Konversi ke desimal: {desimal}")
    print(f"Konversi ke biner: {biner}")
    print(f"Konversi ke oktal: {oktal}")
except ValueError:
    print("Input tidak valid! Gunakan angka 0-9 atau huruf A-F.")

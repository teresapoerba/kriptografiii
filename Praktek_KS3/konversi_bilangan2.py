# latihan2.py
# Konversi bilangan Oktal ke Desimal, Biner, dan Hexadesimal

print("=== Konversi Bilangan Oktal ke Desimal, Biner, dan Hexadesimal ===")

oktal = input("Masukkan bilangan oktal: ")

try:
    desimal = int(oktal, 8)
    biner = bin(desimal)[2:]
    heksa = hex(desimal).upper()[2:]
    print(f"Bilangan oktal: {oktal}")
    print(f"Konversi ke desimal: {desimal}")
    print(f"Konversi ke biner: {biner}")
    print(f"Konversi ke hexadesimal: {heksa}")
except ValueError:
    print("Input tidak valid! Masukkan hanya angka 0-7.")

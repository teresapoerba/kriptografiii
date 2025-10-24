# latihan1.py
# Konversi bilangan Biner ke Desimal dan Hexadesimal

print("=== Konversi Bilangan Biner ke Desimal dan Hexadesimal ===")

biner = input("Masukkan bilangan biner: ")

try:
    desimal = int(biner, 2)
    heksa = hex(desimal).upper()[2:]
    print(f"Bilangan biner: {biner}")
    print(f"Konversi ke desimal: {desimal}")
    print(f"Konversi ke hexadesimal: {heksa}")
except ValueError:
    print("Input tidak valid! Masukkan hanya angka 0 dan 1.")

def hitung_nilai_akhir(sikap, tugas, uts, uas):
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
  
    if 81 <= total <= 100:
        grade = "A"
        bobot = 4
    elif 76 <= total <= 80:
        grade = "B+"
        bobot = 3.5
    elif 71 <= total <= 75:
        grade = "B"
        bobot = 3
    elif 66 <= total <= 70:
        grade = "C+"
        bobot = 2.5
    elif 56 <= total <= 65:
        grade = "C"
        bobot = 2
    elif 46 <= total <= 55:
        grade = "D"
        bobot = 1
    else:
        grade = "E"
        bobot = 0

    if total >= 56:
        keterangan = "Lulus"
    else:
        keterangan = "Tidak Lulus"
    
    return total, grade, bobot, keterangan


print("=== Program Menghitung Nilai Akhir Akademik ===")
sikap = float(input("Masukkan nilai Sikap/Kehadiran (0-100): "))
tugas = float(input("Masukkan nilai Tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

total, grade, bobot, keterangan = hitung_nilai_akhir(sikap, tugas, uts, uas)

print("\n=== Hasil Perhitungan ===")
print(f"Total Nilai Akhir : {total:.2f}")
print(f"Nilai Huruf       : {grade}")
print(f"Bobot Nilai       : {bobot}")
print(f"Keterangan        : {keterangan}")

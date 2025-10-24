import tkinter as tk
from tkinter import messagebox

# ====== Fungsi Kalkulator ======
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else "Error: Bagi 0!"

# ====== Fungsi Hitung Nilai ======
def hitung_nilai_akhir(sikap, tugas, uts, uas):
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

    if 81 <= total <= 100:
        grade, bobot = "A", 4
    elif 76 <= total <= 80:
        grade, bobot = "B+", 3.5
    elif 71 <= total <= 75:
        grade, bobot = "B", 3
    elif 66 <= total <= 70:
        grade, bobot = "C+", 2.5
    elif 56 <= total <= 65:
        grade, bobot = "C", 2
    elif 46 <= total <= 55:
        grade, bobot = "D", 1
    else:
        grade, bobot = "E", 0

    keterangan = "Lulus" if total >= 56 else "Tidak Lulus"
    return total, grade, bobot, keterangan


# ====== Utility Tombol Warna ======
def buat_tombol(master, text, command, bg, fg="white"):
    btn = tk.Button(master, text=text, command=command, bg=bg, fg=fg,
                    font=("Arial", 10, "bold"), width=20, relief="raised", bd=3)
    btn.bind("<Enter>", lambda e: btn.config(bg="black", fg="yellow"))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg, fg=fg))
    return btn


# ====== Form Latihan 1 ======
def buka_latihan1():
    latihan1 = tk.Toplevel(root)
    latihan1.title("Latihan 1 - Kalkulator")
    latihan1.geometry("420x320")
    latihan1.config(bg="#E6F7FF")

    tk.Label(latihan1, text="Kalkulator Sederhana (Latihan 1)", font=("Arial", 14, "bold"), bg="#E6F7FF").pack(pady=10)

    frame = tk.Frame(latihan1, bg="white", bd=2, relief="groove")
    frame.pack(pady=10)

    tk.Label(frame, text="Angka Pertama:", bg="white").grid(row=0, column=0, padx=5, pady=5)
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Angka Kedua:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    hasil_label = tk.Label(latihan1, text="", font=("Arial", 11), bg="#E6F7FF", justify="left")
    hasil_label.pack(pady=10)

    def hitung():
        try:
            a, b = float(e1.get()), float(e2.get())
            hasil = f"""
            Penjumlahan : {tambah(a, b)}
            Pengurangan : {kurang(a, b)}
            Perkalian   : {kali(a, b)}
            Pembagian   : {bagi(a, b)}
            """
            hasil_label.config(text=hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    buat_tombol(latihan1, "Hitung", hitung, "#007ACC").pack(pady=5)


# ====== Form Latihan 2 ======
def buka_latihan2():
    latihan2 = tk.Toplevel(root)
    latihan2.title("Latihan 2 - Kalkulator")
    latihan2.geometry("420x320")
    latihan2.config(bg="#FFF0F5")

    tk.Label(latihan2, text="Kalkulator Sederhana (Latihan 2)", font=("Arial", 14, "bold"), bg="#FFF0F5").pack(pady=10)

    frame = tk.Frame(latihan2, bg="white", bd=2, relief="groove")
    frame.pack(pady=10)

    tk.Label(frame, text="Angka Pertama:", bg="white").grid(row=0, column=0, padx=5, pady=5)
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Angka Kedua:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    hasil_label = tk.Label(latihan2, text="", font=("Arial", 11), bg="#FFF0F5", justify="left")
    hasil_label.pack(pady=10)

    def hitung():
        try:
            a, b = float(e1.get()), float(e2.get())
            hasil = f"""
            Penjumlahan : {tambah(a, b)}
            Pengurangan : {kurang(a, b)}
            Perkalian   : {kali(a, b)}
            Pembagian   : {bagi(a, b)}
            """
            hasil_label.config(text=hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    buat_tombol(latihan2, "Hitung", hitung, "#FF69B4").pack(pady=5)


# ====== Form Latihan 3 ======
def buka_latihan3():
    latihan3 = tk.Toplevel(root)
    latihan3.title("Latihan 3 - Nilai Akademik")
    latihan3.geometry("450x380")
    latihan3.config(bg="#F0FFF0")

    tk.Label(latihan3, text="Hitung Nilai Akhir Akademik", font=("Arial", 14, "bold"), bg="#F0FFF0").pack(pady=10)

    frame = tk.Frame(latihan3, bg="white", bd=2, relief="groove")
    frame.pack(pady=10)

    tk.Label(frame, text="Nilai Sikap:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Nilai Tugas:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    tk.Label(frame, text="Nilai UTS:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    e3 = tk.Entry(frame); e3.grid(row=2, column=1)

    tk.Label(frame, text="Nilai UAS:", bg="white").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    e4 = tk.Entry(frame); e4.grid(row=3, column=1)

    hasil_label = tk.Label(latihan3, text="", font=("Arial", 11), bg="#F0FFF0", justify="left")
    hasil_label.pack(pady=15)

    def hitung():
        try:
            sikap, tugas, uts, uas = float(e1.get()), float(e2.get()), float(e3.get()), float(e4.get())
            total, grade, bobot, keterangan = hitung_nilai_akhir(sikap, tugas, uts, uas)

            hasil = f"""
            Total Nilai Akhir : {total:.2f}
            Nilai Huruf       : {grade}
            Bobot Nilai       : {bobot}
            Keterangan        : {keterangan}
            """
            hasil_label.config(text=hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    buat_tombol(latihan3, "Hitung Nilai", hitung, "#32CD32").pack(pady=5)


# ====== MENU UTAMA ======
root = tk.Tk()
root.title("Program Pilihan Latihan")
root.geometry("450x350")
root.config(bg="#FDF5E6")

tk.Label(root, text="=== MENU LATIHAN ===", font=("Arial", 16, "bold"), bg="#FDF5E6").pack(pady=20)

buat_tombol(root, "Latihan 1 - Kalkulator", buka_latihan1, "#007ACC").pack(pady=5)
buat_tombol(root, "Latihan 2 - Kalkulator", buka_latihan2, "#FF69B4").pack(pady=5)
buat_tombol(root, "Latihan 3 - Nilai Akademik", buka_latihan3, "#32CD32").pack(pady=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b): return a / b if b != 0 else "Error: Bagi 0!"

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


def buka_latihan1():
    latihan1 = tk.Toplevel(root)
    latihan1.title("Latihan 1 - Kalkulator")
    latihan1.geometry("400x300")

    tk.Label(latihan1, text="Kalkulator Sederhana (Latihan 1)", font=("Arial", 12, "bold")).pack(pady=10)

    frame = tk.Frame(latihan1)
    frame.pack()

    tk.Label(frame, text="Angka Pertama:").grid(row=0, column=0, padx=5, pady=5)
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Angka Kedua:").grid(row=1, column=0, padx=5, pady=5)
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    hasil_label = tk.Label(latihan1, text="", font=("Arial", 11), justify="left")
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

    tk.Button(latihan1, text="Hitung", bg="lightblue", command=hitung).pack(pady=5)


def buka_latihan2():
    latihan2 = tk.Toplevel(root)
    latihan2.title("Latihan 2 - Kalkulator")
    latihan2.geometry("400x300")

    tk.Label(latihan2, text="Kalkulator Sederhana (Latihan 2)", font=("Arial", 12, "bold")).pack(pady=10)

    frame = tk.Frame(latihan2)
    frame.pack()

    tk.Label(frame, text="Angka Pertama:").grid(row=0, column=0, padx=5, pady=5)
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Angka Kedua:").grid(row=1, column=0, padx=5, pady=5)
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    hasil_label = tk.Label(latihan2, text="", font=("Arial", 11), justify="left")
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

    tk.Button(latihan2, text="Hitung", bg="lightgreen", command=hitung).pack(pady=5)


def buka_latihan3():
    latihan3 = tk.Toplevel(root)
    latihan3.title("Latihan 3 - Nilai Akademik")
    latihan3.geometry("400x350")

    tk.Label(latihan3, text="Hitung Nilai Akhir Akademik", font=("Arial", 12, "bold")).pack(pady=10)

    frame = tk.Frame(latihan3)
    frame.pack()

    tk.Label(frame, text="Nilai Sikap:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    e1 = tk.Entry(frame); e1.grid(row=0, column=1)

    tk.Label(frame, text="Nilai Tugas:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    e2 = tk.Entry(frame); e2.grid(row=1, column=1)

    tk.Label(frame, text="Nilai UTS:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    e3 = tk.Entry(frame); e3.grid(row=2, column=1)

    tk.Label(frame, text="Nilai UAS:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    e4 = tk.Entry(frame); e4.grid(row=3, column=1)

    hasil_label = tk.Label(latihan3, text="", font=("Arial", 11), justify="left")
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

    tk.Button(latihan3, text="Hitung Nilai", bg="lightblue", command=hitung).pack(pady=5)


root = tk.Tk()
root.title("Program Pilihan Latihan")
root.geometry("400x300")

tk.Label(root, text="=== MENU LATIHAN ===", font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(root, text="Latihan 1 - Kalkulator", width=25, command=buka_latihan1).pack(pady=5)
tk.Button(root, text="Latihan 2 - Kalkulator", width=25, command=buka_latihan2).pack(pady=5)
tk.Button(root, text="Latihan 3 - Nilai Akademik", width=25, command=buka_latihan3).pack(pady=5)

root.mainloop()

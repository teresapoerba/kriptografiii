import tkinter as tk
from tkinter import messagebox

def hitung_nilai_akhir():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

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

        hasil_total.set(f"{total:.2f}")
        hasil_grade.set(grade)
        hasil_bobot.set(bobot)
        hasil_keterangan.set(keterangan)

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid (0-100)!")

root = tk.Tk()
root.title("Form Nilai Akhir Akademik")

tk.Label(root, text="Sikap/Kehadiran (10%)").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_sikap = tk.Entry(root)
entry_sikap.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tugas (30%)").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_tugas = tk.Entry(root)
entry_tugas.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="UTS (25%)").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_uts = tk.Entry(root)
entry_uts.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="UAS (35%)").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_uas = tk.Entry(root)
entry_uas.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Hitung Nilai Akhir", command=hitung_nilai_akhir).grid(row=4, column=0, columnspan=2, pady=10)

hasil_total = tk.StringVar()
hasil_grade = tk.StringVar()
hasil_bobot = tk.StringVar()
hasil_keterangan = tk.StringVar()

tk.Label(root, text="Total Nilai Akhir:").grid(row=5, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=hasil_total, state="readonly").grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Nilai Huruf:").grid(row=6, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=hasil_grade, state="readonly").grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Bobot Nilai:").grid(row=7, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=hasil_bobot, state="readonly").grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Keterangan:").grid(row=8, column=0, sticky="w", padx=10)
tk.Entry(root, textvariable=hasil_keterangan, state="readonly").grid(row=8, column=1, padx=10, pady=5)

root.mainloop()

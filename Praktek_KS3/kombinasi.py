import tkinter as tk
from tkinter import messagebox
import itertools

def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    if r > n:
        return 0
    return faktorial(n) // (faktorial(r) * faktorial(n - r))

def hitung_kombinasi():
    huruf_input = entry_huruf.get().strip()
    r_input = entry_r.get().strip()

    if not huruf_input or not r_input:
        messagebox.showwarning("Peringatan", "Harap isi semua kolom!")
        return

    try:
        huruf = huruf_input.split()
        n = len(huruf)
        r = int(r_input)
    except ValueError:
        messagebox.showerror("Error", "Masukkan jumlah huruf yang benar!")
        return

    if r > n:
        messagebox.showerror("Error", "Nilai r tidak boleh lebih besar dari jumlah huruf!")
        return

    jumlah = kombinasi(n, r)
    hasil_text.delete("1.0", tk.END)
    hasil_text.insert(tk.END, f"Jumlah kombinasi C({n}, {r}) = {jumlah}\n\n")

    hasil_text.insert(tk.END, "Hasil kombinasi huruf:\n")
    hasil_kombinasi = list(itertools.combinations(huruf, r))
    for komb in hasil_kombinasi:
        hasil_text.insert(tk.END, f"{komb}\n")


root = tk.Tk()
root.title("Program Kombinasi Huruf")
root.geometry("600x450")
root.configure(bg="#E8F0FE")  

judul = tk.Label(root, text="💠 PROGRAM KOMBINASI DENGAN INISIAL HURUF 💠",
                 font=("Segoe UI", 14, "bold"), bg="#E8F0FE", fg="#3C3C3C")
judul.pack(pady=10)

frame_input = tk.Frame(root, bg="#F9FBFD", bd=2, relief="groove")
frame_input.pack(pady=10, padx=20, fill="x")

tk.Label(frame_input, text="Masukkan huruf (pisahkan dengan spasi):",
         bg="#F9FBFD", font=("Segoe UI", 11)).pack(pady=5)
entry_huruf = tk.Entry(frame_input, font=("Segoe UI", 11), width=50, justify="center")
entry_huruf.pack(pady=5)

tk.Label(frame_input, text="Masukkan jumlah huruf yang dipilih (r):",
         bg="#F9FBFD", font=("Segoe UI", 11)).pack(pady=5)
entry_r = tk.Entry(frame_input, font=("Segoe UI", 11), width=10, justify="center")
entry_r.pack(pady=5)

btn_hitung = tk.Button(root, text="Hitung Kombinasi", font=("Segoe UI", 12, "bold"),
                       bg="#B5EAD7", fg="#2F4F4F", relief="raised", command=hitung_kombinasi)
btn_hitung.pack(pady=10)

frame_hasil = tk.Frame(root, bg="#FDFEFE", bd=2, relief="sunken")
frame_hasil.pack(pady=10, padx=20, fill="both", expand=True)

tk.Label(frame_hasil, text="Hasil Perhitungan:", bg="#FDFEFE",
         font=("Segoe UI", 12, "bold")).pack(anchor="w", padx=10, pady=5)

hasil_text = tk.Text(frame_hasil, height=10, font=("Consolas", 11),
                     bg="#FFFFFF", fg="#333333", wrap="word")
hasil_text.pack(padx=10, pady=5, fill="both", expand=True)

root.mainloop()

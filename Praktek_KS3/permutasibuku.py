import tkinter as tk
from tkinter import messagebox
import itertools

def proses_pengaturan():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())

        if n <= 0 or r <= 0:
            messagebox.showerror("Error", "Nilai n dan r harus lebih dari 0!")
            return
        buku = [f"Buku{i+1}" for i in range(n)]
        pengaturan = list(itertools.product(range(1, r + 1), repeat=n))

        hasil_box.delete("1.0", tk.END)  # Hapus hasil sebelumnya
        hasil_box.insert(tk.END, f"=== PROGRAM PENGATURAN BUKU DI RAK ===\n")
        hasil_box.insert(tk.END, f"Terdapat {len(pengaturan)} cara mengatur {n} buku di {r} bagian rak:\n\n")

        for cara in pengaturan:
            for i in range(n):
                hasil_box.insert(tk.END, f"{buku[i]} -> Bagian {cara[i]}\n")
            hasil_box.insert(tk.END, "-" * 30 + "\n")

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def clear_all():
    entry_n.delete(0, tk.END)
    entry_r.delete(0, tk.END)
    hasil_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("📚 Pengaturan Buku di Rak 📚")
root.geometry("550x550")
root.config(bg="#e6f0ef")  

judul = tk.Label(
    root,
    text="📘 PROGRAM PENGATURAN BUKU DI RAK 📘",
    bg="#e6f0ef",
    fg="#1b4d3e",
    font=("Segoe UI", 13, "bold")
)
judul.pack(pady=15)

frame_input = tk.Frame(root, bg="#e6f0ef")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Masukkan jumlah buku (n):", bg="#e6f0ef", fg="black", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
entry_n = tk.Entry(frame_input, font=("Consolas", 11), width=15, justify="center")
entry_n.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_input, text="Masukkan jumlah bagian rak (r):", bg="#e6f0ef", fg="black", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
entry_r = tk.Entry(frame_input, font=("Consolas", 11), width=15, justify="center")
entry_r.grid(row=1, column=1, padx=10, pady=5)

frame_btn = tk.Frame(root, bg="#e6f0ef")
frame_btn.pack(pady=10)

btn_proses = tk.Button(frame_btn, text="Proses", command=proses_pengaturan, bg="#6ab04c", fg="white", font=("Segoe UI", 10, "bold"), relief="ridge", width=10)
btn_proses.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(frame_btn, text="Clear", command=clear_all, bg="#ff7979", fg="white", font=("Segoe UI", 10, "bold"), relief="ridge", width=10)
btn_clear.grid(row=0, column=1, padx=10)
tk.Label(root, text="Hasil:", bg="#e6f0ef", fg="black", font=("Segoe UI", 11, "bold")).pack(pady=5)
hasil_box = tk.Text(root, height=15, width=60, font=("Consolas", 10))
hasil_box.pack(pady=5)
tk.Label(root, text="Made with 💚 by Tkinter", bg="#e6f0ef", fg="#1b4d3e", font=("Segoe UI", 8, "italic")).pack(side="bottom", pady=5)

root.mainloop()

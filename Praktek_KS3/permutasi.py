import tkinter as tk
from tkinter import messagebox, ttk
import itertools


def permutasi_menyeluruh(data):
    return list(itertools.permutations(data))

def permutasi_sebagian(data, k):
    return list(itertools.permutations(data, k))

def permutasi_keliling(data):
    if not data:
        return []
    pertama = data[0]
    return [[pertama] + list(p) for p in itertools.permutations(data[1:])]

def permutasi_berkelompok(data, grup):
    hasil = []
    for g in itertools.combinations(data, grup):
        hasil.extend(itertools.permutations(g))
    return hasil


def tampilkan_hasil(jenis, hasil):
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f"=== {jenis.upper()} ===\n")
    for p in hasil:
        text_output.insert(tk.END, f"{p}\n")


def proses():
    data = entry_data.get().split()
    pilihan = combo_jenis.get()

    if not data:
        messagebox.showwarning("Peringatan", "Masukkan elemen terlebih dahulu!")
        return

    if pilihan == "Permutasi Menyeluruh":
        hasil = permutasi_menyeluruh(data)
        tampilkan_hasil(pilihan, hasil)

    elif pilihan == "Permutasi Sebagian":
        try:
            k = int(entry_k.get())
            if k <= 0 or k > len(data):
                raise ValueError
            hasil = permutasi_sebagian(data, k)
            tampilkan_hasil(pilihan, hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai k yang valid!")

    elif pilihan == "Permutasi Keliling":
        hasil = permutasi_keliling(data)
        tampilkan_hasil(pilihan, hasil)

    elif pilihan == "Permutasi Berkelompok":
        try:
            grup = int(entry_k.get())
            if grup <= 0 or grup > len(data):
                raise ValueError
            hasil = permutasi_berkelompok(data, grup)
            tampilkan_hasil(pilihan, hasil)
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai kelompok yang valid!")
    else:
        messagebox.showinfo("Info", "Pilih jenis permutasi terlebih dahulu.")


def clear():
    entry_data.delete(0, tk.END)
    entry_k.delete(0, tk.END)
    text_output.delete(1.0, tk.END)
    combo_jenis.set("")


root = tk.Tk()
root.title("Program Permutasi")
root.geometry("600x500")
root.configure(bg="#E8EAF6")  


judul = tk.Label(root, text="✨ PROGRAM PERMUTASI ✨", 
                 font=("Segoe UI", 16, "bold"), 
                 bg="#E8EAF6", fg="#3E4A89")
judul.pack(pady=10)


frame_input = tk.Frame(root, bg="#E8EAF6")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Masukkan elemen (pisahkan spasi):", 
         bg="#E8EAF6", fg="#3E4A89", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w")
entry_data = tk.Entry(frame_input, width=40)
entry_data.grid(row=1, column=0, padx=5, pady=5)

tk.Label(frame_input, text="Masukkan nilai k / kelompok:", 
         bg="#E8EAF6", fg="#3E4A89", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w")
entry_k = tk.Entry(frame_input, width=15)
entry_k.grid(row=3, column=0, padx=5, pady=5, sticky="w")


tk.Label(frame_input, text="Pilih Jenis Permutasi:", 
         bg="#E8EAF6", fg="#3E4A89", font=("Segoe UI", 10)).grid(row=4, column=0, sticky="w")
combo_jenis = ttk.Combobox(frame_input, width=35, state="readonly", 
                           values=[
                               "Permutasi Menyeluruh", 
                               "Permutasi Sebagian",
                               "Permutasi Keliling",
                               "Permutasi Berkelompok"
                           ])
combo_jenis.grid(row=5, column=0, padx=5, pady=5)


frame_tombol = tk.Frame(root, bg="#E8EAF6")
frame_tombol.pack(pady=10)

btn_proses = tk.Button(frame_tombol, text="Proses", command=proses, 
                       bg="#A5D6A7", fg="black", font=("Segoe UI", 10, "bold"),
                       relief="flat", width=12)
btn_proses.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(frame_tombol, text="Clear", command=clear, 
                      bg="#FFCDD2", fg="black", font=("Segoe UI", 10, "bold"),
                      relief="flat", width=12)
btn_clear.grid(row=0, column=1, padx=5)


frame_output = tk.Frame(root, bg="#E8EAF6")
frame_output.pack(pady=10, fill="both", expand=True)

tk.Label(frame_output, text="Hasil:", 
         bg="#E8EAF6", fg="#3E4A89", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10)
text_output = tk.Text(frame_output, height=12, wrap="word", bg="#F3F4F6", fg="#2E2E2E", font=("Consolas", 10))
text_output.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()

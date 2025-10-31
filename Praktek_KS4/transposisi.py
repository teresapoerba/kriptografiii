import tkinter as tk
from tkinter import messagebox, ttk

# === FUNGSI SUBSTITUSI ===
def substitusi_cipher(teks):
    hasil = ""
    for ch in teks.lower():
        if ch == 'u':
            hasil += 'k'
        elif ch == 'a':
            hasil += 'b'
        elif ch.isalpha():
            hasil += ch
        else:
            pass  # abaikan spasi atau tanda baca
    return hasil

# === FUNGSI TRANSPOSISI ===
def transposisi_cipher(teks, kolom=4):
    panjang = len(teks)
    baris = (panjang + kolom - 1) // kolom
    total = baris * kolom
    teks += "x" * (total - panjang)

    matriks = [teks[i*kolom:(i+1)*kolom] for i in range(baris)]
    return matriks

def baca_per_kolom(matriks):
    kolom = len(matriks[0])
    baris = len(matriks)
    hasil = ""
    for c in range(kolom):
        for r in range(baris):
            hasil += matriks[r][c]
    return hasil

# === PROSES ENKRIPSI ===
def proses_enkripsi():
    plaintext = entry_plaintext.get().strip()
    key_str = entry_kolom.get().strip()

    if not plaintext:
        messagebox.showwarning("Peringatan", "Masukkan plaintext terlebih dahulu!")
        return
    if not key_str.isdigit():
        messagebox.showerror("Error", "Kolom harus berupa angka!")
        return

    kolom = int(key_str)
    plain_clean = plaintext.replace(" ", "").lower()
    hasil_substitusi = substitusi_cipher(plain_clean)
    matriks = transposisi_cipher(hasil_substitusi, kolom)
    hasil_transposisi = baca_per_kolom(matriks)

    # Tampilkan hasil di GUI
    entry_substitusi.delete(0, tk.END)
    entry_substitusi.insert(0, hasil_substitusi)

    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, hasil_transposisi)

    # Tampilkan matriks transposisi di tabel
    for i in tabel_matriks.get_children():
        tabel_matriks.delete(i)

    for r, row in enumerate(matriks):
        tabel_matriks.insert("", "end", values=[ch.upper() for ch in row])

# === FUNGSI RESET ===
def reset():
    entry_plaintext.delete(0, tk.END)
    entry_kolom.delete(0, tk.END)
    entry_substitusi.delete(0, tk.END)
    entry_ciphertext.delete(0, tk.END)
    for i in tabel_matriks.get_children():
        tabel_matriks.delete(i)

# === FUNGSI SALIN HASIL ===
def salin():
    hasil = entry_ciphertext.get()
    if hasil:
        root.clipboard_clear()
        root.clipboard_append(hasil)
        messagebox.showinfo("Disalin", "Ciphertext berhasil disalin ke clipboard!")

# === GUI SETUP ===
root = tk.Tk()
root.title("Gabungan Substitusi + Transposisi Cipher")
root.geometry("650x600")
root.configure(bg="#DFF5E3")

# === JUDUL ===
judul = tk.Label(root, text="🔐 Substitusi + Transposisi Cipher", font=("Poppins", 18, "bold"), bg="#DFF5E3", fg="#146C43")
judul.pack(pady=10)

# === FRAME INPUT ===
frame_input = tk.Frame(root, bg="#DFF5E3")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Masukkan Plaintext:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext = tk.Entry(frame_input, width=40, font=("Consolas", 11))
entry_plaintext.grid(row=0, column=1, padx=10)

tk.Label(frame_input, text="Jumlah Kolom:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=1, column=0, sticky="w", pady=5)
entry_kolom = tk.Entry(frame_input, width=40, font=("Consolas", 11))
entry_kolom.grid(row=1, column=1, padx=10)

# === FRAME HASIL ===
frame_hasil = tk.Frame(root, bg="#DFF5E3")
frame_hasil.pack(pady=10)

tk.Label(frame_hasil, text="Setelah Substitusi:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=0, column=0, sticky="w", pady=5)
entry_substitusi = tk.Entry(frame_hasil, width=50, font=("Consolas", 11))
entry_substitusi.grid(row=0, column=1, pady=5, padx=10)

tk.Label(frame_hasil, text="Ciphertext Akhir:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=1, column=0, sticky="w", pady=5)
entry_ciphertext = tk.Entry(frame_hasil, width=50, font=("Consolas", 11), fg="#2D6A4F")
entry_ciphertext.grid(row=1, column=1, pady=5, padx=10)

# === FRAME TOMBOL ===
frame_btn = tk.Frame(root, bg="#DFF5E3")
frame_btn.pack(pady=10)

btn_proses = tk.Button(frame_btn, text="🔒 Enkripsi", command=proses_enkripsi,
                       bg="#38B000", fg="white", font=("Poppins", 11, "bold"),
                       relief="flat", activebackground="#2D6A4F", cursor="hand2", width=12)
btn_proses.grid(row=0, column=0, padx=10)

btn_reset = tk.Button(frame_btn, text="🔄 Reset", command=reset,
                      bg="#52B788", fg="white", font=("Poppins", 11, "bold"),
                      relief="flat", activebackground="#40916C", cursor="hand2", width=12)
btn_reset.grid(row=0, column=1, padx=10)

btn_salin = tk.Button(frame_btn, text="📋 Salin Hasil", command=salin,
                      bg="#74C69D", fg="white", font=("Poppins", 11, "bold"),
                      relief="flat", activebackground="#40916C", cursor="hand2", width=12)
btn_salin.grid(row=0, column=2, padx=10)

# === LABEL TABEL ===
tk.Label(root, text="📊 Matriks Transposisi:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11, "bold")).pack(pady=5)

# === TABEL MATRIKS ===
tabel_frame = tk.Frame(root, bg="#DFF5E3")
tabel_frame.pack()

tabel_matriks = ttk.Treeview(tabel_frame, columns=("1", "2", "3", "4", "5", "6"), show="headings", height=6)
tabel_matriks.pack()

# Default 6 kolom biar fleksibel
for i in range(1, 7):
    tabel_matriks.heading(str(i), text=f"Kol {i}")
    tabel_matriks.column(str(i), width=80, anchor="center")

# === KETERANGAN ===
keterangan = tk.Label(root,
    text="💡 Substitusi otomatis: U→K, A→B | Transposisi: baca kolom demi kolom.",
    bg="#DFF5E3", fg="#40916C", font=("Poppins", 9))
keterangan.pack(pady=10)

root.mainloop()
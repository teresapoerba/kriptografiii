import tkinter as tk
from tkinter import messagebox

# === ATURAN SUBSTITUSI DARI DOKUMEN ===
aturan_substitusi = {
    'U': 'K',  # [cite: 198, 199]
    'N': 'N',  # [cite: 200, 201]
    'I': 'I',  # [cite: 202]
    'K': 'K',  # [cite: 203]
    'A': 'B'   # [cite: 204]
}

# === FUNGSI ENKRIPSI ===
def substitusi_cipher(plaintext, aturan):  # [cite: 189]
    ciphertext = ''  # [cite: 190]
    for char in plaintext.upper():  # [cite: 191]
        if char in aturan:  # [cite: 192]
            ciphertext += aturan[char]  # [cite: 194]
        else:
            ciphertext += char  # [cite: 195]
    return ciphertext  # [cite: 196]

# === FUNGSI TOMBOL ENKRIPSI ===
def proses_enkripsi():
    plaintext = entry_plaintext.get().strip().upper()
    if not plaintext:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu!")
        return

    ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

    entry_ciphertext.delete(0, tk.END)
    entry_ciphertext.insert(0, ciphertext)

# === FUNGSI RESET ===
def reset():
    entry_plaintext.delete(0, tk.END)
    entry_ciphertext.delete(0, tk.END)

# === FUNGSI SALIN HASIL ===
def salin():
    hasil = entry_ciphertext.get()
    if hasil:
        root.clipboard_clear()
        root.clipboard_append(hasil)
        messagebox.showinfo("Disalin", "Ciphertext berhasil disalin ke clipboard!")

# === GUI ===
root = tk.Tk()
root.title("Substitusi Cipher - Tema Hijau")
root.geometry("480x380")
root.configure(bg="#DFF5E3")

# === JUDUL ===
judul = tk.Label(root, text="🔐 Substitusi Cipher", font=("Poppins", 18, "bold"), bg="#DFF5E3", fg="#146C43")
judul.pack(pady=10)

# === FRAME UTAMA ===
frame = tk.Frame(root, bg="#DFF5E3")
frame.pack(pady=10)

# === INPUT PLAIN TEXT ===
tk.Label(frame, text="Masukkan Plaintext:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=0, column=0, sticky="w", pady=5)
entry_plaintext = tk.Entry(frame, width=40, font=("Consolas", 11))
entry_plaintext.grid(row=0, column=1, pady=5, padx=10)

# === HASIL CIPHERTEXT ===
tk.Label(frame, text="Hasil Ciphertext:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 11)).grid(row=1, column=0, sticky="w", pady=5)
entry_ciphertext = tk.Entry(frame, width=40, font=("Consolas", 11), fg="#2D6A4F")
entry_ciphertext.grid(row=1, column=1, pady=5, padx=10)

# === TOMBOL-TOMBOL ===
frame_btn = tk.Frame(root, bg="#DFF5E3")
frame_btn.pack(pady=15)

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

# === AREA INFORMASI ATURAN ===
frame_info = tk.Frame(root, bg="#DFF5E3")
frame_info.pack(pady=10)

tk.Label(frame_info, text="📘 Aturan Substitusi:", bg="#DFF5E3", fg="#1B4332", font=("Poppins", 10, "bold")).pack()
aturan_label = tk.Label(frame_info, text=str(aturan_substitusi),
                        bg="#DFF5E3", fg="#2D6A4F", font=("Consolas", 10))
aturan_label.pack()

# === KETERANGAN ===
keterangan = tk.Label(root,
    text="💡 Contoh: UNIKA → KNIKB berdasarkan aturan di atas.",
    bg="#DFF5E3", fg="#40916C", font=("Poppins", 9))
keterangan.pack(pady=5)

root.mainloop()

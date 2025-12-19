import tkinter as tk
from tkinter import messagebox
import random

# =============================
# FUNGSI CEK BILANGAN PRIMA
# =============================
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# =============================
# FUNGSI INVERS MODULO
# =============================
def mod_inverse(a, p):
    return pow(a, -1, p)

# =============================
# PROSES ELGAMAL
# =============================
def proses_elgamal():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        x = int(entry_x.get())
        plaintext = entry_plain.get()

        # -----------------------------
        # VALIDASI INPUT
        # -----------------------------
        if not is_prime(p):
            messagebox.showerror("Error", "p harus bilangan prima")
            return
        if g >= p:
            messagebox.showerror("Error", "g harus lebih kecil dari p")
            return
        if not (1 <= x <= p-2):
            messagebox.showerror("Error", "x harus 1 ≤ x ≤ p-2")
            return

        output.delete("1.0", tk.END)

        # =============================
        # PEMBANGKITAN KUNCI
        # =============================
        output.insert(tk.END, "====================================\n")
        output.insert(tk.END, "PROSES PEMBANGKITAN KUNCI\n")
        output.insert(tk.END, "====================================\n")

        output.insert(tk.END, f"Diketahui:\n")
        output.insert(tk.END, f"p = {p} (bilangan prima)\n")
        output.insert(tk.END, f"g = {g}\n")
        output.insert(tk.END, f"x = {x} (kunci privat)\n\n")

        y = pow(g, x, p)

        output.insert(tk.END, "Hitung kunci publik:\n")
        output.insert(tk.END, "y = g^x mod p\n")
        output.insert(tk.END, f"y = {g}^{x} mod {p} = {y}\n\n")

        output.insert(tk.END, f"Kunci Publik = (y, g, p) = ({y}, {g}, {p})\n")
        output.insert(tk.END, f"Kunci Privat = (x, p)   = ({x}, {p})\n\n")

        # =============================
        # PROSES ENKRIPSI
        # =============================
        output.insert(tk.END, "====================================\n")
        output.insert(tk.END, "PROSES ENKRIPSI\n")
        output.insert(tk.END, "====================================\n")

        k = random.randint(1, p-2)
        output.insert(tk.END, f"Bilangan acak k dipilih otomatis\n")
        output.insert(tk.END, f"k = {k}\n\n")

        cipher = []

        for i, ch in enumerate(plaintext):
            m = ord(ch)

            output.insert(tk.END, f"Huruf ke-{i+1}: {ch}\n")
            output.insert(tk.END, f"ASCII('{ch}') = {m}\n")

            a = pow(g, k, p)
            b = (pow(y, k, p) * m) % p

            output.insert(tk.END, "Hitung:\n")
            output.insert(tk.END, f"a = g^k mod p = {g}^{k} mod {p} = {a}\n")
            output.insert(tk.END, f"b = y^k * m mod p = {b}\n")
            output.insert(tk.END, f"Ciphertext = ({a}, {b})\n\n")

            cipher.append((a, b))

        # =============================
        # PROSES DEKRIPSI
        # =============================
        output.insert(tk.END, "====================================\n")
        output.insert(tk.END, "PROSES DEKRIPSI\n")
        output.insert(tk.END, "====================================\n")

        hasil = ""

        for i, (a, b) in enumerate(cipher):
            output.insert(tk.END, f"Cipher ke-{i+1}: ({a}, {b})\n")

            ax = pow(a, x, p)
            ax_inv = mod_inverse(ax, p)
            m = (b * ax_inv) % p
            ch = chr(m)

            output.insert(tk.END, f"a^x mod p = {a}^{x} mod {p} = {ax}\n")
            output.insert(tk.END, f"(a^x)^(-1) mod p = {ax_inv}\n")
            output.insert(tk.END, f"m = b * (a^x)^(-1) mod p = {m}\n")
            output.insert(tk.END, f"ASCII {m} = '{ch}'\n\n")

            hasil += ch

        output.insert(tk.END, f"HASIL DEKRIPSI = {hasil}\n")

    except:
        messagebox.showerror("Error", "Input tidak valid")

# =============================
# GUI
# =============================
root = tk.Tk()
root.title("ElGamal Edukatif Step by Step")
root.geometry("900x700")

tk.Label(root, text=" ELGAMAL ",
         font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Bilangan Prima p").grid(row=0, column=0, sticky="w")
entry_p = tk.Entry(frame)
entry_p.grid(row=0, column=1)

tk.Label(frame, text="Generator g").grid(row=1, column=0, sticky="w")
entry_g = tk.Entry(frame)
entry_g.grid(row=1, column=1)

tk.Label(frame, text="Kunci Privat x").grid(row=2, column=0, sticky="w")
entry_x = tk.Entry(frame)
entry_x.grid(row=2, column=1)

tk.Label(frame, text="Plaintext").grid(row=3, column=0, sticky="w")
entry_plain = tk.Entry(frame, width=40)
entry_plain.grid(row=3, column=1)

tk.Button(root, text="PROSES ELGAMAL",
          command=proses_elgamal,
          bg="green", fg="white",
          font=("Arial", 10, "bold")).pack(pady=10)

output = tk.Text(root, height=30, width=110)
output.pack()

root.mainloop()

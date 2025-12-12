import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import math


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    r = int(n**0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_prime(low=50, high=200):
    primes = [x for x in range(low, high+1) if is_prime(x)]
    return random.choice(primes)

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a)*y, y

def modinv(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        return None
    return x % phi

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)


class RSARandomApp:
    def __init__(self, root):
        root.title("Latihan 2 – RSA (p,q,e Bilangan Prima 50–200)")
        root.geometry("900x680")
        root.config(bg="#FFF5E8")

        tk.Label(root, text="LATIHAN 2 – RSA NILAI ACAK (PRIMA 50–200)", 
                 font=("Arial", 18, "bold"), bg="#FFF5E8").pack(pady=10)

        frame = tk.Frame(root, bg="#FFF5E8")
        frame.pack()

        tk.Label(frame, text="Masukkan Plaintext:", bg="#FFF5E8").grid(row=0, column=0)
        self.entry = tk.Entry(frame, width=50, font=("Consolas", 12))
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        tk.Button(root, text="🔁 Generate Key + Enkripsi + Dekripsi", 
                  bg="#FFD9A0", font=("Arial", 11, "bold"),
                  command=self.run_rsa).pack(pady=8)

        tk.Label(root, text="Kunci Publik & Privat:", bg="#FFF5E8").pack(anchor="w", padx=10)
        self.key_box = scrolledtext.ScrolledText(root, width=100, height=4, font=("Consolas", 10))
        self.key_box.pack(padx=10, pady=5)

        tk.Label(root, text="Ciphertext:", bg="#FFF5E8").pack(anchor="w", padx=10)
        self.cipher_box = scrolledtext.ScrolledText(root, width=100, height=3, font=("Consolas", 10))
        self.cipher_box.pack(padx=10, pady=5)

        tk.Label(root, text="Dekripsi:", bg="#FFF5E8").pack(anchor="w", padx=10)
        self.plain_box = scrolledtext.ScrolledText(root, width=100, height=3, font=("Consolas", 10))
        self.plain_box.pack(padx=10, pady=5)

        tk.Label(root, text="DEBUG DETAIL PERHITUNGAN:", bg="#FFF5E8").pack(anchor="w", padx=10)
        self.debug = scrolledtext.ScrolledText(root, width=100, height=20, font=("Consolas", 10))
        self.debug.pack(padx=10, pady=5)

    def run_rsa(self):
        text = self.entry.get()
        if text == "":
            messagebox.showwarning("Peringatan", "Isi plaintext terlebih dahulu!")
            return

        p = generate_prime()
        q = generate_prime()
        while q == p:
            q = generate_prime()

        n = p * q
        phi = (p - 1) * (q - 1)

        e = generate_prime()
        while math.gcd(e, phi) != 1 or e == p or e == q:
            e = generate_prime()

        d = modinv(e, phi)

        self.debug.delete("1.0", tk.END)
        self.key_box.delete("1.0", tk.END)
        self.cipher_box.delete("1.0", tk.END)
        self.plain_box.delete("1.0", tk.END)

        key_info = (
            f"p = {p}\n"
            f"q = {q}\n"
            f"n = {n}\n"
            f"phi(n) = {phi}\n"
            f"e (prima 50–200) = {e}\n"
            f"d = {d}\n"
            f"Public Key  = (e={e}, n={n})\n"
            f"Private Key = (d={d}, n={n})\n"
        )
        self.key_box.insert(tk.END, key_info)

        self.debug.insert(tk.END, "=== RSA LATIHAN 2 – NILAI PRIMA ACAK 50–200 ===\n")
        self.debug.insert(tk.END, key_info + "\n")

        cipher_list = []
        self.debug.insert(tk.END, "=== ENKRIPSI PER KARAKTER ===\n")
        for i, ch in enumerate(text):
            m = ord(ch)
            c = rsa_encrypt(m, e, n)
            cipher_list.append(str(c))
            self.debug.insert(tk.END, f"[{i}] '{ch}' -> m={m} -> c={c}\n")

        cipher_text = " ".join(cipher_list)
        self.cipher_box.insert(tk.END, cipher_text)

        self.debug.insert(tk.END, "\n=== DEKRIPSI PER KARAKTER ===\n")
        decrypted_chars = []
        for i, c_str in enumerate(cipher_list):
            c = int(c_str)
            m2 = rsa_decrypt(c, d, n)
            ch2 = chr(m2)
            decrypted_chars.append(ch2)
            self.debug.insert(tk.END, f"[{i}] {c} -> m={m2} -> '{ch2}'\n")

        final_plain = "".join(decrypted_chars)
        self.plain_box.insert(tk.END, final_plain)

        self.debug.insert(tk.END, "\n=== SELESAI ===")
        

if __name__ == "__main__":
    root = tk.Tk()
    RSARandomApp(root)
    root.mainloop()

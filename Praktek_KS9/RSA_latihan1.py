import tkinter as tk
from tkinter import scrolledtext, messagebox

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None
    return x % m

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

class RSAStatic:
    def __init__(self, root):
        root.title("Latihan 1 – RSA p=17, q=11, e=7")
        root.geometry("850x600")
        root.config(bg="#eef9ff")

        tk.Label(root, text="LATIHAN 1 – RSA NILAI TETAP",
                 font=("Arial", 18, "bold"), bg="#eef9ff").pack(pady=10)

        frame = tk.Frame(root, bg="#eef9ff")
        frame.pack()

        tk.Label(frame, text="Masukkan plaintext:", bg="#eef9ff").grid(row=0, column=0)
        self.entry = tk.Entry(frame, width=40)
        self.entry.grid(row=1, column=0, pady=5)

        tk.Button(root, text="ENKRIPSI + DEKRIPSI", bg="#b6e5ff",
                  command=self.run_rsa).pack(pady=10)

        tk.Label(root, text="Ciphertext:", bg="#eef9ff").pack(anchor="w", padx=10)
        self.out_cipher = scrolledtext.ScrolledText(root, width=90, height=4)
        self.out_cipher.pack()

        tk.Label(root, text="Dekripsi:", bg="#eef9ff").pack(anchor="w", padx=10)
        self.out_plain = scrolledtext.ScrolledText(root, width=90, height=3)
        self.out_plain.pack()

        tk.Label(root, text="Detail Perhitungan:", bg="#eef9ff").pack(anchor="w", padx=10)
        self.debug = scrolledtext.ScrolledText(root, width=90, height=20)
        self.debug.pack()

    def run_rsa(self):
        text = self.entry.get()
        if text == "":
            messagebox.showwarning("Warning", "Isi plaintext dahulu!")
            return

        p, q, e = 17, 11, 7
        n = p*q
        phi = (p-1)*(q-1)
        d = modinv(e, phi)

        self.out_cipher.delete("1.0", tk.END)
        self.out_plain.delete("1.0", tk.END)
        self.debug.delete("1.0", tk.END)

        cipher_list = []
        debug_log = f"""
=== PARAMETER RSA LATIHAN 1 ===
p = {p}
q = {q}
n = {n}
phi = {phi}
e = {e}
d = {d}


"""

        for ch in text:
            m = ord(ch)
            c = rsa_encrypt(m, e, n)
            cipher_list.append(str(c))
            debug_log += f"{ch} -> ord={m} -> c = {m}^{e} mod {n} = {c}\n"

        cipher_str = " ".join(cipher_list)
        self.out_cipher.insert(tk.END, cipher_str)

        debug_log += "\n=== DEKRIPSI ===\n"
        plain = ""

        for c_str in cipher_list:
            c = int(c_str)
            m2 = rsa_decrypt(c, d, n)
            plain += chr(m2)
            debug_log += f"{c} -> m = {c}^{d} mod {n} = {m2} -> '{chr(m2)}'\n"

        self.out_plain.insert(tk.END, plain)
        self.debug.insert(tk.END, debug_log)


if __name__ == "__main__":
    root = tk.Tk()
    RSAStatic(root)
    root.mainloop()

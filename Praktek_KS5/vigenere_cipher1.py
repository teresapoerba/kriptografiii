import tkinter as tk
from tkinter import messagebox, scrolledtext

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        ciphertext = ""
        key_index = 0
        detail = []  

        for p in plaintext:
            if p.isalpha():
                p_value = ord(p) - ord('A')
                k_value = ord(self.key[key_index % len(self.key)]) - ord('A')
                c_value = (p_value + k_value) % 26
                result_char = chr(ord('A') + c_value)
                ciphertext += result_char

                detail.append(f"{p} + {self.key[key_index % len(self.key)]} → {result_char} (geser {k_value})")
                key_index += 1
            else:
                ciphertext += p
                detail.append(f"{p} (tidak diubah)")

        return ciphertext, detail

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        plaintext = ""
        key_index = 0
        detail = [] 

        for c in ciphertext:
            if c.isalpha():
                c_value = ord(c) - ord('A')
                k_value = ord(self.key[key_index % len(self.key)]) - ord('A')
                p_value = (c_value - k_value + 26) % 26
                result_char = chr(ord('A') + p_value)
                plaintext += result_char

                detail.append(f"{c} - {self.key[key_index % len(self.key)]} → {result_char} (geser {-k_value})")
                key_index += 1
            else:
                plaintext += c
                detail.append(f"{c} (tidak diubah)")

        return plaintext, detail

class VigenereApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌸 Vigenère Cipher App")
        self.root.geometry("700x650")
        self.root.config(bg="#EAF6F6")

        title = tk.Label(
            root, text="🔐 Vigenère Cipher", font=("Poppins", 20, "bold"),
            fg="#3A506B", bg="#EAF6F6"
        )
        title.pack(pady=15)

        frame = tk.Frame(root, bg="#EAF6F6")
        frame.pack(pady=10)

        tk.Label(frame, text="Masukkan Teks:", font=("Poppins", 11), bg="#EAF6F6").grid(row=0, column=0, sticky="w")
        self.text_input = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=4, font=("Consolas", 11))
        self.text_input.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        tk.Label(frame, text="Masukkan Kunci:", font=("Poppins", 11), bg="#EAF6F6").grid(row=2, column=0, sticky="w")
        self.key_entry = tk.Entry(frame, width=30, font=("Consolas", 11))
        self.key_entry.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

        button_frame = tk.Frame(root, bg="#EAF6F6")
        button_frame.pack(pady=10)

        encrypt_btn = tk.Button(button_frame, text="🔒 Enkripsi", command=self.encrypt_text,
                                bg="#A8DADC", fg="#1D3557", font=("Poppins", 11, "bold"), width=12)
        encrypt_btn.grid(row=0, column=0, padx=10)

        decrypt_btn = tk.Button(button_frame, text="🔓 Dekripsi", command=self.decrypt_text,
                                bg="#F1FAEE", fg="#1D3557", font=("Poppins", 11, "bold"), width=12)
        decrypt_btn.grid(row=0, column=1, padx=10)

        tk.Label(root, text="Hasil:", font=("Poppins", 11), bg="#EAF6F6").pack()
        self.output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=5, font=("Consolas", 11))
        self.output_box.pack(padx=10, pady=5)

        tk.Label(root, text="🧩 Detail Proses:", font=("Poppins", 11), bg="#EAF6F6").pack()
        self.detail_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, font=("Consolas", 10), fg="#1D3557")
        self.detail_box.pack(padx=10, pady=5)

    def encrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci tidak boleh kosong!")
            return

        cipher = VigenereCipher(key)
        result, detail = cipher.encrypt(text)

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, result)

        self.detail_box.delete("1.0", tk.END)
        self.detail_box.insert(tk.END, "\n".join(detail))

    def decrypt_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Teks dan kunci tidak boleh kosong!")
            return

        cipher = VigenereCipher(key)
        result, detail = cipher.decrypt(text)

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, result)

        self.detail_box.delete("1.0", tk.END)
        self.detail_box.insert(tk.END, "\n".join(detail))

if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereApp(root)
    root.mainloop()

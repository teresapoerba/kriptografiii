import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------
# DES tables & constants
# -----------------------
PC1 = [
    57,49,41,33,25,17,9,1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,21,13,5,28,20,12,4
]

PC2 = [
    14,17,11,24,1,5,3,28,15,6,21,10,
    23,19,12,4,26,8,16,7,27,20,13,2,
    41,52,31,37,47,55,30,40,51,45,33,48,
    44,49,39,56,34,53,46,42,50,36,29,32
]

SHIFT_TABLE = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

FP = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

E = [
    32,1,2,3,4,5,4,5,6,7,8,9,
    8,9,10,11,12,13,12,13,14,15,16,17,
    16,17,18,19,20,21,20,21,22,23,24,25,
    24,25,26,27,28,29,28,29,30,31,32,1
]

SBOX = [
    [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],

    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],

    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],

    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],

    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
     [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
     [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
     [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],

    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
     [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
     [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
     [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],

    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
     [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
     [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
     [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],

    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

P = [
    16,7,20,21,29,12,28,17,
    1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,
    19,13,30,6,22,11,4,25
]

# -----------------------
# Helpers (bits/permute)
# -----------------------
def to_bits(b: bytes) -> str:
    return "".join(f"{byte:08b}" for byte in b)

def to_bytes(bits: str) -> bytes:
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

def permute(bits: str, table: list) -> str:
    return "".join(bits[i-1] for i in table)

def shift_left(bits: str, n: int) -> str:
    return bits[n:] + bits[:n]

# -----------------------
# Key schedule
# -----------------------
def generate_subkeys(key8: bytes) -> list:
    key_bits = to_bits(key8)
    key56 = permute(key_bits, PC1)
    C = key56[:28]
    D = key56[28:]
    subkeys = []
    for i in range(16):
        C = shift_left(C, SHIFT_TABLE[i])
        D = shift_left(D, SHIFT_TABLE[i])
        sub56 = C + D
        sub48 = permute(sub56, PC2)
        subkeys.append(sub48)
    return subkeys

# -----------------------
# Feistel function
# -----------------------
def feistel(R: str, K: str, debug=False):
    expanded = permute(R, E)
    xored = "".join('1' if expanded[i] != K[i] else '0' for i in range(48))

    s_out = ""
    sbox_logs = []

    for box_idx in range(8):
        block = xored[box_idx*6:(box_idx+1)*6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = SBOX[box_idx][row][col]
        out_bits = f"{val:04b}"
        s_out += out_bits
        sbox_logs.append(
            f"S{box_idx+1:02d}: in={block} row={row} col={col} val={val} out={out_bits}"
        )

    p_out = permute(s_out, P)

    if debug:
        return p_out, expanded, xored, sbox_logs, s_out, p_out

    return p_out

# -----------------------
# DES block encrypt
# -----------------------
def des_block_encrypt(block8: bytes, subkeys: list, debug=False):
    bits = to_bits(block8)
    permuted = permute(bits, IP)
    L = permuted[:32]
    R = permuted[32:]

    debug_log = []

    for i in range(16):
        if debug:
            debug_log.append(f"--- Round {i+1:02d} | using K{i+1:02d} ---")
            debug_log.append(f"Before: L = {L}")
            debug_log.append(f"        R = {R}")

            f_out, expanded, xored, sbox_logs, s32, p32 = feistel(R, subkeys[i], debug=True)

            debug_log.append(f"E(R) = {expanded}")
            debug_log.append(f"E(R) XOR K = {xored}")
            debug_log.append("S-box results:")
            for sb in sbox_logs:
                debug_log.append(f"    {sb}")
            debug_log.append(f"S_out (32bit) = {s32}")
            debug_log.append(f"P(S_out) = {p32}")
        else:
            f_out = feistel(R, subkeys[i])

        newR = "".join('1' if L[j] != f_out[j] else '0' for j in range(32))
        L, R = R, newR

        if debug and i == 15:
            round16_bits = L + R
            try:
                round16_hex = to_bytes(round16_bits).hex().upper()
            except:
                round16_hex = "<err>"
            debug_log.append(f"Round 16 output (bin): {round16_bits}")
            debug_log.append(f"Round 16 output (hex): {round16_hex}")
            debug_log.append("")

        if debug:
            debug_log.append(f"After : L = {L}")
            debug_log.append(f"        R = {R}\n")

    preout = R + L
    final_bits = permute(preout, FP)
    output_bytes = to_bytes(final_bits)

    if debug:
        return output_bytes, "\n".join(debug_log)

    return output_bytes

# -----------------------
# Padding helpers
# -----------------------
def pkcs5_pad(data: bytes) -> bytes:
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len]) * pad_len

def pkcs5_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 8:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

# -----------------------
# High-level encrypt/decrypt
# -----------------------
def des_encrypt(data: bytes, key8: bytes) -> tuple:
    subkeys = generate_subkeys(key8)
    padded = pkcs5_pad(data)
    cipher = b""
    logs = []

    for blk in range(0, len(padded), 8):
        block = padded[blk:blk+8]
        cb, lg = des_block_encrypt(block, subkeys, debug=True)
        cipher += cb
        logs.append(f"--- Block {(blk//8)+1} ---\n{lg}")

    return cipher, subkeys, "\n\n".join(logs)

def des_decrypt(cipher: bytes, key8: bytes) -> tuple:
    subkeys = generate_subkeys(key8)
    subkeys_rev = list(reversed(subkeys))
    out = b""
    for i in range(0, len(cipher), 8):
        out += des_block_encrypt(cipher[i:i+8], subkeys_rev, debug=False)
    return pkcs5_unpad(out), subkeys_rev

# -----------------------
# GUI
# -----------------------
PINK = "#f7d8e8"
FONT_MAIN = ("Times New Roman", 11)
FONT_HEADER = ("Times New Roman", 18, "bold")
FONT_OUTPUT = ("Times New Roman", 11)

class DESGuiApp:
    def __init__(self, root):
        self.root = root
        root.title("DES Encryption Tool (Complete)")
        root.geometry("1000x720")
        root.configure(bg=PINK)

        ttk.Style().configure("TButton", font=FONT_MAIN, padding=6)

        tk.Label(root, text="DES Encryption Tool (16 Round)", font=FONT_HEADER, bg=PINK)\
            .pack(pady=10)

        main = tk.Frame(root, bg=PINK)
        main.pack(fill="both", expand=True, padx=10, pady=5)

        # ---------- LEFT PANEL ----------
        left = tk.Frame(main, bg=PINK)
        left.pack(side="left", fill="y", padx=10)

        ttk.Label(left, text="Plaintext:").grid(row=0, column=0, sticky="w")
        self.txt_plain = tk.Text(left, width=45, height=8, font=FONT_MAIN)
        self.txt_plain.grid(row=1, column=0, pady=4)

        ttk.Label(left, text="Key (1–8 chars):").grid(row=2, column=0, sticky="w")
        self.entry_key = ttk.Entry(left, width=25, font=FONT_MAIN)
        self.entry_key.grid(row=3, column=0, pady=4)

        btnf = tk.Frame(left, bg=PINK)
        btnf.grid(row=4, column=0, pady=8)

        ttk.Button(btnf, text="Encrypt", command=self.encrypt_once).grid(row=0, column=0, padx=3)
        ttk.Button(btnf, text="Decrypt", command=self.decrypt_last).grid(row=0, column=1, padx=3)
        ttk.Button(btnf, text="Reset", command=self.reset_all).grid(row=0, column=2, padx=3)

        self.btn_view = ttk.Button(btnf, text="View Subkeys", command=self.view_subkeys)
        self.btn_view.grid(row=0, column=3, padx=3)
        self.btn_view.config(state="disabled")

        # ---------- RIGHT PANEL ----------
        right = tk.Frame(main, bg=PINK)
        right.pack(side="left", fill="both", expand=True)

        ttk.Label(right, text="Output:").pack(anchor="w")
        self.txt_output = tk.Text(right, width=75, height=36, font=FONT_OUTPUT)
        self.txt_output.pack(fill="both", expand=True, padx=5, pady=5)
        self.txt_output.config(state="disabled")

        # Internal memory
        self.last_cipher = b""
        self.last_subkeys = []
        self.encrypt_count = 0

    def get_key_bytes(self):
        key = self.entry_key.get()
        if not (1 <= len(key) <= 8):
            raise ValueError("Key length must be 1–8 characters.")
        kb = key.encode()
        return kb.ljust(8, b'\x00')[:8]

    def encrypt_once(self):
        try:
            keyb = self.get_key_bytes()
        except Exception as e:
            messagebox.showerror("Key Error", str(e))
            return

        if self.encrypt_count == 0:
            data = self.txt_plain.get("1.0", "end").rstrip("\n").encode()
        else:
            data = self.last_cipher

        cipher, subkeys, logs = des_encrypt(data, keyb)

        self.last_cipher = cipher
        self.last_subkeys = subkeys
        self.encrypt_count += 1

        self.update_output(
            f"=== Encrypt #{self.encrypt_count} ===\n"
            f"Input bytes : {data}\n"
            f"Cipher HEX  : {cipher.hex().upper()}\n"
            f"Cipher BIN  : {to_bits(cipher)}\n\n"
            f"=== Round Log ===\n{logs}\n\n"
        )

        self.btn_view.config(state="normal")

    def decrypt_last(self):
        if not self.last_cipher:
            return messagebox.showinfo("Info", "Tidak ada ciphertext.")

        try:
            keyb = self.get_key_bytes()
        except Exception as e:
            return messagebox.showerror("Key Error", str(e))

        plain, _ = des_decrypt(self.last_cipher, keyb)

        try:
            decoded = plain.decode()
        except:
            decoded = str(plain)

        self.update_output(
            f"=== Decrypt Result ===\n"
            f"Plaintext : {decoded}\n"
            f"Bytes     : {plain}\n\n"
        )

    def view_subkeys(self):
        win = tk.Toplevel(self.root)
        win.title("Subkeys K1–K16")
        win.geometry("500x420")
        win.configure(bg=PINK)

        tk.Label(win, text="Subkeys (48-bit):", bg=PINK, font=("Times New Roman", 13, "bold"))\
            .pack(pady=5)

        txt = tk.Text(win, font=FONT_OUTPUT)
        txt.pack(fill="both", expand=True, padx=8, pady=8)

        for i, k in enumerate(self.last_subkeys, start=1):
            txt.insert("end", f"K{i:02d}: {k}\n")

    def update_output(self, msg):
        self.txt_output.config(state="normal")
        self.txt_output.insert("end", msg)
        self.txt_output.see("end")
        self.txt_output.config(state="disabled")

    def reset_all(self):
        self.txt_plain.delete("1.0", "end")
        self.entry_key.delete(0, "end")
        self.last_cipher = b""
        self.last_subkeys = []
        self.encrypt_count = 0
        self.btn_view.config(state="disabled")

        self.txt_output.config(state="normal")
        self.txt_output.delete("1.0", "end")
        self.txt_output.config(state="disabled")


# -----------------------
# Run Program
# -----------------------
if __name__ == "__main__":
    root = tk.Tk()
    DESGuiApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk

SBOX = [
    0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
    0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
    0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
    0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
    0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
    0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
    0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
    0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
    0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
    0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
    0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
    0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
    0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
    0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
    0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
    0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

def text_to_hex_list(text):
    t = text[:16].ljust(16, '\x00')
    return [format(ord(c), '02X') for c in t]

def to_matrix_rowmajor_from_hex_list(hex_list):
    m = [[None]*4 for _ in range(4)]
    for i in range(16):
        r = i // 4
        c = i % 4
        m[r][c] = hex_list[i]
    return m

def hex_matrix_to_int_matrix(hm):
    return [[int(hm[r][c],16) for c in range(4)] for r in range(4)]

def int_matrix_to_hex_matrix(im):
    return [[format(im[r][c],'02X') for c in range(4)] for r in range(4)]

def xor_int_matrices(a, b):
    return [[a[r][c] ^ b[r][c] for c in range(4)] for r in range(4)]

# key expansion 
def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    return [SBOX[b] for b in word]

def key_expansion_from_intmatrix_rowmajor(key_int_matrix):
    key_words = []
    for col in range(4):
        key_words.append([key_int_matrix[row][col] for row in range(4)])
    for i in range(4, 44):
        temp = key_words[i-1].copy()
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[(i//4)-1]
        neww = [temp[j] ^ key_words[i-4][j] for j in range(4)]
        key_words.append(neww)
    return key_words

def words_to_matrix_rowmajor(words):
    mat = [[0]*4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            mat[row][col] = words[col][row]
    return mat


root = tk.Tk()
root.title("AES TOOL - Pink Edition (Row-major) - No Enkripsi")
root.geometry("1100x680")
root.configure(bg="#FFD6E8")

style = ttk.Style()
style.configure("TButton", font=("Arial", 11, "bold"), padding=6)
style.map("TButton", background=[("active", "#FF9BCB")])

# INPUT
frame_in = tk.Frame(root, bg="#FFD6E8")
frame_in.pack(pady=12)

tk.Label(frame_in, text="Plaintext (maks 16 karakter):", bg="#FFD6E8",
         font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w")
entry_plain = tk.Entry(frame_in, width=40, font=("Arial", 12))
entry_plain.grid(row=0, column=1, padx=8)

tk.Label(frame_in, text="Cipher Key (16 karakter):", bg="#FFD6E8",
         font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w")
entry_key = tk.Entry(frame_in, width=40, font=("Arial", 12))
entry_key.grid(row=1, column=1, padx=8)

# OUTPUT FRAME (4 boxes)
out_frame = tk.Frame(root, bg="#FFD6E8")
out_frame.pack(padx=10, pady=6, fill="both", expand=False)

def make_labeled_text(parent, title, width=60, height=12):
    sub = tk.Frame(parent, bg="#FFD6E8")
    lbl = tk.Label(sub, text=title, bg="#FFD6E8", font=("Arial", 11, "bold"))
    lbl.pack(anchor="w")
    text = tk.Text(sub, width=width, height=height, font=("Consolas", 10))
    sb = tk.Scrollbar(sub, command=text.yview)
    text.configure(yscrollcommand=sb.set)
    text.pack(side="left", fill="both", expand=False)
    sb.pack(side="right", fill="y")
    return sub, text

left_top, out1 = make_labeled_text(out_frame, "OUT1: PLAINTEXT -> HEX ", width=48, height=12)
right_top, out2 = make_labeled_text(out_frame, "OUT2: CIPHERKEY -> HEX ", width=48, height=12)
left_bottom, out3 = make_labeled_text(out_frame, "OUT3: HASIL XOR (AddRoundKey awal)", width=48, height=12)
right_bottom, out4 = make_labeled_text(out_frame, "OUT4: K0-K10 (Pemb. Kunci)", width=48, height=12)

left_top.grid(row=0, column=0, padx=8, pady=4)
right_top.grid(row=0, column=1, padx=8, pady=4)
left_bottom.grid(row=1, column=0, padx=8, pady=4)
right_bottom.grid(row=1, column=1, padx=8, pady=4)

# printing helpers
def print_hex_matrix_to_widget(widget, mat_int, title=None):
    if title:
        widget.insert(tk.END, f"\n=== {title} ===\n")
    for r in range(4):
        line = " ".join(format(mat_int[r][c], "02X") for c in range(4))
        widget.insert(tk.END, line + "\n")

def print_hexstr_matrix_to_widget(widget, mat_hex, title=None):
    if title:
        widget.insert(tk.END, f"\n=== {title} ===\n")
    for r in range(4):
        line = " ".join(mat_hex[r][c] for c in range(4))
        widget.insert(tk.END, line + "\n")


def proses_hex():
    out1.delete("1.0", tk.END)
    out2.delete("1.0", tk.END)

    pt = entry_plain.get()
    ck = entry_key.get()

    hex_plain = text_to_hex_list(pt)
    hex_key = text_to_hex_list(ck)

    m_plain = to_matrix_rowmajor_from_hex_list(hex_plain)
    m_key = to_matrix_rowmajor_from_hex_list(hex_key)

    print_hexstr_matrix_to_widget(out1, m_plain, "PLAINTEXT (HEX) dalam Matriks 4x4 ")
    print_hexstr_matrix_to_widget(out2, m_key, "CIPHERKEY (HEX) dalam Matriks 4x4 ")

def proses_xor():
    out3.delete("1.0", tk.END)
    pt = entry_plain.get()
    ck = entry_key.get()

    hex_plain = text_to_hex_list(pt)
    hex_key = text_to_hex_list(ck)

    m_plain = to_matrix_rowmajor_from_hex_list(hex_plain)
    m_key = to_matrix_rowmajor_from_hex_list(hex_key)

    int_plain = hex_matrix_to_int_matrix(m_plain)
    int_key = hex_matrix_to_int_matrix(m_key)
    res = xor_int_matrices(int_plain, int_key)
    print_hex_matrix_to_widget(out3, int_plain, "PLAINTEXT (HEX) ")
    print_hex_matrix_to_widget(out3, int_key, "CIPHERKEY (HEX) ")
    print_hex_matrix_to_widget(out3, res, "HASIL XOR (AddRoundKey)")

def proses_keyexp():
    out4.delete("1.0", tk.END)
    ck = entry_key.get()
    hex_key = text_to_hex_list(ck)
    key_hex_mat = to_matrix_rowmajor_from_hex_list(hex_key)
    key_int_mat = hex_matrix_to_int_matrix(key_hex_mat)
    all_words = key_expansion_from_intmatrix_rowmajor(key_int_mat)

    out4.insert(tk.END, "\n=== Pembentukan K0..K10  ===\n")
    for r in range(11):
        start = r*4
        words = all_words[start:start+4]
        km = words_to_matrix_rowmajor(words)
        print_hex_matrix_to_widget(out4, km, f"K{r}")

    # store key words for potential future use (keamanan)
    out4._key_words = all_words

# Buttons frame
btn_frame = tk.Frame(root, bg="#FFD6E8")
btn_frame.pack(pady=8)

ttk.Button(btn_frame, text="Konversi ke HEX", command=proses_hex).grid(row=0, column=0, padx=8)
ttk.Button(btn_frame, text="Proses XOR", command=proses_xor).grid(row=0, column=1, padx=8)
ttk.Button(btn_frame, text="Pembentukan Kunci K0-K10", command=proses_keyexp).grid(row=0, column=2, padx=8)

root.mainloop()

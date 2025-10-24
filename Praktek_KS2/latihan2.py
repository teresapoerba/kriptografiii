import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ========== WARNA & GAYA ==========
BG_GRAD1 = "#FFD1DC"    # pink lembut
BG_GRAD2 = "#F3C4FB"    # ungu muda pastel
CARD_BG = "#FFF6FA"     # putih agak pink
BTN_COLOR = "#FF85A1"   # pink cerah
BTN_HOVER = "#FF6384"   # pink lebih gelap saat hover
TEXT_COLOR = "#4A3C58"  # ungu gelap untuk teks

# ========== WINDOW ==========
root = tk.Tk()
root.title("Kalkulator Pink Cantik 💕")
root.geometry("500x400")
root.resizable(False, False)

# ========== GRADIENT BACKGROUND ==========
canvas = tk.Canvas(root, width=500, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

for i in range(400):
    r1, g1, b1 = root.winfo_rgb(BG_GRAD1)
    r2, g2, b2 = root.winfo_rgb(BG_GRAD2)
    r = int(r1 + (r2 - r1) * i / 400) >> 8
    g = int(g1 + (g2 - g1) * i / 400) >> 8
    b = int(b1 + (b2 - b1) * i / 400) >> 8
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_line(0, i, 500, i, fill=color)

# ========== FRAME UTAMA ==========
frame = tk.Frame(root, bg=CARD_BG, bd=0, highlightthickness=0)
frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=320)

# ========== FUNGSI ==========
def hitung_tambah():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil: {a + b}")
    except ValueError:
        messagebox.showwarning("Input Error", "Masukkan angka yang valid!")

def hitung_kurang():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil.set(f"Hasil: {a - b}")
    except ValueError:
        messagebox.showwarning("Input Error", "Masukkan angka yang valid!")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    hasil.set("Hasil: -")

def keluar():
    root.destroy()

def on_enter(e): e.widget.config(bg=BTN_HOVER)
def on_leave(e): e.widget.config(bg=BTN_COLOR)

# ========== LABEL HEADER ==========
title = tk.Label(frame, text="Kalkulator Pink Cantik 💕", 
                 font=("Poppins", 16, "bold"), fg=TEXT_COLOR, bg=CARD_BG)
title.pack(pady=(15, 5))

# ========== GAMBAR ==========
try:
    img = Image.open("math.png")
    img = img.resize((70, 70))
    photo = ImageTk.PhotoImage(img)
    label_img = tk.Label(frame, image=photo, bg=CARD_BG)
    label_img.pack(pady=(0, 10))
except:
    label_img = tk.Label(frame, text="🩷", font=("Arial", 40), bg=CARD_BG)
    label_img.pack(pady=(0, 10))

# ========== INPUT ==========
tk.Label(frame, text="Angka 1:", font=("Poppins", 11), bg=CARD_BG, fg=TEXT_COLOR).pack()
entry1 = tk.Entry(frame, font=("Poppins", 11), width=20, justify="center", bd=2, relief="flat")
entry1.pack(pady=2)

tk.Label(frame, text="Angka 2:", font=("Poppins", 11), bg=CARD_BG, fg=TEXT_COLOR).pack()
entry2 = tk.Entry(frame, font=("Poppins", 11), width=20, justify="center", bd=2, relief="flat")
entry2.pack(pady=2)

# ========== HASIL ==========
hasil = tk.StringVar(value="Hasil: -")
lbl_hasil = tk.Label(frame, textvariable=hasil, font=("Poppins", 12, "bold"),
                     bg=CARD_BG, fg="#FF4F83")
lbl_hasil.pack(pady=8)

# ========== TOMBOL ==========
btn_frame = tk.Frame(frame, bg=CARD_BG)
btn_frame.pack(pady=10)

def buat_tombol(text, cmd, warna=BTN_COLOR):
    btn = tk.Button(btn_frame, text=text, command=cmd, font=("Poppins", 10, "bold"),
                    bg=warna, fg="white", width=10, relief="flat", bd=0,
                    activebackground=BTN_HOVER, cursor="hand2")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btn1 = buat_tombol("Tambah", hitung_tambah)
btn2 = buat_tombol("Kurang", hitung_kurang)
btn3 = buat_tombol("Reset", reset, warna="#FCA3B7")
btn4 = buat_tombol("Keluar", keluar, warna="#F55A8A")

btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3.grid(row=1, column=0, padx=5, pady=5)
btn4.grid(row=1, column=1, padx=5, pady=5)

# ========== JALANKAN ==========
root.mainloop()

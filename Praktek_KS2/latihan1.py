import tkinter as tk
from tkinter import messagebox
import operator

# === Fungsi Aritmatika ===
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# === Fungsi untuk tombol ===
def hitung():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operator_var.get()

        if op not in ops:
            messagebox.showwarning("Peringatan", "Pilih operator dengan benar (+, -, *, /)")
            return

        hasil = ops[op](a, b)
        label_hasil.config(
            text=f"Hasil dari {a} {op} {b} = {hasil}",
            fg="#D63384"
        )
    except ValueError:
        messagebox.showerror("Error", "Input nilai harus berupa angka!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Pembagian dengan nol tidak diperbolehkan!")

def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    operator_var.set('+')
    label_hasil.config(text="Hasil: ", fg="#4A4A4A")

def keluar():
    if messagebox.askyesno("Konfirmasi", "Apakah kamu yakin ingin keluar? 🥺"):
        root.destroy()

# === WINDOW UTAMA ===
root = tk.Tk()
root.title("🩷 Kalkulator Sederhana Cantik 🩷")
root.geometry("440x420")
root.resizable(False, False)
root.configure(bg="#FFE6F2")  # pink lembut

# === FRAME UTAMA (CARD) ===
card = tk.Frame(root, bg="#FFF0F6", bd=2, relief="ridge", padx=10, pady=10)
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=350)

# === JUDUL ===
judul = tk.Label(
    card,
    text="💗 Kalkulator Pink Cantik 💗",
    font=("Poppins", 16, "bold"),
    bg="#FFB6C1",
    fg="white",
    relief="flat",
    width=30,
    pady=8
)
judul.pack(pady=(5, 15))

# === FRAME INPUT ===
frame_input = tk.Frame(card, bg="#FFF0F6")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Nilai A :", bg="#FFF0F6", fg="#6A0572", font=("Poppins", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_input, width=14, font=("Poppins", 11), justify="center", bd=2, relief="flat")
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Nilai B :", bg="#FFF0F6", fg="#6A0572", font=("Poppins", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_input, width=14, font=("Poppins", 11), justify="center", bd=2, relief="flat")
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Operator :", bg="#FFF0F6", fg="#6A0572", font=("Poppins", 11)).grid(row=2, column=0, padx=5, pady=5)
operator_var = tk.StringVar(value='+')
menu_operator = tk.OptionMenu(frame_input, operator_var, '+', '-', '*', '/')
menu_operator.config(bg="#FFCCE5", fg="#4A004A", font=("Poppins", 10, "bold"), width=8, relief="flat", activebackground="#FF99CC")
menu_operator.grid(row=2, column=1, pady=5)

# === HASIL ===
label_hasil = tk.Label(
    card,
    text="Hasil: ",
    font=("Poppins", 12, "bold"),
    bg="#FFF0F6",
    fg="#4A4A4A"
)
label_hasil.pack(pady=10)

# === FRAME TOMBOL ===
frame_btn = tk.Frame(card, bg="#FFF0F6")
frame_btn.pack(pady=5)

def buat_tombol(text, warna_bg, warna_fg, cmd):
    return tk.Button(
        frame_btn, text=text, command=cmd,
        bg=warna_bg, fg=warna_fg,
        font=("Poppins", 10, "bold"),
        width=10, relief="flat", bd=0,
        activebackground="#FF99CC", cursor="hand2"
    )

btn_hitung = buat_tombol("Hitung", "#FF69B4", "white", hitung)
btn_reset = buat_tombol("Reset", "#FFD1DC", "#4A004A", reset)
btn_keluar = buat_tombol("Keluar", "#F06292", "white", keluar)

btn_hitung.grid(row=0, column=0, padx=8, pady=10)
btn_reset.grid(row=0, column=1, padx=8, pady=10)
btn_keluar.grid(row=0, column=2, padx=8, pady=10)

# === FOOTER ===
footer = tk.Label(
    card,
    text="✨ Dibuat oleh Teresa Purba | 2025 ✨",
    bg="#FFF0F6",
    font=("Poppins", 9, "italic"),
    fg="#A64CA6"
)
footer.pack(side="bottom", pady=5)

root.mainloop()

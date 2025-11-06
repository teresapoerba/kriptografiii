import tkinter as tk
from tkinter import messagebox, ttk


def konversi_biner():
    biner = entry_input.get().strip()
    if not biner or not all(ch in '01' for ch in biner):
        messagebox.showerror("Error", "Masukkan hanya angka biner (0 dan 1)!")
        return
    desimal = int(biner, 2)
    heksa = hex(desimal).upper()[2:]
    hasil_text.set(f"Desimal : {desimal}\nHexadesimal : {heksa}")

def konversi_oktal():
    oktal = entry_input.get().strip()
    if not oktal or not all(ch in '01234567' for ch in oktal):
        messagebox.showerror("Error", "Masukkan hanya angka oktal (0–7)!")
        return
    desimal = int(oktal, 8)
    biner = bin(desimal)[2:]
    heksa = hex(desimal).upper()[2:]
    hasil_text.set(f"Desimal : {desimal}\nBiner : {biner}\nHexadesimal : {heksa}")

def konversi_heksa():
    heksa = entry_input.get().strip().upper()
    try:
        desimal = int(heksa, 16)
        biner = bin(desimal)[2:]
        oktal = oct(desimal)[2:]
        hasil_text.set(f"Desimal : {desimal}\nBiner : {biner}\nOktal : {oktal}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan hanya angka 0–9 atau huruf A–F!")


def clear_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_menu():
    clear_frame()
    tk.Label(content_frame, text="✨ PILIH JENIS KONVERSI ✨",
             bg="#D7E8BA", fg="#2C3E50", font=("Segoe UI", 14, "bold")).pack(pady=15)

    btn1 = tk.Button(content_frame, text="Konversi Biner ke Desimal & Hexadesimal", 
                     command=show_biner, bg="#A5D6A7", fg="black", font=("Segoe UI", 10, "bold"), relief="flat", width=40)
    btn1.pack(pady=5)

    btn2 = tk.Button(content_frame, text="Konversi Oktal ke Desimal, Biner & Hexadesimal",
                     command=show_oktal, bg="#AED581", fg="black", font=("Segoe UI", 10, "bold"), relief="flat", width=40)
    btn2.pack(pady=5)

    btn3 = tk.Button(content_frame, text="Konversi Hexadesimal ke Desimal, Biner & Oktal",
                     command=show_heksa, bg="#C5E1A5", fg="black", font=("Segoe UI", 10, "bold"), relief="flat", width=40)
    btn3.pack(pady=5)

def show_biner():
    show_konversi("Biner", konversi_biner, "Masukkan bilangan biner (0 dan 1):")

def show_oktal():
    show_konversi("Oktal", konversi_oktal, "Masukkan bilangan oktal (0–7):")

def show_heksa():
    show_konversi("Hexadesimal", konversi_heksa, "Masukkan bilangan hexadesimal (0–9 atau A–F):")

def show_konversi(jenis, fungsi, label_text):
    clear_frame()

    tk.Label(content_frame, text=f"✨ KONVERSI {jenis.upper()} ✨",
             bg="#D7E8BA", fg="#2C3E50", font=("Segoe UI", 14, "bold")).pack(pady=10)
    tk.Label(content_frame, text=label_text, bg="#D7E8BA",
             fg="#2C3E50", font=("Segoe UI", 10, "bold")).pack(pady=5)

    global entry_input, hasil_text
    entry_input = tk.Entry(content_frame, font=("Consolas", 12), width=30, justify="center")
    entry_input.pack(pady=5)

    frame_btn = tk.Frame(content_frame, bg="#D7E8BA")
    frame_btn.pack(pady=10)

    tk.Button(frame_btn, text="Konversi", command=fungsi,
              bg="#81C784", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", width=12).grid(row=0, column=0, padx=5)

    tk.Button(frame_btn, text="Kembali", command=show_menu,
              bg="#FFB6B9", fg="black", font=("Segoe UI", 10, "bold"), relief="flat", width=12).grid(row=0, column=1, padx=5)

    hasil_text = tk.StringVar()
    tk.Label(content_frame, textvariable=hasil_text, bg="#D7E8BA", fg="#2C3E50", 
             font=("Consolas", 12)).pack(pady=15)


root = tk.Tk()
root.title("✨ KONVERSI BILANGAN ✨")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#D7E8BA")  


tk.Label(root, text="PROGRAM KONVERSI BILANGAN",
         bg="#D7E8BA", fg="#2C3E50", font=("Segoe UI", 16, "bold")).pack(pady=10)

content_frame = tk.Frame(root, bg="#D7E8BA")
content_frame.pack(fill="both", expand=True)

show_menu()

root.mainloop()

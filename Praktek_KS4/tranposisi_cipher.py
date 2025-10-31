def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# === Input dari user ===
plaintext = input("Masukkan plaintext: ").upper()

# Membuat aturan substitusi berdasarkan input user
aturan_substitusi = {}
jumlah_aturan = int(input("Berapa banyak huruf yang ingin disubstitusi? "))

for i in range(jumlah_aturan):
    huruf_asli = input(f"Masukkan huruf asli ke-{i+1}: ").upper()
    huruf_ganti = input(f"Masukkan huruf pengganti untuk '{huruf_asli}': ").upper()
    aturan_substitusi[huruf_asli] = huruf_ganti

# Proses enkripsi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Tampilkan hasil
print("\n=== HASIL ENKRIPSI ===")
print(f"Plaintext : {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Aturan substitusi: {aturan_substitusi}")
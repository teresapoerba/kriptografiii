# === Fungsi Substitusi Cipher ===
def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext


# === Fungsi Transposisi Cipher (4 blok) ===
def transposisi_cipher(plaintext):
    part_length = len(plaintext) // 4
    parts = [plaintext[i:i + part_length] for i in range(0, len(plaintext), part_length)]

    ciphertext = ""
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
    return ciphertext


# === Program Utama ===
# a. Input Plaintext
plaintext = input("Masukkan plaintext: ").upper()

# b. Proses Substitusi Cipher (aturan dari gambar)
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B',
    'S': 'S',
    'T': 'T',
    'O': 'O',
    'H': 'H',
    'M': 'M',
}

cipher_substitusi = substitusi_cipher(plaintext, aturan_substitusi)

# c. Proses Transposisi Cipher (4 blok)
cipher_transposisi = transposisi_cipher(cipher_substitusi)

# === Tampilkan hasil ===
print("\n=== HASIL ENKRIPSI ===")
print(f"Input Plaintext : {plaintext}")
print(f"Ciphertext Substitusi : {cipher_substitusi}")
print(f"Ciphertext Substitusi + Transposisi : {cipher_transposisi}")
import random

# Modular Exponentiation untuk menghitung perpangkatan modular
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Extended Euclid, menghitung koefisien x dan y
def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

#menghitung modular inversi saat dekripsi
def mod_inverse(a, m): 
    gcd, x, y = extended_euclid(a, m)
    return x % m

p = 467 #bilangan prima besar
g = 2   #generator
x = 127   # PRIVATE KEY
y = mod_exp(g, x, p)

public_key = (p, g, y)
private_key = x

# ENKRIPSI 
def encrypt_text(text):
    cipher = [] #menyimpan teks enkripsi
    for char in text:   #mengenkripsi setiap karakter
        m = ord(char)   #konversi karakter ke angka
        k = random.randint(2, p-2) #membuat nilai k acak agar chipertext berbeda
        c1 = mod_exp(g, k, p)
        c2 = (m * mod_exp(y, k, p)) % p
        cipher.append((c1, c2)) #simpan karakter chipper
    return cipher


# DEKRIPSI
def decrypt_text(cipher):
    result = ""
    for c1, c2 in cipher:
        s = mod_exp(c1, private_key, p)
        s_inv = mod_inverse(s, p)
        m = (c2 * s_inv) % p
        result += chr(m)
    return result

# MENU LOOP
while True:

    print("\n=== ELGAMAL CRYPTO SYSTEM ===")
    print("Public Key :", public_key)
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    menu = input("Pilih menu (1/2/3): ")

    if menu == "1":
        teks = input("Masukkan teks: ")
        ciphertext = encrypt_text(teks)
        print("\nCiphertext:")
        print(ciphertext)
        print("\nFormat dekripsi: c1,c2;c1,c2;...")

    elif menu == "2":
        print("Masukkan ciphertext format: c1,c2;c1,c2;...")
        data = input("Ciphertext: ")

        try:
            parts = data.split(";")
            cipher_list = []
            for item in parts:
                c1, c2 = item.split(",")
                cipher_list.append((int(c1), int(c2)))

            hasil = decrypt_text(cipher_list)
            print("\nHasil Dekripsi:", hasil)

        except:
            print("Format salah! Coba lagi.")

    elif menu == "3":
        print("Program selesai. Terima kasih 🙌")
        break   # <- Program keluar di sini

    else:
        print("Pilihan tidak valid.")
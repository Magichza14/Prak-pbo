# Meminta input dari user untuk batas perulangan
n = int(input("Masukkan panjang sisi persegi: "))

# perulangan untuk membuat baris sebanyak n
for i in range(n):

    # perulangan untuk mencetak "*" sebanyak n
    for j in range(n):

        # mencetak "*" sebanyak n
        print("*", end="")

    # membuat baris baru
    print()
'''
username = informatika
password = 12345678
'''

# batas percobaan
n = 3

# perulangan
while True:
    # meminta input dari user (str)
    username = input("Username: ")
    password = input("Password: ")

    # memeriksa input user
    if username == "informatika" and password == "12345678":
        print("Berhasil login!")
        # program berhenti 
        break
    else :

        # mengurangi batas percobaan
        n -= 1

        # memeriksan nilai batas percobaan
        if n > 0:
            print("Username atau password salah, coba lagi!")

        else :
            print("Percobaan habis!")

            # program berhenti
            break

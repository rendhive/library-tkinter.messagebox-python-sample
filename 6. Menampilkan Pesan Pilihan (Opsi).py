import tkinter as tk
from tkinter import messagebox

def ask_choice():
    choice = messagebox.askquestion("Pilihan", "Apakah Anda ingin melanjutkan?")
    print(f"Pilihan pengguna: {choice}")

window = tk.Tk()
window.withdraw()
ask_choice()
window.mainloop()
# Fungsi: Menampilkan dialog pilihan dengan opsi Ya atau Tidak.
# Kondisi: Ketika Anda ingin memberikan pilihan kepada pengguna.
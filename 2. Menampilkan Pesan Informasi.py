import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Informasi", "Ini adalah pesan informasi.")

window = tk.Tk()
window.withdraw()  # Menyembunyikan jendela utama
show_info()
window.mainloop()
# Fungsi: Menampilkan pesan informasi kepada pengguna.
# Kondisi: Ketika Anda ingin memberikan informasi yang penting dengan cara yang jelas
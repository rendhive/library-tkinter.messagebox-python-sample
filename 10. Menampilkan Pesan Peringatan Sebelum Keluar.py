import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        window.destroy()

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)  # Menangani penutupan jendela
window.mainloop()
# Fungsi: Menampilkan peringatan di saat keluar dari aplikasi.
# Kondisi: Ketika Anda ingin mencegah penutupan aplikasi tanpa konfirmasi.
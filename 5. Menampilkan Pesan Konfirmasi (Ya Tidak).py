import tkinter as tk
from tkinter import messagebox

def ask_confirmation():
    result = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin melanjutkan?")
    print(f"Apakah pengguna ingin melanjutkan: {result}")

window = tk.Tk()
window.withdraw()
ask_confirmation()
window.mainloop()
# Fungsi: Menampilkan dialog konfirmasi dan mendapatkan respons dari pengguna.
# Kondisi: Ketika Anda ingin meminta persetujuan dari pengguna sebelum melakukan tindakan.
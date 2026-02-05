import tkinter as tk
from tkinter import messagebox

def show_error():
    messagebox.showerror("Kesalahan", "Terjadi kesalahan!")

window = tk.Tk()
window.withdraw()
show_error()
window.mainloop()
# Fungsi: Menampilkan pesan kesalahan kepada pengguna.
# Kondisi: Ketika Anda ingin memberi tahu pengguna bahwa telah terjadi kesalahan.
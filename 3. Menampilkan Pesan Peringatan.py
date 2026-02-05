import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Peringatan", "Ini adalah pesan peringatan!")

window = tk.Tk()
window.withdraw()
show_warning()
window.mainloop()
# Fungsi: Menampilkan pesan peringatan untuk memberi tahu pengguna tentang sesuatu yang perlu diperhatikan.
# Kondisi: Ketika Anda ingin memperingatkan pengguna tentang potensi masalah.
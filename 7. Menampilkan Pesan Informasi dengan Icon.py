import tkinter as tk
from tkinter import messagebox

def show_info_with_icon():
    messagebox.showinfo("Informasi", "Ini pesan info dengan icon!", icon='info')

window = tk.Tk()
window.withdraw()
show_info_with_icon()
window.mainloop()
# Fungsi: Menampilkan pesan informasi dengan ikon.
# Kondisi: Ketika Anda ingin menambahkan visual ke pesan informasi.
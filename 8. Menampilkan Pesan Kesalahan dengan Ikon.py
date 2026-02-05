import tkinter as tk
from tkinter import messagebox

def show_error_with_icon():
    messagebox.showerror("Kesalahan", "Ini pesan kesalahan dengan ikon!", icon='error')

window = tk.Tk()
window.withdraw()
show_error_with_icon()
window.mainloop()
# Fungsi: Menampilkan pesan kesalahan dengan ikon.
# Kondisi: Ketika Anda perlu menekankan kesalahan dengan ikon visual.
import tkinter as tk
from tkinter import messagebox

def show_description():
    messagebox.showinfo("Keterangan", "Aplikasi ini dirancang untuk memberikan informasi.")

window = tk.Tk()
info_button = tk.Button(window, text="Tampilkan Keterangan", command=show_description)
info_button.pack(pady=10)
window.mainloop()
# Fungsi: Menyampaikan informasi atau keterangan tentang aplikasi.
# Kondisi: Ketika Anda ingin memberikan detail penting kepada pengguna.
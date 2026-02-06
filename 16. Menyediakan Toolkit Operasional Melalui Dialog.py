import tkinter as tk
from tkinter import messagebox

def toolkit():
    messagebox.showinfo("Toolkit", "Pilih operasi yang ingin Anda lakukan!")

window = tk.Tk()
toolkit_button = tk.Button(window, text="Buka Toolkit", command=toolkit)
toolkit_button.pack(pady=10)
window.mainloop()
# Fungsi: Memberikan panduan atau toolkit tentang apa yang dapat dilakukan dalam aplikasi.
# Kondisi: Ketika user membutuhkan arahan atau pilihan operasi dari aplikasi.
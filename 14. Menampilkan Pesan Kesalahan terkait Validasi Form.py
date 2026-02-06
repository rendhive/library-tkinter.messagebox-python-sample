import tkinter as tk
from tkinter import messagebox

def validate_input():
    if not entry.get():
        messagebox.showerror("Kesalahan", "Kolom tidak boleh kosong!")

window = tk.Tk()
entry = tk.Entry(window)
entry.pack(pady=10)

validate_button = tk.Button(window, text="Validasi Input", command=validate_input)
validate_button.pack(pady=10)
window.mainloop()
# Fungsi: Memvalidasi input dan memberikan kesalahan jika tidak valid.
# Kondisi: Ketika Anda ingin memastikan data yang diperlukan diisi.
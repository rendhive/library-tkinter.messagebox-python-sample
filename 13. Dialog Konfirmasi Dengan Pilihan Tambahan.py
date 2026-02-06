import tkinter as tk
from tkinter import messagebox

def ask_extra_option():
    result = messagebox.askquestion("Pilihan Ekstra", "Apakah Anda ingin melanjutkan?")
    if result == 'yes':
        messagebox.showinfo("Info", "Anda memilih untuk melanjutkan!")

window = tk.Tk()
button = tk.Button(window, text="Tanya Opsi Tambahan", command=ask_extra_option)
button.pack(pady=10)
window.mainloop()
# Fungsi: Menanyakan pilihan ekstra dan memberikan feedback berdasarkan hasil.
# Kondisi: Ketika Anda ingin menambahkan lebih banyak opsi pada pertanyaan.
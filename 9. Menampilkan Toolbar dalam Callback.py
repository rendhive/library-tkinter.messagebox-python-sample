import tkinter as tk
from tkinter import messagebox

def perform_action():
    messagebox.showinfo("Aksi", "Aksi telah dilakukan!")

def on_button_click():
    if messagebox.askyesno("Konfirmasi", "Apakah Anda ingin melaksanakan aksi?"):
        perform_action()

window = tk.Tk()
button = tk.Button(window, text="Lakukan Aksi", command=on_button_click)
button.pack(pady=10)
window.mainloop()
# Fungsi: Menambahkan dialog konfirmasi sebelum melakukan aksi tertentu.
# Kondisi: Ketika Anda ingin menegaskan diri sebelum melaksanakan suatu taks.
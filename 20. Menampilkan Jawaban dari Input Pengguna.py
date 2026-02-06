import tkinter as tk
from tkinter import messagebox

def respond_to_input():
    user_input = input_entry.get()
    messagebox.showinfo("Jawaban", f"Anda memasukkan: {user_input}")

window = tk.Tk()
input_entry = tk.Entry(window)
input_entry.pack(pady=10)

response_button = tk.Button(window, text="Tampilkan Jawaban", command=respond_to_input)
response_button.pack(pady=10)
window.mainloop()
# Fungsi: Menampilkan jawaban dari input pengguna melalui dialog.
# Kondisi: Ketika Anda ingin memberikan reaksi terhadap input yang diberikan pengguna.
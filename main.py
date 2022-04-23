from tkinter import *
import Crypte

# Input
print("Write something to Encrypt !")
text = input()

# Fonctions
def encrypt():
    Encrypt_entry.delete(0, END)
    Encrypt_entry.insert(0, Crypte.crypte(text))


# Window
w = Tk()
w.title("CrypteTxt")
w.geometry("420x420")
w.minsize(420, 420)
w.config(background="#10EEF5")

# Frame
frame = Frame(w, bg="#10EEF5")

label_title = Label(frame, text="Encrypt a text !", font=("Arial", 25), bg='#10EEF5', fg="#087376")
label_title.grid(row=0, column=0, sticky=W)

Encrypt_entry = Entry(frame ,font=("Arial", 20), bg='#10EEF5', fg="#087376")
Encrypt_entry.grid(row=1, column=0, sticky=W)

Encrypt_button = Button(frame, text="Encrypt !", font=("Arial", 30), bg='#10EEF5', fg="#087376", command=encrypt)
Encrypt_button.grid(row=3, column=0, sticky=W)

# Load Windows and Frame
frame.pack(expand=YES)
w.mainloop()

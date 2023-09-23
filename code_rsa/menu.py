from tkinter import *
import os
import customtkinter

def run_key_generation():
    os.system('python rsa_key_generation.py')

def run_encrypt_decrypt():
    os.system('python rsa_encrypt_decrypt.py')

def run_encrypt_decrypt_file():
    os.system('python rsa_encrypt_decrypt_file.py')

def run_sign():
    os.system('python rsa_sign.py')


window = Tk()
window.title("Projet Crypto")
window.configure(bg='white')
window.geometry("350x400")

label=Label(window, text='Projet Crypto : ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=110,y=20)

Generate = customtkinter.CTkButton(master=window, text="Generate Key",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_key_generation).place(x=100,y=80)
enc_decr = customtkinter.CTkButton(master=window, text="Encrypt & Decrypt",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_encrypt_decrypt).place(x=100,y=150)
enc_decr_file = customtkinter.CTkButton(master=window, text="Encrypt & Decrypt File",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_encrypt_decrypt_file).place(x=100,y=220)
Sign = customtkinter.CTkButton(master=window, text="Sign Verify",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_sign).place(x=100,y=290)

window.mainloop()
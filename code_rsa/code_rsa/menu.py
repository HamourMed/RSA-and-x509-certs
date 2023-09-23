from tkinter import *
import os
import customtkinter

def run_encrypt_decrypt():
    os.system('python rsa_encrypt_decrypt.py')

def run_key_generation():
    os.system('python rsa_key_generation.py')

def run_sign():
    os.system('python rsa_sign.py')


window = Tk()
window.title("Projet Crypto")
window.configure(bg='white')
window.geometry("350x400")

label=Label(window, text='Projet Crypto : ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=110,y=20)

# Generate=Button(window,text='Generate Key',width=15, height=1,command=run_key_generation).place(x=120,y=80)
# enc_decr=Button(window,text='Encrypt & Decrypt',width=15, height=1,command=run_encrypt_decrypt).place(x=120,y=150)
# Sign=Button(window,text='Sign Verify',width=15, height=1,command=run_sign).place(x=120,y=220)

Generate = customtkinter.CTkButton(master=window, text="Generate Key",text_color='#ffffff',fg_color='#1081E8',width=150, height=32,corner_radius=7,command=run_key_generation).place(x=110,y=80)
enc_decr = customtkinter.CTkButton(master=window, text="Encrypt & Decrypt",text_color='#ffffff',fg_color='#1081E8',width=150, height=32,corner_radius=7,command=run_encrypt_decrypt).place(x=110,y=150)
Sign = customtkinter.CTkButton(master=window, text="Sign Verify",text_color='#ffffff',fg_color='#1081E8',width=150, height=32,corner_radius=7,command=run_sign).place(x=110,y=220)

window.mainloop()
from tkinter import *
import os
import customtkinter
from subprocess import Popen, PIPE



def run_key_generation():
    Popen(['python', 'rsa_key_generation.py'], stdout=PIPE, stderr=PIPE)
    
def run_encrypt_decrypt():
    Popen(['python', 'rsa_encrypt_decrypt.py'], stdout=PIPE, stderr=PIPE)
    

def run_encrypt_decrypt_file():
    Popen(['python', 'rsa_encrypt_decrypt_file.py'], stdout=PIPE, stderr=PIPE)
    

def run_sign():
    Popen(['python', 'rsa_sign.py'], stdout=PIPE, stderr=PIPE)
    

def run_ca():
    Popen(['python', 'certificat_ca.py'], stdout=PIPE, stderr=PIPE)
    
def run_csr():
    Popen(['python', 'certificat_csr.py'], stdout=PIPE, stderr=PIPE)
    

def run_ver_cer():
    Popen(['python', 'certificat_verify.py'], stdout=PIPE, stderr=PIPE)
    


window = Tk()
window.title("Projet Crypto")
window.configure(bg='white')
window.geometry("700x400")

label=Label(window, text='RSA : ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=150,y=20)
Generate = customtkinter.CTkButton(master=window, text="Generate Key",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_key_generation).place(x=100,y=80)
enc_decr = customtkinter.CTkButton(master=window, text="Encrypt/Decrypt",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_encrypt_decrypt).place(x=100,y=150)
enc_decr_file = customtkinter.CTkButton(master=window, text="Encrypt/Decrypt File",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_encrypt_decrypt_file).place(x=100,y=220)
Sign = customtkinter.CTkButton(master=window, text="Sign Verify",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_sign).place(x=100,y=290)

label=Label(window, text='CERTIFICAT : ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=450,y=20)
ca = customtkinter.CTkButton(master=window, text="CA Certificat",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_ca).place(x=440,y=80)
csr = customtkinter.CTkButton(master=window, text="CSR Signature",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_csr).place(x=440,y=150)
cer_ver = customtkinter.CTkButton(master=window, text="Certificat Verification",text_color='#ffffff',fg_color='#1081E8',width=160, height=32,corner_radius=7,command=run_ver_cer).place(x=440,y=220)

window.mainloop()

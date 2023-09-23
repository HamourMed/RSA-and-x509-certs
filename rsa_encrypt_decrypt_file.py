from tkinter import *
from tkinter import filedialog as fd
import customtkinter
import rsa
import rsa_file
pub_key, prv_key = None, None
filename = None
def select_file_enc() : 
    global pub_key
    global prv_key
    global filename
    filetypes = (('All files', '*.*'),)
    filename = fd.askopenfilename(title='Encrypt file', filetype=filetypes)

def encrypt() :
    if Val.get() == 2 :
        c = rsa_file.encrypt_file_pkc1_v1_5(filename, filename+'.bin', pub_key)
    elif Val.get() == 3 :
        c = rsa_file.encrypt_file_oaep(filename, filename+'bin', pub_key)

def select_file_dec() : 
    global pub_key
    global prv_key
    filetypes = (('All files', '*.*'),)
    filename = fd.askopenfilename(title='Decrypt file', filetype=filetypes)
    

def decrypt() :
    if Val.get() == 2 :
        c = rsa_file.decrypt_file_pkc1_v1_5(filename, filename+'.dec', prv_key)
    elif Val.get() == 3 :
        c = rsa_file.decrypt_file_oaep(filename, filename+'.dec', prv_key)
    

def select_pub():
    global pub_key
    global prv_key
    filetypes = (('PEM file', '*.pem'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open Public Key', filetypes=filetypes)
    with open(filename,'r') as f :
        data=f.read()
    pub_key = rsa.pem_public_key(data)
    
def select_prv():
    global pub_key
    global prv_key
    filetypes = (('PEM file', '*.pem'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open Private Key', filetypes=filetypes)
    with open(filename,'r') as f :
        data=f.read()
    pub_key, prv_key = rsa.pem_private_key(data)

window = Tk()
window.title("RSA Encrypt/Decrypt File")
window.geometry("700x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()
Val.set(2)

label=Label(window, text='RSA Encrypt/Decrypt: ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)


Radiobutton(window,text="PKCS1",bg='white',variable=Val,value=2).place(x=130,y=60)
Radiobutton(window,text="OAEP",bg='white',variable=Val,value=3).place(x=210,y=60)

Loadprv = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_pub).place(x=480,y=60)
Loadpub = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_prv).place(x=590,y=60)

Label(window, text="Load File to Encrypt",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
customtkinter.CTkButton(master=window, text="File to encrypt",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#F1F5FF',width=150, height=80,corner_radius=7,command=select_file_enc).place(x=80,y=140)

Label(window, text="Load File to Decrypt",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
customtkinter.CTkButton(master=window, text="File to decrypt",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#F1F5FF',width=150, height=80,corner_radius=7,command=select_file_dec).place(x=80,y=260)

Encrypt = customtkinter.CTkButton(master=window, text="Encrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=encrypt).place(x=410,y=160)
Decrypt = customtkinter.CTkButton(master=window, text="Decrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=decrypt).place(x=410,y=280)

window.mainloop()
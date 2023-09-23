from tkinter import *
from tkinter import filedialog as fd
import customtkinter
import sys
import os
  
import rsa



pub_key, prv_key = None, None



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
    

    

def encrypt_text():
    global plain
    global cipher    
    if Val.get() == 1 :
        c = rsa.encrypt_raw(plain.get("1.0","end-1c").encode('utf_8'), pub_key)
    elif Val.get() == 2 :
        c = rsa.encrypt_v1_5(plain.get("1.0","end-1c").encode('utf_8'), pub_key)
    elif Val.get() == 3 :
        c = rsa.encrypt_oaep(plain.get("1.0","end-1c").encode('utf_8'), pub_key)
    cipher.delete("1.0",END)
    cipher.insert("1.0",rsa.base64.encodebytes(c).decode('utf_8'))


def decrypt_text():
    global plain
    global cipher   
    c = rsa.base64.decodebytes(cipher.get("1.0",END).replace('\n','').encode('utf_8')) 
    if Val.get() == 1 :
        m = rsa.decrypt_raw(c, prv_key)
    elif Val.get() == 2 :
        m = rsa.decrypt_v1_5(c, prv_key)
    elif Val.get() == 3 :
        m = rsa.decrypt_oaep(c, prv_key)
    plain.delete("1.0",END)
    plain.insert("1.0",m.decode('utf_8').lstrip('\x00'))


    
window = Tk()
window.title("RSA Encrypt/Decrypt")
window.geometry("700x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Encrypt/Decrypt: ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)

Radiobutton(window,text="RAW",bg='white',variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PKCS1",bg='white',variable=Val,value=2).place(x=130,y=60)
Radiobutton(window,text="OAEP",bg='white',variable=Val,value=3).place(x=210,y=60)
Val.set(2)
Loadpub = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7, command=select_pub).place(x=480,y=60)
Loadprv = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7, command=select_prv).place(x=590,y=60)

Label(window, text="Plain Text",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
plain = Text(window,borderwidth=0,background='#F1F5FF')
plain.place(x=60,y=140,width=306,height=76)

Label(window, text="Crypted Text",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
cipher = Text(window,borderwidth=0,background='#F1F5FF')
cipher.place(x=60,y=260,width=306,height=76)


Encrypt = customtkinter.CTkButton(master=window, text="Encrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=encrypt_text).place(x=410,y=160)
Decrypt = customtkinter.CTkButton(master=window, text="Decrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=decrypt_text).place(x=410,y=280)

window.mainloop()
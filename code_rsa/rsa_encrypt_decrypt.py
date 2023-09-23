from tkinter import *
from tkinter import filedialog as fd
import customtkinter
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)

print(parent_directory)
sys.path.append(parent_directory)
  
import rsa


pub_key, prv_key = rsa.keygen(b=1024)


def select_file():
    fd.askopenfilename()

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
    plain.insert("1.0",m.decode('utf_8'))


    
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
Loadprv = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_file).place(x=480,y=60)
Loadpub = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_file).place(x=590,y=60)

Label(window, text="Plain Text",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
plain = Text(window,borderwidth=0,background='#F1F5FF')
plain.place(x=60,y=140,width=306,height=76)

Label(window, text="Crypted Text",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
cipher = Text(window,borderwidth=0,background='#F1F5FF')
cipher.place(x=60,y=260,width=306,height=76)


Encrypt = customtkinter.CTkButton(master=window, text="Encrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=encrypt_text).place(x=410,y=160)
Decrypt = customtkinter.CTkButton(master=window, text="Decrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=decrypt_text).place(x=410,y=280)

window.mainloop()
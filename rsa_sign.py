from tkinter import *
from tkinter import filedialog as fd
import customtkinter
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

def sign_text():
    global plain
    global cipher   
    if Valeur.get() == 1 :
        f_hash = rsa.sha1
    else :
        f_hash = rsa.sha256 
    if Val.get() == 1 :
        c = rsa.sign_v1_5(plain.get("1.0","end-1c").encode('utf_8'), prv_key, f_hash=f_hash)
    elif Val.get() == 2 :
        c = rsa.sign_pss(plain.get("1.0","end-1c").encode('utf_8'), prv_key, f_hash=f_hash)
    cipher.delete("1.0",END)
    cipher.insert("1.0",rsa.base64.encodebytes(c).decode('utf_8'))

def Verify_text():
    global plain
    global cipher   
    c = rsa.base64.decodebytes(cipher.get("1.0",END).replace('\n','').encode('utf_8'))
    if Valeur.get() == 1 :
        f_hash = rsa.sha1
    else :
        f_hash = rsa.sha256 
    if Val.get() == 1 :
        m = rsa.verify_v1_5(c,plain.get("1.0","end-1c").encode('utf_8'), pub_key, f_hash=f_hash)
    elif Val.get() == 2 :
        m = rsa.verify_pss(c,plain.get("1.0","end-1c").encode('utf_8'), pub_key, f_hash=f_hash)
    if m :
        label.config(text="Verified : True")
    else : 
        label.config(text="Verified : False")
    


window = Tk()
window.title("RSA Sign Verify")
window.geometry("800x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()
Val.set(1)
Valeur.set(1)

label=Label(window, text='RSA Sign Verify: ',font=('roboto',13,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)
Radiobutton(window,text="PKCS1",bg='white',variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PSS",bg='white',variable=Val,value=2).place(x=130,y=60)

label=Label(window, text='Digest: ',font=('roboto',13,'bold'),fg='#0F2851',bg='white').place(x=250,y=30)
Radiobutton(window,text="SHA1",bg='white',variable=Valeur,value=1).place(x=250,y=60)
Radiobutton(window,text="SHA256",bg='white',variable=Valeur,value=2).place(x=320,y=60)

Loadpub = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_pub).place(x=480,y=60)
Loadprv = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_prv).place(x=590,y=60)

Label(window, text="Message",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
plain = Text(window,borderwidth=0,background='#F1F5FF')
plain.place(x=60,y=140,width=320,height=76)

Label(window, text="Signature",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
cipher = Text(window,borderwidth=0,background='#F1F5FF')
cipher.place(x=60,y=260,width=320,height=76)

Sign=customtkinter.CTkButton(master=window, text="Sign",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=sign_text).place(x=410,y=160)
Verify=customtkinter.CTkButton(master=window, text="Verify",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=Verify_text).place(x=410,y=280)

label = Label(window, text="Verified :",font=('roboto',12,'bold'),fg='#0F2851',bg='white')
label.place(x=590,y=280)

window.mainloop()
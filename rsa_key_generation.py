from tkinter import *
import customtkinter
import rsa
from tkinter import filedialog as fd
window = Tk()
window.title("Key Generation")
window.geometry("700x400")
window.configure(bg='white')

Val = IntVar()
Val.set(2)

def select_folder() :
    filetypes = (('PEM file', '*.pem'), ('All files', '*.*'))   

    filename = fd.asksaveasfilename(title="Save Public Key", initialfile = 'Public key.pem' ,filetypes=filetypes)
    with open(filename, 'w') as f:
        f.write(pub.get("1.0","end-1c"))

    filename = fd.asksaveasfilename(title="Save Private Key",initialfile = 'Private key.pem',  filetypes=filetypes)
    with open(filename, 'w') as f:
        f.write(prv.get("1.0","end-1c"))

def Generate_key():
    if Val.get() ==1 :
        b = 512
    elif Val.get() == 2 :
        b=1024
    elif Val.get() == 3:
        b=2048
    else :
        b=4096
    pub_key, prv_key = rsa.keygen(b=b)
    print("Done")
    prv_k=rsa.private_key_pem(pub_key[0],pub_key[1], prv_key[1], prv_key[2], prv_key[3], prv_key[4], prv_key[5], prv_key[6])
    pub_k=rsa.public_key_pem(pub_key[0], pub_key[1])
    pub.delete("1.0",END)
    pub.insert("1.0",pub_k)
    prv.delete("1.0",END)
    prv.insert("1.0",prv_k)
    
label=Label(window,text='Key Generation: ',font=('roboto',12,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)

Radiobutton(window,text="512",bg='white',variable=Val,value=1).place(x=40,y=60,width=85,height=25)
Radiobutton(window,text="1024",bg='white',variable=Val,value=2).place(x=130,y=60,width=85,height=25)
Radiobutton(window,text="2048",bg='white',variable=Val,value=3).place(x=210,y=60,width=85,height=25)
Radiobutton(window,text="4096",bg='white',variable=Val,value=4).place(x=280,y=60,width=85,height=25)

Label(window, text="Public key",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
pub=Text(window,borderwidth=0,background='#F1F5FF')
pub.place(x=60,y=140,width=306,height=76)

Label(window, text="Private key",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
prv=Text(window,borderwidth=0,background='#F1F5FF')
prv.place(x=60,y=260,width=306,height=76)

Generate = customtkinter.CTkButton(master=window, text="Generate",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=Generate_key).place(x=540,y=150)
Save = customtkinter.CTkButton(master=window, text="Save",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=select_folder).place(x=540,y=210)

window.mainloop()

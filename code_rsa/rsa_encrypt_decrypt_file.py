from tkinter import *
from tkinter import filedialog as fd
import customtkinter

prv_key_path=''
public_key_path=''

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    
    return filename

def select_pub():
    public_key_path=select_file()

def select_prv():
    prv_key_path=select_file()

window = Tk()
window.title("RSA Encrypt/Decrypt File")
window.geometry("700x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Encrypt/Decrypt: ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)

Radiobutton(window,text="RAW",bg='white',variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PKCS1",bg='white',variable=Val,value=2).place(x=130,y=60)
Radiobutton(window,text="OAEP",bg='white',variable=Val,value=3).place(x=210,y=60)

Loadprv = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_pub).place(x=480,y=60)
Loadpub = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_prv).place(x=590,y=60)

Label(window, text="Load File to Encrypt",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
customtkinter.CTkButton(master=window, text="File to encrypt",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#F1F5FF',width=150, height=80,corner_radius=7,command=select_file).place(x=80,y=140)

Label(window, text="Load File to Decrypt",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
customtkinter.CTkButton(master=window, text="File to decrypt",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#F1F5FF',width=150, height=80,corner_radius=7,command=select_file).place(x=80,y=260)

Encrypt = customtkinter.CTkButton(master=window, text="Encrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=410,y=160)
Decrypt = customtkinter.CTkButton(master=window, text="Decrypt",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=410,y=280)

window.mainloop()
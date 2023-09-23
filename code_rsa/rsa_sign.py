from tkinter import *
from tkinter import filedialog as fd
import customtkinter

def select_file():
    fd.askopenfilename()

window = Tk()
window.title("RSA Sign Verify")
window.geometry("800x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Sign Verify: ',font=('roboto',13,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)
Radiobutton(window,text="PKCS1",bg='white',variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PSS",bg='white',variable=Val,value=2).place(x=130,y=60)

label=Label(window, text='Digest: ',font=('roboto',13,'bold'),fg='#0F2851',bg='white').place(x=250,y=30)
Radiobutton(window,text="SHA1",bg='white',variable=Val,value=3).place(x=250,y=60)
Radiobutton(window,text="SHA256",bg='white',variable=Val,value=4).place(x=320,y=60)

Loadprv = customtkinter.CTkButton(master=window, text="Load Public Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_file).place(x=480,y=60)
Loadpub = customtkinter.CTkButton(master=window, text="Load Private Key",text_color='#ffffff',font=('roboto',9,'bold'),fg_color='#1081E8',width=95, height=30,corner_radius=7,command=select_file).place(x=590,y=60)

Label(window, text="Message",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
Entry(window,borderwidth=0,background='#F1F5FF').place(x=60,y=140,width=320,height=76)

Label(window, text="Signature",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
Entry(window,borderwidth=0,background='#F1F5FF').place(x=60,y=260,width=320,height=76)

Sign=customtkinter.CTkButton(master=window, text="Sign",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=410,y=160)
Verify=customtkinter.CTkButton(master=window, text="Verify",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=410,y=280)

Label(window, text="Verified :",font=('roboto',12,'bold'),fg='#0F2851',bg='white').place(x=590,y=280)

window.mainloop()
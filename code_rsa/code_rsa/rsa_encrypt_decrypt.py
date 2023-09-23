from tkinter import *
from tkinter import filedialog as fd

def select_file():
    fd.askopenfilename()

window = Tk()
window.title("RSA Encrypt/Decrypt")
window.geometry("700x400")

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Encrypt/Decrypt: ',font=('times',15,'bold')).place(x=60,y=30)

Radiobutton(window,text="RAW",variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PKCS1",variable=Val,value=2).place(x=130,y=60)
Radiobutton(window,text="OAEP",variable=Val,value=3).place(x=210,y=60)

Loadprv=Button(window,text='Load Public Key',width=12, height=1,command=select_file).place(x=480,y=60)
Loadpub=Button(window,text='Load Private Key',width=12, height=1,command=select_file).place(x=590,y=60)

Label(window, text="Plain Text",font=('times',15,'bold')).place(x=60,y=110)
Entry(window).place(x=60,y=140,width=306,height=76)

Label(window, text="Crypted Text",font=('times',15,'bold')).place(x=60,y=230)
Entry(window).place(x=60,y=260,width=306,height=76)

Encrypt=Button(window,text='Encrypt',width=10, height=1).place(x=410,y=160)
Decrypt=Button(window,text='Decrypt',width=10, height=1).place(x=410,y=280)

window.mainloop()
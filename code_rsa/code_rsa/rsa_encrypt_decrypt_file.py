from tkinter import *
from tkinter import filedialog as fd

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

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Encrypt/Decrypt: ',font=('times',15,'bold')).place(x=60,y=30)

Radiobutton(window,text="RAW",variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PKCS1",variable=Val,value=2).place(x=130,y=60)
Radiobutton(window,text="OAEP",variable=Val,value=3).place(x=210,y=60)

Loadprv=Button(window,text='Load Public Key',width=12, height=1,command=select_pub).place(x=480,y=60)
Loadpub=Button(window,text='Load Private Key',width=12, height=1,command=select_prv).place(x=590,y=60)

Label(window, text="Load File to Encrypt",font=('times',15,'bold')).place(x=60,y=110)
Button(window,text='File to encrypt',width=10, height=1,command=select_file).place(x=60,y=140,width=306,height=76)

Label(window, text="Load File to Decrypt",font=('times',15,'bold')).place(x=60,y=230)
Button(window,text='File to decrypt',width=10, height=1,command=select_file).place(x=60,y=260,width=306,height=76)

Encrypt=Button(window,text='Encrypt',width=10, height=1).place(x=410,y=160)
Decrypt=Button(window,text='Decrypt',width=10, height=1).place(x=410,y=280)

window.mainloop()
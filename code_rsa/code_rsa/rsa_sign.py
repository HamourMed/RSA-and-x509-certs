from tkinter import *
from tkinter import filedialog as fd

def select_file():
    fd.askopenfilename()

window = Tk()
window.title("RSA Sign Verify")
window.geometry("800x400")

Val = IntVar()
Valeur = IntVar()

label=Label(window, text='RSA Sign Verify: ',font=('times',15,'bold')).place(x=60,y=30)
Radiobutton(window,text="PKCS1",variable=Val,value=1).place(x=60,y=60)
Radiobutton(window,text="PSS",variable=Val,value=2).place(x=130,y=60)

label=Label(window, text='Digest: ',font=('times',15,'bold')).place(x=250,y=30)
Radiobutton(window,text="SHA1",variable=Val,value=3).place(x=250,y=60)
Radiobutton(window,text="SHA256",variable=Val,value=4).place(x=320,y=60)

Loadprv=Button(window,text='Load Public Key',width=12, height=1,command=select_file).place(x=490,y=60)
Loadpub=Button(window,text='Load Private Key',width=12, height=1,command=select_file).place(x=600,y=60)

Label(window, text="Message",font=('times',15,'bold')).place(x=60,y=110)
Entry(window).place(x=60,y=140,width=320,height=76)

Label(window, text="Signature",font=('times',15,'bold')).place(x=60,y=230)
Entry(window).place(x=60,y=260,width=320,height=76)

Sign=Button(window,text='Sign',width=10, height=1).place(x=410,y=160)
Verify=Button(window,text='Verify',width=10, height=1).place(x=410,y=280)

Label(window, text="Verified :",font=('times',15,'bold')).place(x=590,y=280)

window.mainloop()
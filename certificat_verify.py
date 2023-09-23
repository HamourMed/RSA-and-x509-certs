from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog as fd
import customtkinter
import rsa
import x509
cert= None 
ca = None
def select_cert():
    global cert
    filetypes = (('CRT file', '*.crt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open Certificate', filetypes=filetypes)
    
    cert = x509.open_cert(filename)
    

def select_CA():
    global ca
    filetypes = (('CRT file', '*.crt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open CA Certificate', filetypes=filetypes)
    
    ca = x509.open_cert(filename)
    
def verifier():
    global ca
    global cert
    if x509.verifier_cert(cert, ca):
        label.config(text = 'Certificate Verified ')
    else :        
        label.config(text = 'Certificate Not Verified ')
     
window = Tk()
window.title("Certificate Signing Request Generation")
window.geometry("550x500")
window.configure(bg='white')

Label(window, text='Verify Certificate with CA : ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=30,y=20)


Loadcert = customtkinter.CTkButton(master=window, text="Load Certificate",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#ffffff',border_width=1,border_color='#0F2851',width=200, height=80,corner_radius=7,command=select_cert)
Loadcert.place(x=140,y=140)
LoadCA = customtkinter.CTkButton(master=window, text="Load CA Certificate",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#ffffff',border_width=1,border_color='#0F2851',width=200, height=80,corner_radius=7, command=select_CA)
LoadCA.place(x=140,y=260)

Generate = customtkinter.CTkButton(master=window, text="Verify",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=verifier ).place(x=446,y=417)
label = Label(window, text="",font=('roboto',12,'bold'),fg='#0F2851',bg='white')
label.place(x=120,y=417)

window.mainloop()
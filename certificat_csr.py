from datetime import datetime, timedelta
from tkinter import *
from tkinter import filedialog as fd
import customtkinter
import rsa
import x509

issuer_name= None

pub_key, prv_key = None, None


def select_cert():
    global issuer_name
    filetypes = (('CRT file', '*.crt'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open CA Certificate', filetypes=filetypes)
    
    issuer_name = x509.open_cert(filename)
    
    issuer_name=(str(issuer_name[0][2][0][0][1]), str(issuer_name[0][2][1][0][1]), str(issuer_name[0][2][2][0][1]), str(issuer_name[0][2][3][0][1]), str(issuer_name[0][2][4][0][1]), str(issuer_name[0][2][5][0][1]))
     

def generer() :

    global cert
    global issuer_name

    serial_number = '123456789'
    subject_name = (C.get(), S.get(), L.get(), O.get(), OU.get(), CN.get())
    date = datetime.utcnow()
    date = (date, date+timedelta(days=365))
    cert = x509.generate_cert(serial_number, issuer_name, date, subject_name, pub_key, prv_key )
    
    label.config(text='Certificate generated')

def save() :
    filetypes = (('CRT file', '*.crt'), ('All files', '*.*'))  

    filename = fd.asksaveasfilename(title="Save Public Key", initialfile = 'ServCert.crt' ,filetypes=filetypes)
    x509.save_cert(filename, cert)

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
    _, prv_key = rsa.pem_private_key(data)

window = Tk()
window.title("Certificate Signing Request Generation")
window.geometry("550x500")
window.configure(bg='white')

Label(window, text='CSR Details: ',font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=30,y=20)

Label(window, text="Common Name:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=70)
CN = Entry(window,borderwidth=0,background='#F1F5FF')
CN.place(x=140,y=67,width=306,height=30)

Label(window, text="Organization:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=120)
O = Entry(window,borderwidth=0,background='#F1F5FF')
O.place(x=140,y=117,width=306,height=30)

Label(window, text="Department:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=170)
OU = Entry(window,borderwidth=0,background='#F1F5FF')
OU.place(x=140,y=167,width=306,height=30)

Label(window, text="City:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=220)
L = Entry(window,borderwidth=0,background='#F1F5FF')
L.place(x=140,y=217,width=306,height=30)

Label(window, text="State/Provence:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=270)
S = Entry(window,borderwidth=0,background='#F1F5FF')
S.place(x=140,y=267,width=306,height=30)

Label(window, text="Country:",font=('roboto',10),fg='#0F2851',bg='white').place(x=40,y=320)
C = Entry(window,borderwidth=0,background='#F1F5FF')
C.place(x=140,y=317,width=306,height=30)

Loadpub = customtkinter.CTkButton(master=window, text="Load Public Key Server",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#ffffff',border_width=1,border_color='#0F2851',width=140, height=30,corner_radius=7,command=select_pub)
Loadpub.place(x=50,y=367)
Loadprv = customtkinter.CTkButton(master=window, text="Load CA Private Key",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#ffffff',border_width=1,border_color='#0F2851',width=140, height=30,corner_radius=7,command=select_prv)
Loadprv.place(x=210,y=367)
Loadcert = customtkinter.CTkButton(master=window, text="Load CA Certificate",text_color='#0F2851',font=('roboto',9,'bold'),fg_color='#ffffff',border_width=1,border_color='#0F2851',width=140, height=30,corner_radius=7,command=select_cert)
Loadcert.place(x=370,y=367)

Generate = customtkinter.CTkButton(master=window, text="Generate",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command=generer).place(x=446,y=417)
label = Label(window, text="",font=('roboto',12,'bold'),fg='#0F2851',bg='white')
label.place(x=120,y=417)
save = customtkinter.CTkButton(master=window, text="Save",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7, command= save).place(x=346,y=417)

window.mainloop()
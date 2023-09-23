from tkinter import *
import customtkinter

window = Tk()
window.title("Key Generation")
window.geometry("700x400")
window.configure(bg='white')

Val = IntVar()
Valeur = IntVar()

label=Label(window,text='Key Generation: ',font=('roboto',12,'bold'),fg='#0F2851',bg='white').place(x=60,y=30)

Radiobutton(window,text="512",bg='white',variable=Val,value=1).place(x=40,y=60,width=85,height=25)
Radiobutton(window,text="1024",bg='white',variable=Val,value=2).place(x=130,y=60,width=85,height=25)
Radiobutton(window,text="2048",bg='white',variable=Val,value=3).place(x=210,y=60,width=85,height=25)
Radiobutton(window,text="4096",bg='white',variable=Val,value=4).place(x=280,y=60,width=85,height=25)

Label(window, text="Public key",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=110)
Entry(window,borderwidth=0,background='#F1F5FF').place(x=60,y=140,width=306,height=76)

Label(window, text="Private key",font=('roboto',15,'bold'),fg='#0F2851',bg='white').place(x=60,y=230)
Entry(window,borderwidth=0,background='#F1F5FF').place(x=60,y=260,width=306,height=76)

Generate = customtkinter.CTkButton(master=window, text="Generate",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=540,y=150)
Save = customtkinter.CTkButton(master=window, text="Save",text_color='#ffffff',font=('roboto',10,'bold'),fg_color='#1081E8',width=80, height=32,corner_radius=7).place(x=540,y=210)

window.mainloop()

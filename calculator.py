import tkinter
from tkinter import *

window=Tk()
window.title("CALCULATOR")
window.geometry("570x600")
window.resizable(0,0)
window.configure(bg= "#17161b")

eq=" "

resultl=Label(window,width=40,height=2,text="", font=("times",30))
resultl.pack()

def show(val):
    global eq
    eq=eq+val
    resultl.configure(text=eq)
def clear():
    global eq
    eq=" "
    resultl.configure(text=eq)
def result():
    global eq
    r= ""
    if eq!= "" :
        try :
            r=eval(eq)
        except :
            r="error"
            eq= ""
    resultl.configure(text=r)

Button(window,text="C",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(window,text="(",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("(")).place(x=150,y=100)
Button(window,text=")",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(")")).place(x=290,y=100)
Button(window,text="/",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=430,y=100)
Button(window,text="7",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=200)
Button(window,text="8",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=200)
Button(window,text="9",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=200)
Button(window,text="*",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=200)
Button(window,text="4",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=300)
Button(window,text="5",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=300)
Button(window,text="6",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=300)
Button(window,text="-",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=300)
Button(window,text="1",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=400)
Button(window,text="2",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=400)
Button(window,text="3",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=400)
Button(window,text="+",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=400)
Button(window,text="0",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=500)
Button(window,text=".",width=5, height=1,font=("times",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=150,y=500)
Button(window,text="=",width=11, height=3,font=("times",30,"bold"),bd=1,fg="#fff",bg="#f76623",command=lambda: result()).place(x=290,y=500)



window.mainloop()

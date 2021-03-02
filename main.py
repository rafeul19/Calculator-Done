import tkinter

from tkinter import *

from tkinter import messagebox



val = ""

A = 0

operator = ""


def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)





def btn_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)




def btn_min_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)



def btn_mult_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)




def btn_div_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)



def btn_c_isclicked():
    global A
    global operator
    global val
    A = 0
    operator = ""
    val = ""
    data.set(val)



def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        B = int((val2.split("+")[1]))
        C = A + B
        data.set(C)
        val = str(C)

    elif operator == "-":
        B = int((val2.split("-")[1]))
        C = A - B
        data.set(C)
        val = str(C)

    elif operator == "*":
        B = int((val2.split("*")[1]))
        C = A * B
        data.set(C)
        val = str(C)

    elif operator == "/":
        B = int((val2.split("/")[1]))
        if B == 0 :
            messagebox.showerror("Error","Divisible by 0 not allowed.")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / B)
            data.set(C)
            val = str(C)


root = tkinter.Tk()
root.geometry("350x600+300+300")
root.resizable(0, 0)
root.title("Math Calculator")

data = StringVar()
lbl = Label(
    root,
    text="LABEL",
    anchor=SE,
    font=("Roboto", 30),
    textvariable=data,
    background="#48cae4",
    fg="#f72585"
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="#fca311")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text="1",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked

)
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_plus_isclicked
)
btnplus.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text="4",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked

)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked

)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked

)
btn6.pack(side=LEFT, expand=True, fill="both")

btnminus = Button(
    btnrow2,
    text="-",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_min_isclicked
)
btnminus.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow3,
    text="7",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked

)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked

)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked

)
btn9.pack(side=LEFT, expand=True, fill="both")

btnmult = Button(
    btnrow3,
    text="*",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_mult_isclicked

)
btnmult.pack(side=LEFT, expand=True, fill="both")

btnc = Button(
    btnrow4,
    text="C",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_c_isclicked
)
btnc.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked

)
btn0.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=result
)
btnequal.pack(side=LEFT, expand=True, fill="both")

btndiv = Button(
    btnrow4,
    text="/",
    font=("Roboto", 30),
    relief=GROOVE,
    border=0,
    command=btn_div_isclicked

)
btndiv.pack(side=LEFT, expand=True, fill="both")
root.mainloop()
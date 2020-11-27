# Bank Management System

import os
import random
from tkinter import *
from tkinter import messagebox
from tkinter import font
location = "Data\\"
root = Tk()
root.title("Alpha Bank")


def write(f, l):
    f.seek(0)
    f.truncate()
    f.writelines(l)


def ca(ac_no, pin, re_pin, name, open_bal):
    if int(pin) == int(re_pin):
        details.append(pin + "\n")
        details.append(name + "\n")
        details.append(open_bal + "\n")
        details.append("Opening Balance: Rs" + details[3])
        file = open("%s%s.txt" % (location, str(ac_no)), "w")
        file.writelines(details)
        file.close()
        messagebox.showinfo("Account Created", "Account created Successfully!")
    else:
        messagebox.showwarning("Different PIN", "PINs entered are not same.\nTry Again.")
    create.destroy()


def create_account():
    global create, details
    details = []
    create = Toplevel()
    create.title("Alpha Bank")
    ac_no = random.randint(111111111111, 999999999999)
    while os.path.isfile("%s%s.txt" % (location, str(ac_no))):
        ac_no = random.randint(111111111111, 999999999999)
    Label(create, text="Account No.: " + str(ac_no)).grid(row=0, column=0, columnspan=2)
    details.append(str(ac_no) + "\n")
    Label(create, text="PIN:").grid(row=1, column=0)
    pin = Entry(create, show="*")
    pin.grid(row=1, column=1)
    Label(create, text="Re-Enter:").grid(row=2, column=0)
    re_pin = Entry(create, show="*")
    re_pin.grid(row=2, column=1)
    Label(create, text="Name:").grid(row=3, column=0)
    name = Entry(create)
    name.grid(row=3, column=1)
    Label(create, text="Opening Balance: Rs").grid(row=4, column=0)
    open_bal = Entry(create)
    open_bal.grid(row=4, column=1)
    Button(create, text="Proceed", command=lambda: ca(ac_no, pin.get(), re_pin.get(), name.get(), open_bal.get()), padx=32).grid(row=5, column=0)
    Button(create, text="Exit", command=create.destroy, padx=48).grid(row=5, column=1)


def tm(ac_no, t_ac, pin, amt):
    if os.path.isfile("%s%s.txt" % (location, ac_no)) and os.path.isfile("%s%s.txt" % (location, t_ac)):
        file = open("%s%s.txt" % (location, ac_no), "r+")
        details = file.readlines()
        if int(details[1]) == int(pin):
            t_file = open("%s%s.txt" % (location, t_ac), "r+")
            t_details = t_file.readlines()
            if (int(details[3]) - int(amt)) < 0:
                messagebox.showwarning("Incorrect Withdrawal Amount", "Incorrect Withdrawal Amount.\nTry Again.")
            else:
                details.append("Debited(AC: " + t_ac + "): Rs" + str(amt) + "\n")
                details[3] = str(int(details[3]) - int(amt)) + "\n"
                write(file, details)
                t_details.append("Credited(AC: " + ac_no + "): Rs" + str(amt) + "\n")
                t_details[3] = str(int(t_details[3]) + int(amt)) + "\n"
                write(t_file, t_details)
                messagebox.showinfo("Money Transferred", "Money Transferred Successfully!")
            t_file.close()
        else:
            messagebox.showwarning("Incorrect PIN", "Incorrect PIN.\nTry Again.")
        file.close()
    else:
        messagebox.showwarning("Incorrect Card No", "Incorrect Card Number.\nTry Again.")
    trans.destroy()


def transfer_money():
    global trans
    trans = Toplevel()
    trans.title("Alpha Bank")
    Label(trans, text="Your Card No.:").grid(row=0, column=0)
    ac_no = Entry(trans)
    ac_no.grid(row=0, column=1)
    Label(trans, text="Receiver's Card No.:").grid(row=1, column=0)
    t_ac = Entry(trans)
    t_ac.grid(row=1, column=1)
    Label(trans, text="Your PIN:").grid(row=2, column=0)
    pin = Entry(trans, show="*")
    pin.grid(row=2, column=1)
    Label(trans, text="Amount: Rs").grid(row=3, column=0)
    amt = Entry(trans)
    amt.grid(row=3, column=1)
    Button(trans, text="Proceed", command=lambda: tm(ac_no.get(), t_ac.get(), pin.get(), amt.get()), padx=32).grid(row=4, column=0)
    Button(trans, text="Exit", command=trans.destroy, padx=48).grid(row=4, column=1)


def cla(ac_no, pin):
    if os.path.isfile("%s%s.txt" % (location, ac_no)):
        file = open("%s%s.txt" % (location, ac_no), "r")
        details = file.readlines()
        file.close()
        if int(details[1]) == int(pin):
            os.remove("%s%s.txt" % (location, ac_no))
            messagebox.showinfo("Account Closed", "Account Closed Successfully!")
        else:
            messagebox.showwarning("Incorrect PIN", "Incorrect PIN.\nTry Again.")
    else:
        messagebox.showwarning("Incorrect Card No", "Incorrect Card Number.\nTry Again.")
    close.destroy()


def close_account():
    global close
    close = Toplevel()
    close.title("Alpha Bank")
    Label(close, text="Card No.:").grid(row=0, column=0)
    ac_no = Entry(close)
    ac_no.grid(row=0, column=1)
    Label(close, text="PIN:").grid(row=1, column=0)
    pin = Entry(close, show="*")
    pin.grid(row=1, column=1)
    Button(close, text="Proceed", command=lambda: cla(ac_no.get(), pin.get()), padx=32).grid(row=2, column=0)
    Button(close, text="Exit", command=close.destroy, padx=48).grid(row=2, column=1)


Label(root, text="Welcome to Alpha Bank!", font=font.Font(size=22)).grid(row=0, column=0, columnspan=2)
Button(root, text="Create Account", command=create_account, padx=30).grid(row=1, column=0)
Button(root, text="Transfer Money", command=transfer_money, padx=30).grid(row=1, column=1)
Button(root, text="Close Account", command=close_account, padx=33).grid(row=2, column=0)
Button(root, text="Exit", command=root.destroy, padx=63).grid(row=2, column=1)
root.mainloop()

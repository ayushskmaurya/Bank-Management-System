# ATM Management System

from tkinter import *
from tkinter import messagebox
from tkinter import font
location = "Data\\"
root = Tk()
root.title("Alpha ATM")


def write():
    file.seek(0)
    file.truncate()
    file.writelines(details)


def close():
    file.close()
    ac_no.delete(0, END)
    pin.delete(0, END)


def dm(amt):
    details.append("Deposit: Rs" + str(amt) + "\n")
    details[3] = str(int(details[3]) + int(amt)) + "\n"
    write()
    messagebox.showinfo("Money Deposited", "Money Deposited Successfully!")
    dep.destroy()
    home.destroy()
    close()


def deposit_money():
    global dep
    dep = Toplevel()
    dep.title("Alpha ATM")
    Label(dep, text="Deposited: Rs").grid(row=0, column=0)
    amt = Entry(dep)
    amt.grid(row=0, column=1)
    Button(dep, text="Proceed", command=lambda: dm(amt.get()), padx=40).grid(row=1, column=0)
    Button(dep, text="Exit", command=dep.destroy, padx=50).grid(row=1, column=1)


def wm(amt):
    if (int(details[3]) - int(amt)) < 0:
        messagebox.showwarning("Incorrect Withdrawal Amount", "Incorrect Withdrawal Amount.\nTry Again.")
    else:
        details.append("Withdraw: Rs" + str(amt) + "\n")
        details[3] = str(int(details[3]) - int(amt)) + "\n"
        write()
        messagebox.showinfo("Money Withdrawn", "Money Withdrawn Successfully!")
    wid.destroy()
    home.destroy()
    close()


def withdraw_money():
    global wid
    wid = Toplevel()
    wid.title("Alpha ATM")
    Label(wid, text="Amount: Rs").grid(row=0, column=0)
    amt = Entry(wid)
    amt.grid(row=0, column=1)
    Button(wid, text="Proceed", command=lambda: wm(amt.get()), padx=40).grid(row=1, column=0)
    Button(wid, text="Exit", command=wid.destroy, padx=50).grid(row=1, column=1)


def balanced_amount():
    messagebox.showinfo("Balanced Amount", "Balanced Amount: Rs" + details[3])
    close()


def ast():
    acs.destroy()
    home.destroy()
    close()


def account_statement():
    global acs
    acs = Toplevel()
    acs.title("Alpha ATM")
    j = 0
    for i in details:
        if j > 3:
            Label(acs, text=i).pack()
        j += 1
    Button(acs, text="Exit", command=ast).pack()


def cp(o_pin, n_pin, r_pin):
    if int(details[1]) == int(o_pin):
        if int(n_pin) == int(r_pin):
            details[1] = n_pin + "\n"
            write()
            messagebox.showinfo("PIN Changed", "PIN Changed Successfully!")
        else:
            messagebox.showwarning("Different PIN", "PINs entered are not same.\nTry Again.")
    else:
        messagebox.showwarning("Incorrect PIN", "Incorrect PIN.\nTry Again.")
    pn.destroy()
    home.destroy()
    close()


def change_pin():
    global pn
    pn = Toplevel()
    pn.title("Alpha ATM")
    Label(pn, text="Old PIN:").grid(row=0, column=0)
    o_pin = Entry(pn, show="*")
    o_pin.grid(row=0, column=1)
    Label(pn, text="New PIN:").grid(row=1, column=0)
    n_pin = Entry(pn, show="*")
    n_pin.grid(row=1, column=1)
    Label(pn, text="Re-Enter:").grid(row=2, column=0)
    r_pin = Entry(pn, show="*")
    r_pin.grid(row=2, column=1)
    Button(pn, text="Proceed", command=lambda: cp(o_pin.get(), n_pin.get(), r_pin.get()), padx=40).grid(row=3, column=0)
    Button(pn, text="Exit", command=pn.destroy, padx=50).grid(row=3, column=1)


def atm():
    try:
        global home, file, details
        file = open("%s%s.txt" % (location, ac_no.get()), "r+")
        details = file.readlines()
        if int(details[1]) == int(pin.get()):
            home = Toplevel()
            home.title("Alpha ATM")
            Button(home, text="Deposit Money", command=deposit_money, padx=25).grid(row=0, column=0)
            Button(home, text="Withdraw Money", command=withdraw_money, padx=17).grid(row=0, column=1)
            Button(home, text="Balanced Amount", command=balanced_amount, padx=17).grid(row=1, column=0)
            Button(home, text="Account Statement", command=account_statement, padx=12).grid(row=1, column=1)
            Button(home, text="Change PIN", command=change_pin, padx=33).grid(row=2, column=0)
            Button(home, text="Exit", command=home.destroy, padx=54).grid(row=2, column=1)
        else:
            messagebox.showwarning("Incorrect PIN", "Incorrect PIN.\nTry Again.")
            close()
    except FileNotFoundError:
        messagebox.showwarning("Incorrect Card No", "Incorrect Card Number.\nTry Again.")


Label(root, text="Welcome to Alpha ATM!", font=font.Font(size=22)).grid(row=0, column=0, columnspan=2)
Label(root, text="Card No.:").grid(row=1, column=0)
ac_no = Entry(root)
ac_no.grid(row=1, column=1)
Label(root, text="PIN:").grid(row=2, column=0)
pin = Entry(root, show="*")
pin.grid(row=2, column=1)
Button(root, text="Proceed", command=atm, padx=40).grid(row=3, column=0)
Button(root, text="Exit", command=root.destroy, padx=50).grid(row=3, column=1)
root.mainloop()

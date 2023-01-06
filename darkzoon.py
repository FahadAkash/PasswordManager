#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.3
#  in conjunction with Tcl version 8.6
#    Jun 24, 2020 07:20:16 AM EDT  platform: Linux

import sys
import easygui
import os
from tkinter import messagebox
from encoder import vp_start_gui_encode
from decoder import vp_start_gui_decode
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import nnew_support

def encoder():
    sound_button()
    vp_start_gui_encode()

def decoder():
    sound_button()
    vp_start_gui_decode()

def sound_button():
    pass

def appendNew(username,password,website):
        file = open('info.txt','a')
        UserName = username
        passwordd = password
        website = website
        #main_password = input("Enter Your Main Password To Encrypt")
        username ="UserName: "+ UserName + "\n"
        pwd = "Number: " + passwordd + "\n"
        web = "Website: " + website + "\n"
    
        file.write("..................................\n")
        file.write(username)
        file.write(pwd)
        file.write(web)
        file.write(".....................................\n")
        file.close()


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    nnew_support.set_Tk_var()
    top = Mainpage (root)
    nnew_support.init(root, top)
    root.mainloop()

w = None
def fileshow():
    if os.path.isfile('info.fahadakash') == False:
        messagebox.showwarning("file not found",'info.fahadakash not found')
    else:
        with open('info.fahadakash','rb') as f:
            content = f.read()
        text = 'Password managers offer greater security and convenience for the use of passwords to access online services. Greater security is achieved principally through the capability of most password manager applications to generate unique, long, complex, easily changed passwords for all online accounts and the secure encrypted storage of those passwords either through a local or cloud-based vault. Greater convenience is provided by the use of a single master password to access the password vault rather than attempting to memorize different passwords for all accounts. Most password manager applications offer additional capabilities that enhance both convenience and security such as storage of credit card and frequent flyer information and autofill functionality. '
        easygui.codebox(msg=text,title="password manager",text=content.decode())
        info_fahadakash = messagebox.askquestion("Delete info.fahadakash","Do You Wana Remvoe info.fahadakash")
        if info_fahadakash == 'yes':
            os.remove('info.fahadakash')
            messagebox.showinfo("file Removed","info.fahadakash remove sucessfully :)")
        else:
            messagebox.showwarning('Delete file','info.fahadakash file must delete when your work finished')

def create_Mainpage(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Mainpage(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    nnew_support.set_Tk_var()
    top = Mainpage (w)
    nnew_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Mainpage():
    global w
    w.destroy()
    w = None

class Mainpage:
    def passwordmanager(self):
        sound_button()
        username = self.email.get()
        password = self.password.get()
        website = self.website.get()
        if username == "" and password == "":
            #tkMessageBox.showwarning("Not Valid User","Please Enter Valid Info :-)")
            messagebox.showwarning("Not Valid User","Please Enter Valid Info :-)")
        else:
            #time.sleep(3)
            #print(filelocation)
            appendNew(username,password,website)
            messagebox.showinfo("Complete","Info Saved Complete Check info.txt")
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("947x512+290+123")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Password Manager")
        top.configure(borderwidth="10")
        top.configure(background="#d83253")
        top.configure(cursor="arrow")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#d83253',fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Show Info")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                font="TkMenuFont",
                foreground="#000000",
                label="Password Show")
        self.sub_menu12 = tk.Menu(top,tearoff=0)
        self.sub_menu.add_cascade(menu=self.sub_menu12,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                font="TkMenuFont",
                foreground="#d83253",
                label="More Show")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                command=encoder,
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Encoder")
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                command=decoder,
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Decoder")
        self.menubar.add_separator(
                background="#d9d9d9")
        
        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Info Show",
                command=fileshow)

        self.menubar.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d83253",
                compound="left",
                font="TkMenuFont",
                foreground="#000000",
                label="Exit",
                command=exit)

        self.email = tk.Entry(top)
        self.email.place(relx=0.393, rely=0.156,height=33, relwidth=0.27)
        self.email.configure(background="#36d7ff")
        self.email.configure(font="TkFixedFont")
        self.email.configure(selectbackground="#c4c4c4")

        self.website = tk.Entry(top)
        self.website.place(relx=0.393, rely=0.268,height=33, relwidth=0.27)
        self.website.configure(background="#12d7ff")
        self.website.configure(font="TkFixedFont")
        self.website.configure(selectbackground="#c4c4c4")

        self.password = tk.Entry(top)
        self.password.place(relx=0.393, rely=0.379,height=33, relwidth=0.27)
        self.password.configure(background="#03e6ff")
        self.password.configure(font="TkFixedFont")
        self.password.configure(selectbackground="#c4c4c4")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.127, rely=0.156, height=36, width=241)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#d83253")
        self.Label1.configure(highlightcolor="#efeded")
        self.Label1.configure(takefocus="1")
        self.Label1.configure(text='''Enter Your Email Or Name''')

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.122, rely=0.268, height=36, width=241)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(background="#d83253")
        self.Label1_3.configure(text='''Enter Your Website''')

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(relx=0.12, rely=0.369, height=36, width=241)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(background="#d83253")
        self.Label1_4.configure(text='''Enter Your Password''')

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.0, rely=0.912, height=67, width=376)
        self.TLabel1.configure(background="#d83253")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''This Software Made By FahadAkash''')
        self.TLabel1.configure(cursor="spider")

        self.MainButton = tk.Button(top)
        self.MainButton.place(relx=0.455, rely=0.574, height=51, width=131)
        self.MainButton.configure(activebackground="#f9f9f9")
        self.MainButton.configure(background="#d8b91c")
        self.MainButton.configure(text='''Click Here''')
        self.MainButton.configure(command=self.passwordmanager)

        self.termcheck = tk.Checkbutton(top)
        self.termcheck.place(relx=0.401, rely=0.473, relheight=0.066
                , relwidth=0.329)
        self.termcheck.configure(activebackground="#d83253")
        self.termcheck.configure(background="#d83253")
        self.termcheck.configure(justify='left')
        self.termcheck.configure(state='active')
        self.termcheck.configure(text='''Check For Term And Condition''')
        self.termcheck.configure(variable=nnew_support.che57)

if __name__ == '__main__':
    vp_start_gui()






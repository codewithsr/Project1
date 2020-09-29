from tkinter import *
import tkinter.messagebox as tkMessageBox
import re
from tkinter import filedialog
import sqlite3
from PIL import Image,ImageTk
#***************************************Show**************************************

def show():
 delo=Tk()
 global describe
 describe=description.get(1.0,END)

 if:
      re.findall(r"headache",describe):
 label13=Label(delo,text="Medicine Name is:
Crocine",font=("arial",18),fg="red",bg="black")
 label13.pack()
 if re.findall(r"vomit|vomiting",describe):
 label=Label(delo,text="medicine name is :
Domparidon",font=("arial",18),fg="red",bg="black")
 label.pack()
 if re.findall(r"fever",describe):
 result=tkMessageBox.askquestion("question","Is your fever from last 3
days")
 if result =="yes":
 label14=Label(delo,text="you should test your fever "
,bg="black",fg="red",font=("arial",24))
 label14.pack()
 label15=Label(delo,text="Test Name is : Blood
Test",font=("arial",18),fg="red",bg="black")
 label15.pack()
 else:
 label1=Label(delo,text="Medicine Name is :
Paracetamol",font=("arial",18),fg="red",bg="black")
 label1.pack()
 if re.findall("^(vomiting|vomit).fever$",describe):
 label2=Label(delo,text="Medicine Name is: Paracetamol and
Domparidon ",font=("arial",18),fg="red",bg="black")
 label2.pack()
 if re.findall(r"stomach pain",describe):
 label3=Label(delo,text="Medicine Name is :Maffanic
acid",font=("arial",18),fg="red",bg="black")
 label3.pack()
 if re.findall(r"body pain",describe):
 label4=Label(delo,text="Medicine Name is : Paracetamol or
Combiflame",font=("arial",18),fg="red",bg="black")
 label4.pack()
 if re.findall("vomiting ,low energy|tired|tire,sleeping|sleep,problem in
breathing|breathing problem,pain in back|back pain,chest pain",describe ):
 label5=Label(delo,text="It might be hearth
disease",font=("arial",18),fg="red",bg="black")
 label5.place(x=200,y=500)
 label6=Label(delo,text="Consullt with
Doctor",font=("arial",18),fg="red",bg="black")
 label6.pack()
 if re.findall("low energy|tired|tire",describe):
 label60=Label(delo,text="Medicine Name is : Revital Or
Supradin",font=("arial",18),fg="red",bg="black")
 label60.pack()
 if re.findall("loose motion",describe):
 label7=Label(delo,text="Medicine Name is :
Oflexoz",font=("arial",18),fg="red",bg="black")
 label7.pack()
 if re.findall("problem in breathing|breathing problem",describe):
 label9=Label(delo,text="Medicine Name is
:",font=("arial",18),fg="red",bg="black")
 label9.pack()
 if re.findall("pain in back|back pain",describe):
 label10=Label(delo,text="Medicine Name is
:",font=("arial",18),fg="red",bg="black")
 label10.pack()
 if re.findall("cough|coughing,cold",describe):
 label11=Label(delo,text="Medicine Name is : Synarest or
Corex",font=("arial",18),fg="red",bg="black")
 label11.pack()
 if re.findall("throat pain",describe):
 label12=Label(delo,text="Medicine Name is :
Azee",font=("arial",18),fg="red",bg="black")
 label12.pack()
 if re.findall("izzing",describe):
 label13=Label(delo,text="Medicine Name is : Citrigin Or
Evil",font=("arial",18),fg="red",bg="black")
 label13.pack()
 if re.findall("liver pain",describe):
 label14=Label(delo,text="Medicine Name is : Maffanic
Acid",font=("arial",18),fg="red",bg="black")
 label14.pack()
 if re.findall("constipation",describe):
 label15=Label(delo,text="Medicine Name is :
Duflack",font=("arial",18),fg="red",bg="black")
 label15.pack()
# ****************************************Next
Button************************************************
def next():
 result1=tkMessageBox.askquestion("Question","do you want to
continue all details are correct")
 if result1=="yes":
 database()
 display.destroy()
 master = Tk()
 master.geometry("900x900")
 master.config(bg="red")
 label = Label(master, text="HEALTH CARE", font=("arial", 45,
"bold"),bg="black",fg="white").pack()
 c=Canvas(master)
 img=PhotoImage(file="C:\\Users\\Mohit\\Desktop\\image5.gif")
 label=Label(master,image=img).place(x=0,y=100)
 label1 = Label(master, text="Describe your disease", font=("arial",
18, "bold")).place(x=50, y=200)
 global description
 description = Text(master, bg='light blue')
 description.place(x=350, y=150, height=200, width=700)
 button=Button(master, text="Show
suggestion",command=show).place(x=300, y=400)
 master.mainloop()
# *****************
*******************file**************************************************************
def file():
 global file1
 file1 = filedialog.askopenfilename()
# **********************
SubmiT*******************************************************************
def submit():
 global x,y,z,a,username_info,password
 x = entry1.get()
 y = entry2.get()
 z=entry3.get()
 a=v.get()
 b=mine.get()
 username_info=entry4.get()
 password=entry5.get()
 match=re.search(r"@",username_info)
 match1=re.search(r"\d{3}",username_info)
 match2=re.search(r".com",username_info)
 match3=re.findall(r"@|_|-|!|#|%|&|.",password)
 match4=re.match(r"^{A-Z}",password)
 if b!=1:
 tkMessageBox.showerror("error","check the check button")
 if match2==None:
 tkMessageBox.showerror("error","invalid username")
 elif match==None:
 tkMessageBox.showerror("error","inalid username")
 elif match4=="":
 tkMessageBox.showerror("error","password empty")
 elif match1==None:
 tkMessageBox.showerror("error","invalid username")
 elif x=="":
 tkMessageBox.showerror("error","empty name")
 elif len(x)<2:
 tkMessageBox.showerror("error","length of name is small")
 elif x.isalpha()==False:
 tkMessageBox.showerror("error","invalid name")
 elif y=="":
 tkMessageBox.showerror("error","empty age")
 elif y.isnumeric()==False:
 tkMessageBox.showerror("error","invalid age")
 elif z=="":
 tkMessageBox.showerror("error","empty mobile number")
 elif z.isnumeric()==False:
 tkMessageBox.showerror("error","invalid mobile number")
 elif len(z)<10:
 tkMessageBox.showerror("error","length of mobile number is small")
 elif username_info=="":
 tkMessageBox.showerror("error","empty username")
 elif password=="":
 tkMessageBox.showerror("error","empty password")
 elif len(username_info)<10:
 tkMessageBox.showerror("error","length small of username")
 elif len(password)<8:
 tkMessageBox.showerror("small length of password")
 else:
 global display
 screen1.destroy()
 display=Tk()
 display.geometry("800x800")
 display.title("display data")
 #display.config(bg="orange")
 display1=Label(display,text="Health Care",font=("arial",45))
 display1.pack()
 #c=Canvas(display,height=1000,width=900)
 #img=PhotoImage(file="C:\\Users\\Mohit\\Desktop\\print.gif")
 #iamge=Label(window,image=img).place(x=0,y=100)
 display2=Label(display,text="Details of patient",font=("arial",24))
 display2.place(x=250,y=100)
 display3=Label(display,text="Name :"+" "+x,font=("arial",18))
 display3.place(x=150, y=250)
 display4 = Label(display, text="Age :" + " " + y, font=("arial", 18))
 display4.place(x=150, y=300)
 display5 = Label(display, text="Mobile Number :" + " " + z,
font=("arial", 18))
 display5.place(x=150, y=350)
 if a== 0:
 display6 = Label(display, text="Sex :" + "Male", font=("arial", 18))
 display6.place(x=150, y=400)
 elif a == 1:
 display7 = Label(display, text="Sex :" + "Female", font=("arial", 18))
 display7.place(x=150, y=400)
 display8=Label(display,text="username :"+"
"+username_info,font=("arial",18))
 display8.place(x=150,y=450)
 img = PhotoImage(file=file1)
 panel = Label(display, image = img,height=150,width=200)
 panel.place(x=600,y=150)
 button = Button(display, text="Next", command=next, width=25)
 button.place(x=400, y=550)
 button1 = Button(display, text="Edit", command=mohit, width=25)
 button1.place(x=600, y=550)
 display.mainloop()
# **************************LogIn***************************************
def login():
 global rip,entry7,entry6
 window.destroy()
 rip = Tk()
 frame=Frame(rip)
 rip.title("LogIn")
 rip.geometry("900x900")
 canvas=Canvas(rip)
 scrollbar=Scrollbar(rip)
 img=PhotoImage(file="C:\\Users\\Mohit\\Desktop\\image5.gif")
 Label(rip,image=img,).place(x=0,y=100)
 label = Label(rip, text="LOG IN", font=("arial", 45))
 label.pack()
 label1 = Label(rip, text="UserName", font=("arial", 18))
 label1.place(x=200, y=200)
 label3 = Label(rip, text=":")
 label3.place(x=400, y=200)
 entry7 = Entry(rip, width=40)
 entry7.place(x=500, y=200)
 label2 = Label(rip, text="Password:", font=("arial", 18))
 label2.place(x=200, y=300)
 entry6 = Entry(rip, width=40)
 entry6.place(x=500, y=300)
 label4 = Label(rip, text=":")
 label4.place(x=400, y=300)
 button = Button(rip, text="Login", width=40, command = lambda:my1())
 button.place(x=330, y=450)
 rip.mainloop()
# ************************** Help****************************************
def help():
 global screen
 screen = Tk()
 screen.title("Help")
 label1 = Label(screen, text="contact number=8130736520")
 label = Label(screen, text="contact to that number for further
information")
 label1.pack()
 label.pack()
# **********************************signup*****************************************
def mohit():
 global screen1
 window.destroy()
 screen1 = Tk()
 screen1.title("SIGN UP")
 screen1.minsize(width=900, height=900)
 screen1.geometry("800x800")
 screen1.config(bg="red")
 label=Label(screen1,text="Health
Care",font=("arial",45),fg="white",bg="black").pack()
 can=Canvas(screen1,height=1000,width=900)
 img=PhotoImage(file="C:\\Users\\Mohit\\Desktop\\image5.gif")
 label=Label(screen1,image=img).place(x=0,y=100)
 menu1 = Menu(screen1)
 # for menu bar
 screen1.config(menu=menu1) # it also pack
 submenu1 = Menu(menu1,bg="black")
 menu1.add_cascade(label="File", menu=submenu1)
 submenu1.add_command(label="Exit", command=quit)
 submenu2 = Menu(menu1)
 menu1.add_command(label="Help", command=help)
 menu1.add_command(label="Login")
 label1 = Label(screen1, text="Enter Your Name", font=("arial", 14))
 label1.place(x=200, y=200)
 label2 = Label(screen1, text="Enter your age", font=("arial", 14))
 label2.place(x=200, y=250)
 label3 = Label(screen1, text="Enter Mobile Number", font=("arial", 14))
 label3.place(x=200, y=300)
 label4 = Label(screen1, text="Enter Sex", font=("arial", 14))
 label4.place(x=200, y=350)
 global entry1
 entry1 = Entry(screen1, width=40)
 global entry2
 entry2 = Entry(screen1, width=40)
 global entry3
 entry3 = Entry(screen1, width=40)
 global entry4
 entry4 = Entry(screen1, width=40)
 global entry5
 entry5 = Entry(screen1, width=40,show="*")
 entry1.place(x=450, y=200)
 entry2.place(x=450, y=250)
 entry3.place(x=450, y=300)
 entry4.place(x=450, y=400)
 entry5.place(x=450, y=450)
 global v
 v=IntVar()
 radio1=Radiobutton(screen1, text="Male",variable=v, value=0)
 radio1.place(x=450,y=350)
 radio2=Radiobutton(screen1, text="female", variable=v , value=1)
 radio2.place(x=550, y=350)
 label5 = Label(screen1, text="Username", font=("arial", 14))
 label5.place(x=200, y=400)
 label6 = Label(screen1, text="Password", font=("arial", 14))
 label6.place(x=200, y=450)
 button = Button(screen1, text="upload image",command=file)
 button.place(x=200, y=500)
 global mine
 mine=IntVar()
 check = Checkbutton(screen1, text="I agree all details are
correct",variable=mine)
 check.place(x=200, y=550)
 btn = Button(screen1, text="submit",command=submit)
 btn.place(x=500, y=600)
 screen1.mainloop()
# *********************** Firstscreen**********************************************
global window
window=Tk()
window.geometry("800x800")
window.config(bg="sea green")
window.title("Health Care")
can=Canvas(window,height=1000,width=900)
label = Label(window, text="Health Care", font=("arial",
45),bg="black",fg="yellow")
label.pack()
img=PhotoImage(file="C:\\Users\\Mohit\\Desktop\\image.png")
label=Label(window,image=img).place(x=0,y=120)
button=Button(window,text="login",width=30,command=
login,bg="black",fg="yellow")
button.place(x=300,y=150)
button2 = Button(window, text="Sign up",
width=30,command=mohit,bg="black",fg="yellow")
button2.place(x=300, y=400)
window.mainloop()
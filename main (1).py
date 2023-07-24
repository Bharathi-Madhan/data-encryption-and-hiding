from tkinter import *
import time
from tkinter import filedialog
#from tkinter import messagebox
import os

import encryptor as e

root=Tk()
root.title("HIDE ITTTT")
root.geometry("350x400+500+200")
root.configure(bg="Light Green")
root.resizable(False,False)

def hiding():
    window=Toplevel(root)
    window.title("Encrypt nd hide!")
    window.geometry("300x245+500+200")
    window.configure(bg='Sky Blue')
    window.resizable(False,False)


    def select_cover():
        global filename1
        filename1=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select File",
                                            filetype=(('file_type','*.png'),('all files',".*")))
        print(filename1)

    def select_file():
        global filename2
        filename2=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select File",
                                            filetype=(('file_type','*.txt'),('all files',".*")))
        print(filename2)

    
    def eh():
        temp1 = filename1.split("/") #cover
        temp2 = filename2.split("/") #file
        #start = time.time()
        ehtime = e.main1(temp1[len(temp1)-1],temp2[len(temp2)-1])
        #end = time.time()
        print("FILE ENCRYPTED AND EMBEDDED SUCCESSFULLY......!")
        print("Time taken for data encryption nd hiding:",ehtime)
    
        
    #icon
    image_icon1=PhotoImage(file="D:/studies/mini project/gui/lock.png")
    window.iconphoto(False,image_icon1)

    Button(window,text="select cover image",width=14,height=1,font='arial 14 bold',bg='White',fg='Black',command=select_cover).place(x=60,y=30)
    Button(window,text="select file to encrypt",width=17,height=1,font='arial 14 bold',bg="White",fg='Black',command=select_file).place(x=50,y=100)

    Button(window,text="Encrypt nd hide!",width=15,height=1,bg='white',fg='black',command=eh).place(x=90,y=180)
    #Entry(window, width=20).insert(1,"name of new image(with extension)")
    #textbox.place(x= 90, y = 200)
    window.mainloop()

def unhiding():
    main=Toplevel(root)
    main.title("decrypt nd unhide!")
    main.geometry("300x245+500+200")
    main.configure(bg='Sky blue')
    main.resizable(False,False)

    def select_stego():
        global filename3
        filename3=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select File",
                                            filetype=(('file_type','*.png'),('all files',".*")))
        print(filename3)

    def du():
        print("Enter the key details")
        k1=int(input('e:'))
        k2=int(input('n:'))
        temp3 = filename3.split("/")
        temp3 = temp3[len(temp3)-1]
        start = time.time()
        e.main2(temp3,k1,k2)
        end = time.time()
        print("FILE EXTRACTED & DECRYPTED SUCCESSFULLY........!")
        print("Time taken for decryption:",(end-start))

    #icon
    image_icon1=PhotoImage(file="D:/studies/mini project/gui/lock.png")
    main.iconphoto(False,image_icon1)

    Label(main,text='Unhide',font=('arial',20),bg='White',fg='Black').place(x=95,y=31)    

    Button(main,text='Upload stego-image',width=17,height=1,font=('arial',15,'bold'),bg='White',fg='Black',command=select_stego).place(x=43,y=95)

    rr=Button(main,text='Unhide & decrypt!',width=18,height=1,bg='White',fg='Black',font='arial 14 bold',command=du)
    rr.place(x=37,y=150)
    
    main.mainloop()
    
#icon
image1=PhotoImage(file="D:/studies/mini project/gui/lock.png")
root.iconphoto(False,image1)

Label(root,text="Hide itt",font=('Arial 20 bold'),bg="Light Green").place(x=115,y=7)
Label(root,text='HIDE ITT-A data encryptor & hider app',font=('Acumin Variable Concept',10),bg="Light Green").place(x=45,y=327)
#Label(root,text='124157008',font=('Acumin Variable Concept',8),bg='#856ff8').place(x=140,y=350)
Frame(root,width=400,height=2,bg="White").place(x=0,y=50)

#hide button
enc=Button(root,text="HIDE",bg="pink",bd='5',command=hiding)
enc.place(x=50,y=65)

#unhide button
dec=Button(root,text="UNHIDE",bg="pink",bd='5',command=unhiding)
dec.place(x=225,y=65)

Label(root,image=image1).place(x=25,y=115)
root.mainloop()
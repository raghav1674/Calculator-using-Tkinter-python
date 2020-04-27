from tkinter import *
from tkinter.messagebox import showwarning,showinfo

root=Tk()






#previousresults=["no current value"]
# previousresults=list(set(previousresults))
root.geometry("320x340")
root.minsize(width="300",height="340")
root.maxsize(width=300,height=370)
#root.wm_iconbitmap("download.ico")
root.configure(background="light grey")
root.title("MY CALCULATOR")
opeartions=["7","8","9","<=","4","5","6","**","1","2","3","/","+","0","*","C","%","-",".","="]
# extra=["+","0","%","=","%","/",".","C"]
total=len(opeartions)
def click(event):
   # global scvalue
    #global previousresults
    text=str(event.widget.cget("text"))

    if text=="<=":
        te=scvalue.get()
        te=te.strip()
        # print(len(te))
        if len(te)==1:
            scvalue.set(" ")
            screen.update()
        else:
            text1=scvalue.get()
            text1=text1.strip()
            # print(text1)
            scvalue.set(text1[:len(text1)-1])
            screen.update()
    elif text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        elif len(scvalue.get().strip("=").strip())== 0:
            showinfo("NO INPUT","Enter value before evaluating")
            if len(previousresults)!=0:
                value=                               previousresults[len(previousresults)-1]
            else:
                value=" "
        else:
            try:
                value=round((eval(scvalue.get())),5)
            except:

               showwarning("INVALID INPUT","Enter the valid input")
               value="previous result:"+str(previousresults[len(previousresults)-1])


        scvalue.set(value)
        previousresults.append(value)
        print(previousresults)
        screen.update()


    elif text =="C":
        scvalue.set(" ")
        screen.update()
    else:

       scvalue.set(scvalue.get()+text)
       screen.update()
def enterkey(event):
    global previousresults
    if scvalue.get().isdigit():
        value = int(scvalue.get())
    elif len(scvalue.get().strip("=").strip()) == 0:
        showinfo("NO INPUT", "Enter value before evaluating")
        if len(previousresults) != 1:
            value = previousresults[len(previousresults) - 1]
        else:
            value = " "
    else:
        try:
            value = round((eval(scvalue.get())), 5)
        except:

            showwarning("INVALID INPUT", "Enter the valid input")
            value = " "


    scvalue.set(value)
    previousresults.append(value)
    screen.update()

def keyevents(event):
    global scvalue
    global previousresults
    key = str(event.char)

    if key == "":
        te = scvalue.get()
        te = te.strip()
        # print(len(te))
        if len(te) == 1:
            scvalue.set(" ")
            screen.update()
        else:
            text1 = scvalue.get()
            text1 = text1.strip()
            # print(text1)
            scvalue.set(text1[:len(text1) - 1])
            screen.update()
    elif key == "=":
        print(scvalue.get())

        if scvalue.get().isdigit():
            value = int(scvalue.get())

        elif len(scvalue.get().strip("=").strip()) == 0:
            showinfo("NO INPUT", "Enter value before evaluating")
            if len(previousresults) != 1:
                value ="previous result:"+str(previousresults[len(previousresults)-1])
            else:
                value = " "
        else:
            try:
                scvalue1=scvalue.get().strip("=")
                value = round((eval(scvalue1)), 5)
            except:

                showwarning("INVALID INPUT", "Enter the valid input")
                value = " "

        scvalue.set(value)
        previousresults.append(value)
        screen.update()


    elif key == "C":
        scvalue.set(" ")
        screen.update()
    else:
        if scvalue.get().isalpha()==True:
            showwarning("invalid input","no characters allowed")
            scvalue.set("error")
            screen.update()
        else:
            scvalue.set(scvalue.get()+key)
            screen.update()

scvalue=StringVar()
scvalue.set(" ")

screen=Entry(root,textvariable=scvalue,font="lucida 20")
screen.pack(fill=X,ipadx=20,padx=19,pady=17)
for i in range(0,total//4):
    f= "frame" +str(i)
    f=Frame(root,bg="light grey",width="270",height="60")
    a=total-(total-(4*i))
    b=total-(total-(4*(i+1)))
    # print(a)
    # print(b)
    for j in range(a,b):
        b ="button" +str(j)
        b=Button(f,text=opeartions[j],font="lucida 17",fg="white",bg="grey",padx=19)
        b.pack(side=LEFT,pady=1,padx=2)
        b.bind("<Button-1>",click)
    f.pack(padx=10)
    f.bind()
# for i in range(0,len(extra)//4):
#     f= "frame" +str(i)
#     f=Frame(root,bg="grey",width="270",height="60")
#     a=len(extra)-(len(extra)-(4*i))
#     b=len(extra)-(len(extra)-(4*(i+1)))
#     # print(a)
#     # print(b)
#     for j in range(a,b):
#         b ="button" +str(j)
#         b=Button(f,text=extra[j],font="lucida 18",padx=19)
#         b.pack(side=LEFT,pady=1,padx=1)
#         b.bind("<Button-1>",click)
#     f.pack(padx=10)

# print(previousresults)
root.bind("<Return>",enterkey)
root.bind("<Key>",keyevents)
root.mainloop()




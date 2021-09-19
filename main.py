from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import sqlite3


root = Tk()
root.geometry('600x600+460+75')
#root.resizable(False, False)



main_frame = Frame(root, height=791, width=1000)



my_canvas = Canvas(main_frame, height=596, width=578)
my_canvas.pack(side=LEFT, fill='y', expand='yes')

my_frame = Frame(my_canvas, height=800, width=578, bg='yellow')
my_canvas.create_window((0,0), window=my_frame, anchor='nw')


my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill='y')

my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))

main_frame.place(x=0, y=0)

'''
def hello(event):
    print(event.x_root)
    print(event.y)


root.bind('<Button-1>', hello)
'''




conn = sqlite3.connect('data.db')

c = conn.cursor()

#c.execute('''CREATE TABLE info(

#descp text,
#date text

#)''')

var_holder = {}
btn_holder = {}


font1 =Font(
    family = 'Helvatica',
    size= 25,
    weight = 'bold'
)
font2 = Font(
    size=15,
    weight='bold'
)


def easy_view():
    global Ent,imgg

    imgg = ImageTk.PhotoImage(file='C:/Users/dell/Downloads/bg-3.jpg')
    lable = Label(my_frame, image=imgg, width=600)
    lable.place(x=0, y=0)

    btn = Button(my_frame, text='+', bg='#1f3354', fg='white', height=1, width=5, font=font1,
                 activebackground='#1f3354', command=new_win)
    btn.place(x='235', y='220')

    Ent = Entry(my_frame, width=10, bg='#f009f3')
    Ent.place(x=451, y=20)
    btn1 = Button(my_frame, text='Delete', fg='white', bg='#000000', command=delete)
    btn1.place(x=518, y=15)





def check(event):

    print(event.x_root, event.y)


    n=1

    if event.y_root<=452:
        n=1
        print(n)
        pass
    else:
        num1 = event.y_root - 452 - 76
        if num1< 76:
            n += 1
            print(n)
            pass
        else:
            n+=1
            while True:
                num1 = num1 - 76-24
                if num1 < 76:
                    n+= 1
                    print(n)
                    break
                else:
                    n=n+1
    print(n)

def delete():

    global Ent, imgg
    conn = sqlite3.connect('data.db')

    c = conn.cursor()



    #print(event.x)
    #print(var.get())

    c.execute('DELETE FROM info WHERE oid=' + Ent.get())

    Ent.delete(0, END)

    #checking ways
    '''
    imgg = ImageTk.PhotoImage(file='C:/Users/dell/Downloads/bg-3.jpg')
    lable = Label(my_frame, image=imgg, width=600)
    lable.place(x=0, y=0)

    btn = Button(my_frame, text='+', bg='#1f3354', fg='white', height=1, width=5, font=font1,
                 activebackground='#1f3354', command=new_win)
    btn.place(x='235', y='220')

    Ent = Entry(my_frame, width=10, bg='#f009f3')
    Ent.place(x=451, y=20)
    btn1 = Button(my_frame, text='Delete', fg='white', bg='#000000', command=delete)
    btn1.place(x=518, y=15)
'''
    easy_view()
    #records = c.fetchall()
    #print(records)



    c.execute('SELECT *,oid FROM info')

    records = c.fetchall()

    number = 1
    axis = '320'
    for record in records:
        var_holder['lablo' + str(record[2])] = Frame(my_frame, bg='blue')
        locals().update(var_holder)
        lb1 = Label(var_holder['lablo' + str(record[2])], text=record[0], bg='blue', fg='white', width=50)
        lb1.grid(row=0, column=0, padx=10, pady=(12, 0))
        lb2 = Label(var_holder['lablo' + str(record[2])], text=record[1], bg='blue', fg='white')
        lb2.grid(row=1, column=0, padx=10, pady=(0, 12))
        btnn = Button(var_holder['lablo' + str(record[2])], bg='green', text=record[2], height=1, width=3,command=focs)
        btnn.grid(row=0, column=1, pady=(0, 8))
        btnn.bind('<Button-1>', check)
        var_holder['lablo' + str(record[2])].place(x='100', y=axis)
        axis = str(int(axis) + 100)
        number += 1

    #'#F0F0ED'
    #lbb = LabelFrame(my_frame, bg='yellow', height=80, width=420, bd=0).place(x=100, y=axis)



    conn.commit()

    conn.close()




def save():
    conn = sqlite3.connect('data.db')

    c = conn.cursor()

    c.execute(
        "INSERT INTO info VALUES(:descp, :date)",

        {
            'descp': ent1.get(),
            'date': ent2.get()


        })

    c.execute("SELECT *,oid FROM info")

    records = c.fetchall()


    #one =''
    #two=''
    #three=''
    #four=''
    #five=''
    #six=''


    #lablo = [one, two,three, four, five, six]


    var_holder = {}







    axis = '320'
    number = 1
    for record in records:
        var_holder['lablo'+str(record[2])]=Frame(my_frame, bg='blue')
        locals().update(var_holder)
        lb1 = Label(var_holder['lablo'+str(record[2])], text=record[0], bg='blue', fg='white', width=50)
        lb1.grid(row=0, column=0,padx=10, pady=(12,0))
        lb2 = Label(var_holder['lablo'+str(record[2])], text=record[1], bg='blue', fg='white')
        lb2.grid(row=1, column=0,padx=10, pady=(0,12))
        btnn = Button(var_holder['lablo'+str(record[2])],bg='green', text=record[2] , height=1, width=3,command=focs)
        btnn.grid(row=0, column=1, pady=(0,8))
        btnn.bind('<Button-1>', check )
        print(number)
        var_holder['lablo'+str(record[2])].place(x='100', y=axis)
        axis = str(int(axis)+ 100)
        number +=1


    new.destroy()


    conn.commit()

    conn.close()


def new_win():
    global ent1, ent2, new, img
    new = Toplevel()

    img = PhotoImage(file='C:/Users/dell/Documents/grad.png')
    lb = Label(new, image=img)
    lb.place(x=0, y=0)

    new.geometry('300x300+620+180')

    lbb1 = Label(new, text='Subject', bg='#bccae0', bd=0, font=font2).place(x=120, y=30)
    ent1 = Entry(new, width=30,bd=0)
    ent1.place(x=62, y=60)

    lbb2 = Label(new, text='Date', bg='#bccae0', bd=0, font=font2).place(x=132, y=90)
    ent2 = Entry(new, bd=0)
    ent2.place(x=90, y=120)

    btn1 = Button(new, text='Save', command=save, bg='#419c7d', bd=0, font=font2)
    btn1.place(x=126, y=160)

def focs():
    messagebox.showinfo('Option', 'you can delete subject entering Serial number')
    Ent.focus()

'''
imgg = ImageTk.PhotoImage(file='C:/Users/dell/Downloads/bg-3.jpg')
lable = Label(my_frame, image=imgg, width=600)
lable.place(x=0, y=0)

'''

easy_view()

c.execute('SELECT *,oid FROM info')

records = c.fetchall()


axis = '320'

num=1

print(records)

for record in records:
    var_holder['lablo' + str(record[2])] = Frame(my_frame, bg='blue')

    locals().update(var_holder)
    lb1 = Label(var_holder['lablo' + str(record[2])], text=record[0], bg='blue', fg='white', width=50)
    lb1.grid(row=0, column=0, padx=10, pady=(12, 0))
    lb2 = Label(var_holder['lablo' + str(record[2])], text=record[1], bg='blue', fg='white')
    lb2.grid(row=1, column=0, padx=10, pady=(0, 12))


    btnn = Button(var_holder['lablo' + str(record[2])], bg='green', text=record[2], height=1, width=3, command=focs)
    btnn.grid(row=0, column=1, pady=(0, 8))
    root.bind('<Button-1>', check)
    #btn_holder['btnn' + str(record[2])].bind('<Button-1>', delete)
    var_holder['lablo' + str(record[2])].place(x='100', y=axis)
    axis = str(int(axis) + 100)
    num +=1



'''
btn = Button(my_frame, text='+', bg='#1f3354', fg='white', height=1, width=5, font=font1, activebackground='#1f3354', command=new_win)
btn.place(x='235', y='220')

Ent = Entry(my_frame, width=10, bg='#f009f3')
Ent.place(x=451, y=20)
btn1 = Button(my_frame, text='Delete', fg='white', bg='#000000', command=delete)
btn1.place(x=518, y=15)

'''


conn.commit()

conn.close()






root.mainloop()
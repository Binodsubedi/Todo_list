from tkinter import *
import pytest
from PIL import ImageTk, Image
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import sqlite3



root = Tk()
root.geometry('600x600+460+75')
root.resizable(False, False)

root.title('Todo-list')
root.iconbitmap('images/icon.ico')

main_frame = Frame(root, height=791, width=1000)



my_canvas = Canvas(main_frame, height=596, width=578)
my_canvas.pack(side=LEFT, fill='y', expand='yes')

my_frame = Frame(my_canvas, height=900, width=578)
my_canvas.create_window((0,0), window=my_frame, anchor='nw')


my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill='y')

my_canvas.config(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))

main_frame.place(x=0, y=0)

#try-1 to bind all the buttons

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


#number = 0


def easy_view():
    global Ent,imgg

    imgg = ImageTk.PhotoImage(file='images/bg-3.jpg')
    lable = Label(my_frame, image=imgg, width=600)
    lable.place(x=0, y=0)

    btn = Button(my_frame, text='+', bg='#1f3354', fg='white', height=1, width=5, font=font1,
                 activebackground='#1f3354', command=new_win)
    btn.place(x='235', y='220')

    Ent = Entry(my_frame, width=10, bg='#239e7f')
    Ent.place(x=451, y=20)
    btn1 = Button(my_frame, text='Delete', fg='white', bg='#000000', command=delete)
    btn1.place(x=518, y=15)



#Checking ideas

'''

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
'''


def delete():



    global Ent, imgg



    lol= Ent.get()


    if Ent.get() != '':


        conn = sqlite3.connect('data.db')

        c = conn.cursor()




        #print(event.x)
        #print(var.get())

        c.execute('DELETE FROM info WHERE oid=' + Ent.get())

        Ent.delete(0, END)



        #checking ways
        #used the whole commented below code in function for easy multiple use
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

        #number = 1
        axis = '320'
        for record in records:
            var_holder['lablo' + str(record[2])] = Frame(my_frame, bg='#119959')
            locals().update(var_holder)
            lb1 = Label(var_holder['lablo' + str(record[2])], text=record[0], bg='#119959', fg='white', width=50)
            lb1.grid(row=0, column=0, padx=10, pady=(12, 0))
            lb2 = Label(var_holder['lablo' + str(record[2])], text=record[1], bg='#119959', fg='white')
            lb2.grid(row=1, column=0, padx=10, pady=(0, 12))
            btnn = Button(var_holder['lablo' + str(record[2])], bg='green', text=record[2], height=1, width=3,command=focs)
            btnn.grid(row=0, column=1, pady=(0, 8))

            var_holder['lablo' + str(record[2])].place(x='100', y=axis)
            axis = str(int(axis) + 100)
            #number += 1

        #'#F0F0ED'
        #lbb = LabelFrame(my_frame, bg='yellow', height=80, width=420, bd=0).place(x=100, y=axis)


        conn.commit()

        conn.close()

    else:
        messagebox.showinfo('Empty field', 'Please enter the serial number first')




    return lol




def save():

    if ent1.get() != '' and ent2.get() != '':

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
        #global number

        for record in records:
            var_holder['lablo'+str(record[2])]=Frame(my_frame, bg='#119959')
            locals().update(var_holder)
            lb1 = Label(var_holder['lablo'+str(record[2])], text=record[0], bg='#119959', fg='white', width=50)
            lb1.grid(row=0, column=0,padx=10, pady=(12,0))
            lb2 = Label(var_holder['lablo'+str(record[2])], text=record[1], bg='#119959', fg='white')
            lb2.grid(row=1, column=0,padx=10, pady=(0,12))
            btnn = Button(var_holder['lablo'+str(record[2])],bg='green', text=record[2] , height=1, width=3,command=focs)
            btnn.grid(row=0, column=1, pady=(0,8))

            #print(number)
            var_holder['lablo'+str(record[2])].place(x='100', y=axis)
            axis = str(int(axis)+ 100)
            #number +=1


        new.destroy()


        conn.commit()

        conn.close()

    else:
        new.grab_set()
        messagebox.showinfo('Empty fields', 'Please first fill all the entries')


def new_win():
    global ent1, ent2, new, img
    new = Toplevel()
    new.resizable(0,0)
    new.title('Info')
    new.iconbitmap('images/icon.ico')

    img = PhotoImage(file='images/grad.png')
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

#num=1

#print(records)

for record in records:
    var_holder['lablo' + str(record[2])] = Frame(my_frame, bg='#119959')

    locals().update(var_holder)
    lb1 = Label(var_holder['lablo' + str(record[2])], text=record[0], bg='#119959', fg='white', width=50)
    lb1.grid(row=0, column=0, padx=10, pady=(12, 0))
    lb2 = Label(var_holder['lablo' + str(record[2])], text=record[1], bg='#119959', fg='white')
    lb2.grid(row=1, column=0, padx=10, pady=(0, 12))


    btnn = Button(var_holder['lablo' + str(record[2])], bg='green', text=record[2], height=1, width=3, command=focs)
    btnn.grid(row=0, column=1, pady=(0, 8))



    #btn_holder['btnn' + str(record[2])].bind('<Button-1>', delete)
    var_holder['lablo' + str(record[2])].place(x='100', y=axis)
    axis = str(int(axis) + 100)
    #number +=1



'''
btn = Button(my_frame, text='+', bg='#1f3354', fg='white', height=1, width=5, font=font1, activebackground='#1f3354', command=new_win)
btn.place(x='235', y='220')

Ent = Entry(my_frame, width=10, bg='#f009f3')
Ent.place(x=451, y=20)
btn1 = Button(my_frame, text='Delete', fg='white', bg='#000000', command=delete)
btn1.place(x=518, y=15)

'''
#pytest-------------------
'''
@pytest.fixture
def delet():
    global Ent

    a = Ent.get()

    return a
def test_1(delet):
    b=1
    assert  delet == b
'''








'''
@pytest.mark.parametrize('x,y,z,a', [(Ent1,Ent2,'Admin', '123'), (Ent1,Ent2,'lol', '111'),(Ent1,Ent2,'', '123')])
def test(x, y, z, a):
    assert x == z
    assert y == a


@pytest.mark.parametrize('a,b',[(Ent.get(),''),(Ent.get(), '1')])
def test(a,b):
    assert a == b




#number means total number of created list items

@pytest.mark.parametrize('x,y',[(number,1),(number, 2)])
def test(x,y):
    assert x == y

'''


'''
def pytest_1(delete):
    a= 1
    b=''
    assert delete == a
    assert delete == b
'''
conn.commit()

conn.close()






root.mainloop()
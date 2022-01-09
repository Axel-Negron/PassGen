import random
from tkinter import *
import pyperclip

try:
    password_file = open('Entry.txt', "r")
except:
    password_file = open('Entry.txt','w')


def Delete_Pass(x,y):
    deleted = 0
    with open('Entry.txt','r+') as p:
        new_p = p.readlines()
        p.seek(0)
        for line in new_p:
            if deleted == 0:
                if x not in line:
                    p.write(line)

                if x in line:
                    deleted = 1
                    continue
            if deleted == 1:
                p.write(line)
        p.truncate()
        p.close()
    if y == 1:
        Stored_1 = Label(root,width=30, height=2, font="Fixedsys")
        Stored_1.place(x=10, y=200)
        Store_1 = ''
    if y == 2:
        Stored_2 = Label(root, width=30, height=2, font="Fixedsys")
        Stored_2.place(x=10, y=300)
        Store_2 = ''
    if y == 3:
        Stored_3 = Label(root, width=30, height=2, font="Fixedsys")
        Stored_3.place(x=10, y=400)
        Store_3 = ''
    if y == 4:
        Stored_4 = Label(root, width=30, height=2, font="Fixedsys")
        Stored_4.place(x=355, y=200)
        Store_4 = ''

def Save_Password(y):
    password_file = open('Entry.txt', "r")
    counter = 0
    for thing in password_file:
        counter += 1
    password_file.close()
    if counter < 5:
        password_file = open('Entry.txt', "a")
        password_file.write(password+' '+y+'\n')
        password_file.close()

    else:
        Error_Label = Label(root, text='Cant save more', width=105, height=10)
        Error_Label.place(x=0, y=240)
        Error_Label.after(500, Error_Label.destroy)
    reset()


def get_copy(x):
    try:
        pyperclip.copy(x)
    except:
        Error_Label= Label(root, text='Nothing to be copied', width=105, height=10)
        Error_Label.place(x=0, y=240)
        Error_Label.after(500, Error_Label.destroy)


def clear():
    Password_Label.configure(text='Password Generator')



usable_characters = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',"z"]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',"z"]
usable_symbols = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',"z",'_','-']

global displayed_password
displayed_password = 'Password Generator'
# Window gui stuff
root = Tk()
root.resizable(0, 0)
boot = 1
deleted = 0
symbols = IntVar()


root.configure(height=480, width=720, bg='grey')

Password_Label = Label(root, text=displayed_password, width=50, height=5, font="Fixedsys")
Password_Label.place(x=10, y=5)

Size_var = StringVar()
Size_Entry = Entry(root, text=0, width=30, bg='white', textvariable=Size_var)
Size_Entry.place(x=10, y=110)

Name_variable = StringVar()
Name_Entry = Entry(root, text=0, width=30, bg='white', textvariable=Name_variable)
Name_Entry.place(x=200, y=110)

Password_entry_label = Label(root, text='Password Lenght', bg='grey', fg='white', width=30, font="Fixedsys",anchor='w')
Password_entry_label.place(x=10, y=90)

Name_entry_label = Label(root, text='Name', bg='grey', fg='white', width=30, font="Fixedsys",anchor='w')
Name_entry_label.place(x=200, y=90)

Size_Button = Button(root, text='Get', width=30, height=2, bg='grey40', fg='white')


def reset():
    password_file = open('Entry.txt', "r+")
    global saved_password_1
    global saved_password_2
    global saved_password_3
    global saved_password_4
    list_of_passwords = []
    list_of_names = []

    for thing in password_file:
        Data = thing.split()
        list_of_passwords.append(Data[0])
        list_of_names.append(Data[1])

    try:
        saved_password_1 = [list_of_passwords[0], list_of_names[0]]
        saved_password_2 = [list_of_passwords[1], list_of_names[1]]
        saved_password_3 = [list_of_passwords[2], list_of_names[2]]
        saved_password_4 = [list_of_passwords[3], list_of_names[3]]
    except:
        print('Done')

    try:
        Stored_1 = Label(root, text=saved_password_1[0], width=30, height=2, font="Fixedsys")
        Stored_1.place(x=10, y=200)
        Saved_Text1 = Label(root, text=saved_password_1[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text1.place(x=10, y=170)
    except:
        Stored_1 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_1.place(x=10, y=200)
        Saved_Text1 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text1.place(x=10, y=170)
    try:
        Stored_2 = Label(root, text=saved_password_2[0], width=30, height=2, font="Fixedsys")
        Stored_2.place(x=10, y=300)
        Saved_Text2 = Label(root, text=saved_password_2[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text2.place(x=110, y=270)
    except:
        Stored_2 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_2.place(x=10, y=300)
        Saved_Text2 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text2.place(x=10, y=270)
    try:
        Stored_3 = Label(root, text=saved_password_3[0], width=30, height=2, font="Fixedsys")
        Stored_3.place(x=10, y=400)
        Saved_Text3 = Label(root, text=saved_password_3[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text3.place(x=10, y=370)
    except:
        Stored_3 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_3.place(x=10, y=400)
        Saved_Text3 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text3.place(x=10, y=370)
    try:
        Stored_4 = Label(root, text=saved_password_3[0], width=30, height=2, font="Fixedsys")
        Stored_4.place(x=355, y=200)
        Saved_Text4 = Label(root, text=saved_password_4, bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text4.place(x=355, y=170)
    except:
        Stored_4 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_4.place(x=355, y=200)
        Saved_Text4 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text4.place(x=355, y=170)

    password_file.close()


if boot == 1:
    password_file = open('Entry.txt', "r+")
    global saved_password_1
    global saved_password_2
    global saved_password_3
    global saved_password_4
    list_of_passwords = []
    list_of_names = []

    for thing in password_file:
        Data = thing.split()
        list_of_passwords.append(Data[0])
        list_of_names.append(Data[1])

    try:
        saved_password_1 = [list_of_passwords[0], list_of_names[0]]
        saved_password_2 = [list_of_passwords[1], list_of_names[1]]
        saved_password_3 = [list_of_passwords[2], list_of_names[2]]
        saved_password_4 = [list_of_passwords[3], list_of_names[3]]
    except:
        print('Done')

    try:
        Stored_1 = Label(root, text=saved_password_1[0], width=30, height=2, font="Fixedsys")
        Stored_1.place(x=10, y=200)
        Saved_Text1 = Label(root, text=saved_password_1[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text1.place(x=10, y=170)
    except:
        Stored_1 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_1.place(x=10, y=200)
        Saved_Text1 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text1.place(x=10, y=170)
    try:
        Stored_2 = Label(root, text=saved_password_2[0], width=30, height=2, font="Fixedsys")
        Stored_2.place(x=10, y=300)
        Saved_Text2 = Label(root, text=saved_password_2[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text2.place(x=10, y=270)
    except:
        Stored_2 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_2.place(x=10, y=300)
        Saved_Text2 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text2.place(x=10, y=270)
    try:
        Stored_3 = Label(root, text=saved_password_3[0], width=30, height=2, font="Fixedsys")
        Stored_3.place(x=10, y=400)
        Saved_Text3 = Label(root, text=saved_password_3[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text3.place(x=10, y=370)
    except:
        Stored_3 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_3.place(x=10, y=400)
        Saved_Text3 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text3.place(x=10, y=370)
    try:
        Stored_4 = Label(root, text=saved_password_3[0], width=30, height=2, font="Fixedsys")
        Stored_4.place(x=355, y=200)
        Saved_Text4 = Label(root, text=saved_password_4[1], bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text4.place(x=355, y=170)
    except:
        Stored_4 = Label(root, text='', width=30, height=2, font="Fixedsys")
        Stored_4.place(x=355, y=200)
        Saved_Text4 = Label(root, text='Empty', bg='grey', width=30, fg='white', font='fixedsys')
        Saved_Text4.place(x=355, y=170)


    password_file.close()
    boot = 0


def generatepass(x,y):
    global password
    password1 = ''
    password = ''
    roll = [1, 2]

    if int(x) > 50:
        Password_Label.configure(text='Password Generator')
        Error_Label = Label(root, text='Length exceeded 0 < x < 50, Full Password wont be displayed', width=105, height=10)
        Error_Label.place(x=0, y=240)
        Error_Label.after(5000, Error_Label.destroy)

    if symbols.get() == 0:
        try:
            while len(password1) < int(x):
                checker = random.choice(usable_characters)
                if type(checker) == int:
                    password1 += str(checker)
                else:
                    if random.choice(roll) == 1:
                        password1 += checker
                    else:
                        password1 += checker.upper()
            password = password1
            Password_Label.configure(text=password)

        except:
            Password_Label.configure(text='Password Generator')
            Error_Label = Label(root, text='Length Invalid. Length needed', width=105, height=10)
            Error_Label.place(x=0, y=240)
            Error_Label.after(500, Error_Label.destroy)
    elif symbols.get() == 1:
        try:
            password1 += random.choice(['-', '_'])
            while len(password1) < int(x):
                checker = random.choice(usable_symbols)
                if type(checker) == int:
                    password1 += str(checker)
                elif checker in letters:
                    if random.choice(roll) == 1:
                        password1 += checker
                    else:
                        password1 += checker.upper()
                else:
                    password1 += str(checker)
            password = ''.join(random.sample(password1, len(password1)))
            Password_Label.configure(text=password)

        except:
            Password_Label.configure(text='Password Generator')
            Error_Label = Label(root, text='Length Invalid. Length needed', width=105, height=10)
            Error_Label.place(x=0, y=240)
            Error_Label.after(500, Error_Label.destroy)


Generate_Button = Button(root, text='Generate', width=30, height=2, bg='grey40', fg='white', command=lambda: generatepass(Size_Entry.get(), Name_Entry.get()))
Generate_Button.place(x=395, y=100)


Copy = Button(root, text='Copy', width=10, height=2, bg='grey40', fg='white', command=lambda: get_copy(password))
Copy.place(x=420, y=5)

Clear = Button(root, text='Clear', width=10, height=1, bg='grey40', fg='white', command=clear)
Clear.place(x=420, y=50)

Save_Button = Button(root,text='Save', width=10, height=2, bg='grey40', fg='white', command=lambda: Save_Password(Name_Entry.get()))
Save_Button.place(x=620, y=100)

#Fuck this was unnecesary
Delete_Button1 = Button(root, text='Delete', width=5, height=2, bg='grey40', fg='white', command=lambda: Delete_Pass(saved_password_1[0],1))
Delete_Button1.place(x=255, y=198)

Copy_Button1 = Button(root, text='Copy', width=5, height=2, bg='grey40', fg='white', command=lambda: get_copy(saved_password_1))
Copy_Button1.place(x=305, y=198)

Delete_Button2 = Button(root, text='Delete', width=5, height=2, bg='grey40', fg='white', command=lambda: Delete_Pass(saved_password_2[0],2))
Delete_Button2.place(x=255, y=298)

Copy_Button2 = Button(root, text='Copy', width=5, height=2, bg='grey40', fg='white', command=lambda: get_copy(saved_password_2))
Copy_Button2.place(x=305, y=298)

Delete_Button3 = Button(root, text='Delete', width=5, height=2, bg='grey40', fg='white', command=lambda: Delete_Pass(saved_password_3[0],3))
Delete_Button3.place(x=255, y=398)

Copy_Button3 = Button(root, text='Copy', width=5, height=2, bg='grey40', fg='white', command=lambda: get_copy(saved_password_3))
Copy_Button3.place(x=305, y=398)

Delete_Button3 = Button(root, text='Delete', width=5, height=2, bg='grey40', fg='white', command=lambda: Delete_Pass(saved_password_4[0],4))
Delete_Button3.place(x=605, y=198)

Copy_Button4 = Button(root, text='Copy', width=5, height=2, bg='grey40', fg='white', command=lambda: get_copy(saved_password_4))
Copy_Button4.place(x=655, y=198)

Symbol_check = Checkbutton(root, text='Symbols', bg='grey', variable=symbols, command=lambda: print(symbols))
Symbol_check.place(x=520, y=5)


Test = Button(root,text='Debug', width=5, font='fixedsys', command=lambda: print(Name_Entry.get()))
Test.place(x=650, y=10)



root.mainloop()



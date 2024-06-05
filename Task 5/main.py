from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

# colors
cl1 = "#FFFFFF"
cl2 = "#000000"
cl3 = "#34A85A"

# creating a window
window = Tk()
window.title("Contact Book")
window.geometry("600x600")
window.configure(background=cl1)
window.resizable(False, False)

# Frames for the GUI
frameUp = Frame(window, width=600, height=50, bg=cl3)
frameUp.grid(column=0, row=0, padx=0, pady=1)

frameDown = Frame(window, width=600, height=150, bg=cl1)
frameDown.grid(column=0, row=1, padx=0, pady=1)

frameTable = Frame(window, width=600, height=100, bg=cl1, relief="flat")
frameTable.grid(column=0, row=2, columnspan=2, padx=10, pady=1, sticky=NW)


# Functions

def show():
    global tree
    listHeader = ['Name', 'Phone', 'Email', 'Address']
    demoList = view()
    tree = ttk.Treeview(frameTable, selectmode="extended", columns=listHeader, show="headings")

    vSroll = ttk.Scrollbar(frameTable, orient="vertical", command=tree.yview)
    hSroll = ttk.Scrollbar(frameTable, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vSroll.set, xscrollcommand=hSroll.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vSroll.grid(column=1, row=0, sticky='ns')
    hSroll.grid(column=0, row=1, sticky='ew')

    # tree heading
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Phone', anchor=NW)
    tree.heading(2, text='Email', anchor=NW)
    tree.heading(3, text='Address', anchor=NW)

    # tree Columns
    tree.column(0, width=120, anchor=NW)
    tree.column(1, width=80, anchor=NW)
    tree.column(2, width=173, anchor=NW)
    tree.column(3, width=190, anchor=NW)

    for item in demoList:
        tree.insert('', 'end', values=item)


show()


def insert():
    Name = entryName.get()
    Phone = entryPno.get()
    Email = entryEmail.get()
    Address = entryAdd.get()

    data = [Name, Phone, Email, Address]

    if Name == '' or Phone == '' or Email == '' or Address == '':
        messagebox.showwarning('data', 'Please Fill in All Fields')
    else:
        add(data)
        messagebox.showinfo('data', 'Data Added Successfully')
        entryName.delete(0, 'end')
        entryPno.delete(0, 'end')
        entryEmail.delete(0, 'end')
        entryAdd.delete(0, 'end')
        show()


def toUpdate():
    try:
        treeData = tree.focus()
        treeDictionary = tree.item(treeData)
        treeList = treeDictionary['values']

        Name = str(treeList[0])
        Phone = str(treeList[1])
        Email = str(treeList[2])
        Address = str(treeList[3])

        entryName.insert(0,Name)
        entryPno.insert(1,Phone)
        entryEmail.insert(2,Email)
        entryAdd.insert(3,Address)

        def confirm():
            newName = entryName.get()
            newPhone = entryPno.get()
            newEmail = entryEmail.get()
            newAdd = entryAdd.get()

            data = [newPhone,newName,newPhone,newEmail,newAdd]
            update(data)

            messagebox.showinfo('data','Data Updated Successfully')

            entryName.delete(0, 'end')
            entryPno.delete(0, 'end')
            entryEmail.delete(0, 'end')
            entryAdd.delete(0, 'end')

            for widget in frameTable.winfo_children():
                widget.destroy()

            buttonConfirm.destroy()
            show()
        buttonConfirm = Button(frameDown, text="Confirm", width=10, height=1, bg=cl3, fg=cl1, font=('Ivy 8 bold'),command=confirm)
        buttonConfirm.place(x = 390, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of the from table')


def toRemove():
    try:
        treeData = tree.focus()
        treeDictionary = tree.item(treeData)
        treeList = treeDictionary['values']
        treePhone = str(treeList[2])

        remove(treePhone)

        messagebox.showinfo('Success', 'Data has been deleted successfully')

        for widget in frameTable.winfo_children():
            widget.destroy()

        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of the from table')


def toSearch():
    phone = entrySearch.get()

    data = search(phone)

    def delCommand():
        tree.delete(*tree.get_children())

    delCommand()

    for item in data:
        tree.insert('','end', values = item)
    entrySearch.delete(0,'end')


# frameUp widgets

appName = Label(frameUp, text="Contact Book", font='Verdana 17 bold', height=1, bg=cl3, fg=cl1)
appName.place(x=5, y=5)

# frameDown widgets
labelName = Label(frameDown, text="Name *", width=10, height=1, font=('Ivy 10'), bg=cl1, anchor=NW)
labelName.place(x=10, y=20)
entryName = Entry(frameDown, width=25, justify='left', highlightthickness=1, relief="solid", font=('Ivy 10'), bg=cl1)
entryName.place(x=80, y=20)

labelEmail = Label(frameDown, text="Email *", width=10, height=1, font=('Ivy 10'), bg=cl1, anchor=NW)
labelEmail.place(x=10, y=50)
entryEmail = Entry(frameDown, width=25, justify='left', highlightthickness=1, relief="solid", font=('Ivy 10'), bg=cl1)
entryEmail.place(x=80, y=50)

labelPno = Label(frameDown, text="Phone *", height=1, font=('Ivy 10'), bg=cl1, anchor=NW)
labelPno.place(x=10, y=80)
entryPno = Entry(frameDown, width=25, justify='left', highlightthickness=1, relief="solid", font=('Ivy 10'), bg=cl1)
entryPno.place(x=80, y=80)

labelAdd = Label(frameDown, text="Address *", width=10, height=1, font=('Ivy 10'), bg=cl1, anchor=NW)
labelAdd.place(x=10, y=110)
entryAdd = Entry(frameDown, width=25, justify='left', highlightthickness=1, relief="solid", font='Ivy 10', bg=cl1)
entryAdd.place(x=80, y=110)

buttonSearch = Button(frameDown, text="Search", height=1, bg=cl3, fg=cl1, font='Ivy 8 bold',command=toSearch)
buttonSearch.place(x=390, y=20)
entrySearch = Entry(frameDown, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
entrySearch.place(x=448, y=20)

buttonView = Button(frameDown, text="View", height=1, bg=cl3, fg=cl1, font='Ivy 8 bold',command=show)
buttonView.place(x=390, y=50)

buttonADD = Button(frameDown, text="Add", width=10, height=1, bg=cl3, fg=cl1, font='Ivy 8 bold', command=insert)
buttonADD.place(x=500, y=50)

buttonUpdate = Button(frameDown, text="Update", width=10, height=1, bg=cl3, fg=cl1, font='Ivy 8 bold', command=toUpdate)
buttonUpdate.place(x=500, y=80)

buttonDel = Button(frameDown, text="Delete", width=10, height=1, bg=cl3, fg=cl1, font='Ivy 8 bold', command=toRemove)
buttonDel.place(x=500, y=110)

window.mainloop()

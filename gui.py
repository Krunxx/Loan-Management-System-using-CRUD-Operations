from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from ooptest import LoanDatabase
import pickle 

db = LoanDatabase('store.db')

# db.fetch() Kuhaon ang data then  parts_list.insert(END, row) is gi sulod niya sa katong white box
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)

def add_item():
    try:    
        db.insert(Firstname.get(), Lastname.get(),
                Principal.get(), YearTerm.get(), calculate())
        parts_list.delete(0, END)
        parts_list.insert(END, (Firstname.get(), Lastname.get(),
                Principal.get(), YearTerm.get(), calculate()))
    
    except:
        if Firstname.get() == '' or Lastname.get() == '' or Principal.get() == '' or YearTerm.get() == '':
            messagebox.showerror('*Required Fields', 'Please include all fields')
        return
    
    finally:
        clear_text()
        populate_list()

# Allows user  to select the data either
def select_item(event):
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        Firstname.delete(0, END)
        Firstname.insert(END, selected_item[1])
        Lastname.delete(0, END)
        Lastname.insert(END, selected_item[2])
        Principal.delete(0, END)
        Principal.insert(END, selected_item[3])
        YearTerm.delete(0, END)
        YearTerm.insert(END, selected_item[4])
        LoanTotal.delete(0, END)
        LoanTotal.insert(END, selected_item[5])
        
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    try:
        db.update(selected_item[0], Firstname.get(), Lastname.get(),
                Principal.get(), YearTerm.get(), calculate())
        populate_list()
    
    except:
        if Firstname.get() == '' or Lastname.get() == '' or Principal.get() == '' or YearTerm.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
        return

def clear_text():
    Firstname.delete(0, END)
    Lastname.delete(0, END)
    Principal.delete(0, END)
    YearTerm.delete(0, END)
    LoanTotal.delete(0, END)
    
def calculate():
    p = int(Principal.get())
    t = int(YearTerm.get())
    total = (p * 0.10 * t) + p
    return total

#Open to Read the file 
def open_file():
    path = filedialog.askopenfilename(initialdir="C:\\Users\\Karen\\Documents\\test", defaultextension='.txt',filetypes=[("Text file",".txt"),])
    
    if(path):
        fh =open(path, 'r')
        messagebox.showinfo(path,fh.read())
         
#Write File Handling
def save_file():
    try:
        file = open("storeData.txt", "wb")
        file.write(db.fetch())
        
    finally:
        file.close()
        messagebox.showinfo("*", "Database as text has been saved successfully!")
        
def convert_binary():
    all = (str(db.fetch()))
    try:
        result = ' '. join(format(ord(i), 'b') for i in all)
        x = open("storeBinary.txt", "wb") #wb
        pickle.dump(result, x)

    except:
        messagebox.showerror("", "Fail to convert file")
        
    finally:
        x.close()
        messagebox.showinfo("++The Database has been converted into Binary file++", result)
        print("Finally")
 
root = Tk()
root = root
root.title("Bangku Gulugulu | Loan ")
root.geometry("1000x780")
root.resizable('false', 'false')

my_menu = Menu(root)
root.configure(menu = my_menu,  bg = "#95C8F0")

file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label = "File", menu=file_menu)
file_menu.add_command(label = "Open File", command = open_file)
file_menu.add_command(label = "Save Database as text", command = save_file)
file_menu.add_command(label = "Save As..")
file_menu.add_separator()
file_menu.add_command(label = "Convert File Database As Binary", command = convert_binary)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command=root.quit)

status_bar = Label(root, text = 'Ready     ', anchor = E)
status_bar.pack(fill=X, side = BOTTOM)

TopHeader =Label(root,text="We offer 10% fixed interest", bg = '#95C8F0',  fg = '#204399', font = 'Roboto, 40')
TopHeader.pack(side=TOP, fill= X, ipady = 18)  
#======================================================================
LeftLayoutForm =  Frame(root, bg='powderblue')
LeftLayoutForm.place(x=1, y=100, width=350, height=660)

loanUIDTxt = Label(LeftLayoutForm, text = "Loan UID", bg = 'powderblue', font = ("Roboto 18"))
loanUIDTxt.grid(row = 1, column = 0, padx=20, pady = 10, sticky="w")
LoanUID = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
LoanUID.grid(row = 2, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

FirstnameText = Label(LeftLayoutForm, text = "Firstname", bg = 'powderblue', font = ("Roboto 18"))
FirstnameText.grid(row = 3, column = 0, padx=20, pady = 10, sticky="w")
Firstname = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
Firstname.grid(row = 4, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

LastnameText = Label(LeftLayoutForm, text = "Lastname", bg = 'powderblue', font = ("Roboto 18"))
LastnameText.grid(row = 5, column = 0, padx=20, pady = 10, sticky="w")
Lastname = Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
Lastname.grid(row = 6, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

PrincipalText = Label(LeftLayoutForm, text = "Principal Amount", bg = 'powderblue', font = ("Roboto 18"))
PrincipalText.grid(row = 7, column = 0, padx=20, pady = 10, sticky="w")
Principal= Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
Principal.grid(row = 8, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

YearTermText = Label(LeftLayoutForm, text = "Loan Term (Year)", bg = 'powderblue', font = ("Roboto 18"))
YearTermText.grid(row = 9, column = 0, padx=20, pady = 10, sticky="w")
YearTerm= Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
YearTerm.grid(row = 10, column = 0, padx=20, pady=0, ipadx=20, ipady=3)

LTAText = Label(LeftLayoutForm, text = "Loan Total Amount", bg = 'powderblue', fg = '#204399', font = ("Roboto 18"))
LTAText.grid(row = 11, column = 0, padx=20, pady = 10, sticky="w")
LoanTotal= Entry(LeftLayoutForm, font= ("Roboto", 15), borderwidth = 2)
LoanTotal.grid(row = 12, column = 0, padx=20, pady=0, ipadx=20, ipady=3)
#================================================
DatabaseFrame = Frame(root, bg ="red")
DatabaseFrame.place(x= 350, y=100, width=900, height= 550)

parts_list = Listbox(DatabaseFrame, width = 70, height = 28, font ='consolas')
parts_list.grid(row=0, column=1,  pady = 0, padx = 0)
scrollbar = Scrollbar(DatabaseFrame, orient = VERTICAL)
scrollbar.grid(row=0, column=2, ipady = 257, padx = 0)

parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

parts_list.bind('<<ListboxSelect>>', select_item)

#================================================
btnFrame=Frame(root, bg ="#95C8F0")
btnFrame.place(x= 350,y=650,width=900, height=100)

add_btn = Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399', text = "Apply", command = add_item)
add_btn.grid(row = 2, column = 1,ipady = 12, ipadx = 25, pady= 20, padx = 25)

update_btn = Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399',  text = "Update", command = update_item)
update_btn.grid(row = 2, column = 2, ipady = 12, ipadx = 25, pady= 20, padx = 25)

del_btn= Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399',  text = "Delete", command = remove_item)
del_btn.grid(row = 2, column = 3, ipady = 12, ipadx = 25, pady= 20, padx = 25)

clear_btn = Button(btnFrame, font='Roboto 12 bold', bg='#FDDA0D', fg='#204399', text = "Clear", command = clear_text)
clear_btn.grid(row = 2, column = 4, ipady = 12, ipadx = 25, pady= 20, padx = 25)
populate_list()

root.mainloop()
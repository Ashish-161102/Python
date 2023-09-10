# import modules 
from tkinter import *
from tkinter import ttk
from linkdb import *
from tkinter import messagebox

# object for database
data = Database(db='link.db')

# global variables
count = 0
selected_rowid = 0

# functions
def saveRecord():
    global data
    data.insertRecord(link_name=link_name.get(), link_url=link_url.get())
       


def clearEntries():
    link_name.delete(0, 'end')
    link_url.delete(0, 'end')

def fetch_records():
    f = data.fetchRecord('select rowid, * from link_record')
    global count
    for rec in f:
        tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1], rec[2]))
        count += 1
    tv.after(400, refreshData)


def select_record(event):
    global selected_rowid
    selected = tv.focus()    
    val = tv.item(selected, 'values')
  
    try:
        selected_rowid = val[0]
        d = val[3]
        namevar.set(str[1])
        dopvar.set(str(d))
    except Exception as ep:
        pass


def update_record():
    global selected_rowid

    selected = tv.focus()
	# Update record
    try:
        data.updateRecord(namevar.get(), dopvar.get(), selected_rowid)
        tv.item(selected, text="", values=(namevar.get(), dopvar.get()))
    except Exception as ep:
        messagebox.showerror('Error',  ep)

	# Clear entry boxes
    link_name.delete(0, END)
    link_url.delete(0, END)
    tv.after(400, refreshData)
    



def refreshData():
    for item in tv.get_children():
      tv.delete(item)
    fetch_records()
    
def deleteRow():
    global selected_rowid
    data.removeRecord(selected_rowid)
    refreshData()

# create tkinter object
ws = Tk()
ws.title('Link Recorder')

# variables
f = ('Times new roman', 14)
namevar = StringVar()
dopvar = StringVar()

# Frame widget
f2 = Frame(ws)
f2.pack() 

f1 = Frame(
    ws,
    padx=10,
    pady=10,
)
f1.pack(expand=True, fill=BOTH)


# Label widget
Label(f1, text='LINK NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='LINK URL', font=f).grid(row=1, column=0, sticky=W)


# Entry widgets 
link_name = Entry(f1, font=f, textvariable=namevar)
link_url = Entry(f1, font=f, textvariable=dopvar)


# Entry grid placement
link_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
link_url.grid(row=1, column=1, sticky=EW, padx=(10, 0))



# Action buttons


submit_btn = Button(
    f1, 
    text='Save Record', 
    font=f, 
    command=saveRecord, 
    bg='#42602D', 
    fg='white'
    )

clr_btn = Button(
    f1, 
    text='Clear Entry', 
    font=f, 
    command=clearEntries, 
    bg='#D9B036', 
    fg='white'
    )

quit_btn = Button(
    f1, 
    text='Exit', 
    font=f, 
    command=lambda:ws.destroy(), 
    bg='#D33532', 
    fg='white'
    )



update_btn = Button(
    f1, 
    text='Update',
    bg='#C2BB00',
    command=update_record,
    font=f
)

del_btn = Button(
    f1, 
    text='Delete',
    bg='#BD2A2E',
    command=deleteRow,
    font=f
)

# grid placement

submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))

# Treeview widget
tv = ttk.Treeview(f2, columns=(1, 2, 3), show='headings', height=8)
tv.pack(side="left")

# add heading to treeview
tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)

tv.heading(1, text="Serial no")
tv.heading(2, text="Link Name", )
tv.heading(3, text="Link URL")


# binding treeview
tv.bind("<ButtonRelease-1>", select_record)

# style for treeview
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

# Vertical scrollbar
scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

# calling function 
fetch_records()

# infinite loop
ws.mainloop()
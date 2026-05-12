
from tkinter import * 
from tkinter.messagebox import *
from sqlite3 import *

def db_setup():
	con = None
	try:
		con = connect("profile.db")
		sql = "create table if not exists candidate(name text, phone int, gender text)"
		cursor = con.cursor()
		cursor.execute(sql)
		con.commit()
	except Exception as e:
		con.rollback()
		print("issue", e)
	finally:
		if con is not None:
			con.close()
db_setup()

def save():
	name = ent_name.get()
	phone = ent_phone.get()
	gender = ""
	if g.get() == 1:
		gender = "male"
	else:
		gender = "female"

	con = None
	try:
		con = connect("profile.db")
		sql = "insert into candidate values(?,?,?)"
		cursor = con.cursor()
		cursor.execute(sql, (name,phone,gender))
		con.commit()
		showinfo("success", "saved successfully")
		ent_name.delete(0, END)
		ent_phone.delete(0, END)
		g.set(1)
		ent_name.focus()
	except Exception as e:
		con.rollback()
		print("issue", e)
	finally:
		if con is not None:
			con.close() 

root = Tk()
root.title("Profile App")
root.geometry("1000x600+300+20")
f = ("Arial", 30, "bold")

lab_header = Label(root, text="Profile App", font=f)

lab_name = Label(root, text="Enter Name", font=f)
ent_name = Entry(root, font=f)

lab_phone = Label(root, text="Enter Phone", font=f)
ent_phone = Entry(root, font=f)

lab_gender = Label(root, text="Select Gender", font=f)

g = IntVar()
g.set(1)
rb_male = Radiobutton(root, text="Male", font=f, variable=g, value=1)
rb_female = Radiobutton(root, text="Female", font=f, variable=g, value=2)

btn_submit = Button(root, text="Submit", font=f, width=15, command=save)

lab_header.place(x=300, y=10)

lab_name.place(x=50, y=100)
ent_name.place(x=400, y=100)

lab_phone.place(x=50, y=200)
ent_phone.place(x=400, y=200)

lab_gender.place(x=50, y=300)
rb_male.place(x=400, y=300)
rb_female.place(x=600, y=300)

btn_submit.place(x=400, y=400)

root.mainloop()

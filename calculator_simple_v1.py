from ast import Lambda, operator
from tkinter import*
from tkinter.messagebox import RETRY
root=Tk()
root.title('Simple Calculator by Ashutosh Pathak')
#let's create an entry box feild
entry_box=Entry(root,width=55,fg='red',borderwidth=5)
#entry_box.insert(0)
entry_box.grid(row=0,column=0,columnspan=4)

#click here fun for click on num button
def click_here(number):
    current=entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,str(current)+str(number))

#clear key function
def clear_key():
    entry_box.delete(0,END)

#add key function
def add_key():
    number_1=entry_box.get()
    global var_1
    var_1=float(number_1)
    global operator_is
    operator_is='add'
    entry_box.delete(0,END)

#sub key function
def sub_key():
    number_1=entry_box.get()
    global var_1
    var_1=float(number_1)
    global operator_is
    operator_is='sub'
    entry_box.delete(0,END)

#div key function
def div_key():
    number_1=entry_box.get()
    global var_1
    var_1=float(number_1)
    global operator_is
    operator_is='div'
    entry_box.delete(0,END)

#mul key function
def mul_key():
    number_1=entry_box.get()
    global var_1
    var_1=float(number_1)
    global operator_is
    operator_is='mul'
    entry_box.delete(0,END)

#percentage key
def per_key():
    number_1=entry_box.get()
    global var_1
    var_1=float(number_1)
    entry_box.delete(0,END)
    entry_box.insert(0,var_1/100)



#equla key
def equal_key():

    if operator_is=='add':
            new_var=float(entry_box.get())
            entry_box.delete(0,END)
            entry_box.insert(0,var_1 + new_var)
    if operator_is=='div':
            new_var=float(entry_box.get())
            entry_box.delete(0,END)
            entry_box.insert(0,var_1 /  new_var)
    if operator_is=='sub':
            new_var=float(entry_box.get())
            entry_box.delete(0,END)
            entry_box.insert(0,var_1 - new_var)
    if operator_is=='mul':
            new_var=float(entry_box.get())
            entry_box.delete(0,END)
            entry_box.insert(0,var_1 * new_var)
    

#mentioning all the buttons 


button_7=Button(root,text='7',padx=40,pady=20,command=lambda:click_here(7))
button_8=Button(root,text='8',command=lambda:click_here(8),padx=40,pady=20)
button_9=Button(root,text='9',command=lambda:click_here(9),padx=40,pady=20)
button_add=Button(root,text='+',command=add_key,padx=40,pady=20,fg='blue')

button_4=Button(root,text='4',command=lambda:click_here(4),padx=40,pady=20)
button_5=Button(root,text='5',command=lambda:click_here(5),padx=40,pady=20)
button_6=Button(root,text='6',command=lambda:click_here(6),padx=40,pady=20)
button_sub=Button(root,text='-',command=sub_key,padx=40,pady=20,fg='blue')

button_1=Button(root,text='1',command=lambda:click_here(1),padx=40,pady=20)
button_2=Button(root,text='2',command=lambda:click_here(2),padx=40,pady=20)
button_3=Button(root,text='3',command=lambda:click_here(3),padx=40,pady=20)
button_mul=Button(root,text='*',command=mul_key,padx=40,pady=20,fg='blue')

button_0=Button(root,text='0',command=lambda:click_here(0),padx=40,pady=20)
button_dot=Button(root,text='.',command=lambda:click_here('.'),padx=40,pady=20,fg='green')
button_back=Button(root,text='%',command=per_key,padx=40,pady=20,fg='green')
button_div=Button(root,text='/',command=div_key,padx=40,pady=20,fg='blue')

button_clear=Button(root,text='clear',command=clear_key,padx=40,pady=20,fg='red')
#button_0=Button(root,text='1',command=lambda:click_here(),padx=40
#,pady=200,)
#button_0=Button(root,text='1',command=lambda:click_here(),padx=40
#,pady=200,)
button_ans=Button(root,text='ANS',command=equal_key,padx=40,pady=20,fg='red')


#gridding all buttons to rows and columns

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_back.grid(row=4,column=2)
button_div.grid(row=4,column=3)

button_clear.grid(row=5,column=0)
#button_0.grid(row=,column=1)
#button_0.grid(row=,column=2)
button_ans.grid(row=5,column=3)





root.mainloop()
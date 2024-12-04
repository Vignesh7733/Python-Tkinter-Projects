from tkinter import *
import tkinter.messagebox as msg
import joblib
from tkinter import ttk

model=joblib.load('Online Sales')

root= Tk()
root.title('Payment Method Machine Output')
root.geometry('900x600')
bg_image=PhotoImage(file='Online Sales.png')
bg_label=Label(root,image=bg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


Topheadingframe=Frame(root,width=700,bd=1)
Topheadingframe.pack(side=TOP)
Heading=Label(Topheadingframe,text='Online Sales',fg='white',bg='red',font=('Helvetica',30),)
Heading.grid(row=0,column=0,padx=10,pady=10)

midframe=Frame(root,width=700,bd=1)
midframe.pack(side=TOP)
midframe=Label(midframe,bg='pink',font=('Helvetica',15),)
midframe.grid(row=0,column=0,padx=10,pady=10)

Product_Category=IntVar()
Product_Name=IntVar()
Units_Sold=IntVar()
Units_Price=IntVar()
Total_Revenue=IntVar()
Region=IntVar()
Day=IntVar()
Month=IntVar()
Year=IntVar()

Product_Category.set('')
Product_Name.set('')
Units_Sold.set('')
Units_Price.set('')
Total_Revenue.set('')
Region.set('')
Day.set('')
Month.set('')
Year.set('')

one=Label(midframe,text='Product Category',fg='black',bg='goldenrod',font=('Helvetica',15))
one.grid(row=0,column=0,padx=10,pady=10)
two=Label(midframe,text='Product Name',fg='black',bg='goldenrod',font=('Helvetica',15))
two.grid(row=1,column=0,padx=10,pady=10)
three=Label(midframe,text='Units Sold',fg='black',bg='goldenrod',font=('Helvetica',15))
three.grid(row=2,column=0,padx=10,pady=10)
four=Label(midframe,text='Unit Price',fg='black',bg='goldenrod',font=('Helvetica',15))
four.grid(row=3,column=0,padx=10,pady=10)
five=Label(midframe,text='Total Revenue',fg='black',bg='goldenrod',font=('Helvetica',15))
five.grid(row=4,column=0,padx=10,pady=10)
six=Label(midframe,text='Region',fg='black',bg='goldenrod',font=('Helvetica',15))
six.grid(row=5,column=0,padx=10,pady=10)
seven=Label(midframe,text='Day',fg='black',bg='goldenrod',font=('Helvetica',15))
seven.grid(row=6,column=0,padx=10,pady=10)
eight=Label(midframe,text='Month',fg='black',bg='goldenrod',font=('Helvetica',15))
eight.grid(row=7,column=0,padx=10,pady=10)
nine=Label(midframe,text='Year',fg='black',bg='goldenrod',font=('Helvetica',15))
nine.grid(row=8,column=0,padx=10,pady=10)

one1=Entry(midframe,textvariable=Product_Category,font=('Helvetica',15))
one1.grid(row=0,column=1,padx=10,pady=10)
two1=Entry(midframe,textvariable=Product_Name,font=('Helvetica',15))
two1.grid(row=1,column=1,padx=10,pady=10)
three1=Entry(midframe,textvariable=Units_Sold,font=('Helvetica',15))
three1.grid(row=2,column=1,padx=10,pady=10)
four1=Entry(midframe,textvariable=Units_Price,font=('Helvetica',15))
four1.grid(row=3,column=1,padx=10,pady=10)
five1=Entry(midframe,textvariable=Total_Revenue,font=('Helvetica',15))
five1.grid(row=4,column=1,padx=10,pady=10)
six1=Entry(midframe,textvariable=Region,font=('Helvetica',15))
six1.grid(row=5,column=1,padx=10,pady=10)
seven1=Entry(midframe,textvariable=Day,font=('Helvetica',15))
seven1.grid(row=6,column=1,padx=10,pady=10)
eight1=Entry(midframe,textvariable=Month,font=('Helvetica',15))
eight1.grid(row=7,column=1,padx=10,pady=10)
nine1=Entry(midframe,textvariable=Year,font=('Helvetica',15))
nine1.grid(row=8,column=1,padx=10,pady=10)


def predict():
    for i in model.predict([[(Product_Category.get()),(Product_Name.get()),(Units_Sold.get()),
                                        (Units_Price.get()),(Total_Revenue.get()),(Region.get()),
                                        (Day.get()),(Month.get()),(Year.get())]]):
        if i==1:
            msg.showinfo('Payment Method','Credit card',icon='info')
        elif i==2:
             msg.showinfo('Payment Method','Paypal',icon='info')
        elif i==3:
             msg.showinfo('Payment Method','Debit card',icon='info')
        else:
            pass

sub=Button(midframe,text='Submit',fg='white',bg='red',font=('Helvetica',15),command=predict)
sub.grid(row=9,column=1,padx=10,pady=10)
root.mainloop()

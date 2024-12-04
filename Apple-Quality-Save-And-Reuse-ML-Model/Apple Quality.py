from tkinter import *
import tkinter.messagebox as msg
import joblib
from tkinter import ttk

model = joblib.load('Apple quality - KNN.ipynb')

root = Tk()
root.title('Apple Quality Machine Output')
root.geometry('900x600')
bg_image = PhotoImage(file='Apple img.png')
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Topheadingframe = Frame(root, width=700, bd=1)
Topheadingframe.pack(side=TOP)
Heading = Label(Topheadingframe, text='Apple Quality', fg='white', bg='red', font=('Helvetica', 30), )
Heading.grid(row=0, column=0, padx=10, pady=10)

midframe = Frame(root, width=700, bd=1)
midframe.pack(side=TOP)
midframe = Label(midframe, bg='teal', font=('Helvetica', 15), )
midframe.grid(row=0, column=0, padx=10, pady=10)

Size = IntVar()
Weight = IntVar()
Sweetness = IntVar()
Crunchiness = IntVar()
Juiciness = IntVar()
Ripeness = IntVar()
Acidity = IntVar()

Size.set('')
Weight.set('')
Sweetness.set('')
Crunchiness.set('')
Juiciness.set('')
Ripeness.set('')
Acidity.set('')

one = Label(midframe, text='Size', fg='white', bg='Brown', font=('Helvetica', 15))
one.grid(row=0, column=0, padx=10, pady=10)
two = Label(midframe, text='Weight', fg='white', bg='Brown', font=('Helvetica', 15))
two.grid(row=1, column=0, padx=10, pady=10)
three = Label(midframe, text='Sweetness', fg='white', bg='Brown', font=('Helvetica', 15))
three.grid(row=2, column=0, padx=10, pady=10)
four = Label(midframe, text='Crunchiness', fg='white', bg='Brown', font=('Helvetica', 15))
four.grid(row=3, column=0, padx=10, pady=10)
five = Label(midframe, text='Juiciness', fg='white', bg='Brown', font=('Helvetica', 15))
five.grid(row=4, column=0, padx=10, pady=10)
six = Label(midframe, text='Ripeness', fg='white', bg='Brown', font=('Helvetica', 15))
six.grid(row=5, column=0, padx=10, pady=10)
seven = Label(midframe, text='Acidity', fg='white', bg='Brown', font=('Helvetica', 15))
seven.grid(row=6, column=0, padx=10, pady=10)

one1 = Entry(midframe, textvariable=Size, font=('Helvetica', 15))
one1.grid(row=0, column=1, padx=10, pady=10)
two1 = Entry(midframe, textvariable=Weight, font=('Helvetica', 15))
two1.grid(row=1, column=1, padx=10, pady=10)
three1 = Entry(midframe, textvariable=Sweetness, font=('Helvetica', 15))
three1.grid(row=2, column=1, padx=10, pady=10)
four1 = Entry(midframe, textvariable=Crunchiness, font=('Helvetica', 15))
four1.grid(row=3, column=1, padx=10, pady=10)
five1 = Entry(midframe, textvariable=Juiciness, font=('Helvetica', 15))
five1.grid(row=4, column=1, padx=10, pady=10)
six1 = Entry(midframe, textvariable=Ripeness, font=('Helvetica', 15))
six1.grid(row=5, column=1, padx=10, pady=10)
seven1 = Entry(midframe, textvariable=Acidity, font=('Helvetica', 15))
seven1.grid(row=6, column=1, padx=10, pady=10)


def predict():
    for i in model.predict([[(Size.get()), (Weight.get()), (Sweetness.get()),
                             (Crunchiness.get()), (Juiciness.get()), (Ripeness.get()),
                             (Acidity.get())]]):
        msg.showinfo('Quality', f'{i}', icon='info')


sub = Button(midframe, text='Submit', fg='white', bg='red', font=('Helvetica', 15), command=predict)
sub.grid(row=9, column=1, padx=10, pady=10)
root.mainloop()

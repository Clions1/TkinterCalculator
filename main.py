import tkinter
from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(500, 300)


#reuslt_entry





#result_entry


#numpad
button1 = Button(text="1", width=3)
button1.place(x=100, y=50)

button2 = Button(text="2", width=3)
button2.place(x=150, y=50)

button3 = Button(text="3", width=3)
button3.place(x=200, y=50)

button4 = Button(text="4", width=3)
button4.place(x=100, y=100)

button5 = Button(text="5", width=3)
button5.place(x=150, y=100)

button6 = Button(text="6" , width=3)
button6.place(x=200 , y=100)

button7=Button(text="7", width=3)
button7.place(x=100, y=150)

button8=Button(text="8", width=3)
button8.place(x=150, y=150)

button9=Button(text="9", width=3)
button9.place(x=200, y=150)

button0=Button(text="0", width=3)
button0.place(x=150, y=200)

#numpad

#configurations

buttonA=Button(text="+",width=3 , height=1)
buttonA.place(x=300 , y=50)

buttonB=Button(text="-",width=3 , height=1)
buttonB.place(x=350 , y=50)

buttonC=Button(text="*",width=3 ,height=1)
buttonC.place(x=400,y=50)

buttonC=Button(text="/",width=3 ,height=1)
buttonC.place(x=450,y=50)

#configurations

window.mainloop()

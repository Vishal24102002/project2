import pip
try:
  pip.main(["install"],["tk"])
  pip.main(["install"],["pyttsx3"])
  import pyttsx3
  from tkinter import *
except:
  import pyttsx3
  from tkinter import *

Vikas=tk()
Vikas.geometry("300x250")
Vikas.maxsize(300,250)
Vikas.minsize(300,250)
Vikas.title("Speach converter")
Vikas.configure(bg="black")

def speak():
   Engine=pt.init()
   Engine.say(Entry.get())
   Voices=engine.getProperty('voices') 
   print(Voices) 
   engine.setProperty('voice',Voices[1].id) 
   engine.runAndWait()

   

entry_label=Label(Vikas,text=" ")
entry_label.grid(row=0,column=0)

entry1_label=Label(Vikas,text=" ")
entry1_label.grid(row=0,column=4)

Entry=StringVar()

Text=Entry(Vikas,textvariable=Entry,font=('calibre',12,'normal'))
Text.grid(row=4,column=3,columnspan=4)

Speak=Button(vikas,text="convert",activebackground="blue",command=speak)
Speak.grid(row=5,column=3,columnspan=4)

Vikas.mainloop()
  

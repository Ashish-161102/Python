from tkinter import *
import pyttsx3
import os


#init
root = Tk()
root.title("Text to Audio Converter")
root.geometry("720x550")
root.configure(background="#E3516E")

#head
bookTitle = Label(root, text="Text to Audio Converter", font=("Arial", 30), bg="#FADE8B")
bookTitle.place(x=250,y=30)


#enter content
Label1 = Label(root,text="Enter content to read",bg="#FADE8B")
Label1.place(x=200,y=100)

entry1 = Text(root,width=50,height=20,border=10)
entry1.place(x=200,y=140)

button1 = Button(root,text="Submit",command=lambda: myClick(),bg="#51B5A9")
button1.place(x=350,y=100)



def myClick():
    hello = entry1.get(1.0,END)

    
    
    speaker.say(hello)
    speaker.runAndWait()

    
    entry1.delete(1.0,END)



#for gtts
language = 'en'







#speaker init
speaker = pyttsx3.init()
speaker.setProperty("rate", 178)



root.mainloop()
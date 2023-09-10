from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import PyPDF2

# Init
root = Tk()
root.title('AudioBook Player')
root.geometry("400x620")

speaker = pyttsx3.init()
speaker.setProperty("rate", 178)

book = open("Harry_Potter.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

# Book Title
bookTitle = Label(root, text="Harry Potter", font=("Arial", 30))
bookTitle.place(x=200, y=30, anchor="center")

# Book Cover
bookCover = ImageTk.PhotoImage(Image.open("cover.jpeg"))
image = Label(image=bookCover).place(x=90, y=70)

# Function
def readBook(chapter):
    if chapter == 1:
        for num in range(2, 13):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 2:
        for num in range(13, 23):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 3:
        for num in range(24, 35):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 4:
        for num in range(36, 47):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 5:
        for num in range(48, 69):
            page = pdfReader.getPage(num)
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 6:
        for num in range(70, 91):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 7:
        for num in range(92, 105):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 8:
        for num in range(106, 114):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 9:
        for num in range(115, 131):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()

    elif chapter == 10:
        for num in range(132, 144):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()


# Buttons
chapter1 = Button(root, text="Chapter 1",command=lambda: readBook(1)).place(x=50, y=420)
chapter2 = Button(root, text="Chapter 2",command=lambda: readBook(2)).place(x=170, y=420)
chapter3 = Button(root, text="Chapter 3",command=lambda: readBook(3)).place(x=290, y=420)

chapter4 = Button(root, text="Chapter 4",command=lambda: readBook(4)).place(x=50, y=470)
chapter5 = Button(root, text="Chapter 5",command=lambda: readBook(5)).place(x=170, y=470)
chapter6 = Button(root, text="Chapter 6",command=lambda: readBook(6)).place(x=290, y=470)

chapter7 = Button(root, text="Chapter 7",command=lambda: readBook(7)).place(x=50, y=520)
chapter8 = Button(root, text="Chapter 8",command=lambda: readBook(8)).place(x=170, y=520)
chapter9 = Button(root, text="Chapter 9",command=lambda: readBook(9)).place(x=290, y=520)

chapter10 = Button(root, text="Chapter 10",command=lambda: readBook(10)).place(x=168, y=570)

# Main Loop
root.mainloop()

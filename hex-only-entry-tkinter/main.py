from tkinter import *


def request_format(entry):
    text = entry.get()
    for i in range(len(text)):
        if not text[i] in ('A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            entry.delete(0, END)
            entry.insert(0, text[:-1])


guiApp = Tk()
guiApp.title("Hex Only Entry")

label = Label(guiApp, text="Enter Hex Digit: [A-F, 0-9]")
label.pack()
hexEntryText = StringVar()
hexEntry = Entry(guiApp, textvariable=hexEntryText, width=30)
hexEntryText.trace("w", lambda name, index, mode, hexEntryText=hexEntryText: request_format(hexEntry))
hexEntry.pack()

guiApp.mainloop()
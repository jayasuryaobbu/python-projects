import base64
from tkinter import *
from PIL import Image, ImageTk
import io

guiApp = Tk()
guiApp.title("Base64 to Image Converter")
guiApp.iconbitmap()

logoData = '<Replace with base64 string of image>'

logo = base64.b64decode(logoData)
image = Image.open(io.BytesIO(logo))
img = ImageTk.PhotoImage(image)
logo = Label(guiApp, image=img)
logo.pack()

guiApp.mainloop()

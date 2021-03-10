"""
Screenshot App by Jay - 10/03/20
Github: mr-circuit
"""

import pyautogui
import os
import tkinter as tk

root = tk.Tk()
root.title("Screenshot App")

i = 0

window_frame = tk.Canvas(root, width=450, height=35)
window_frame.pack()


def capture_screenshot():
    global i
    i += 1
    pyautogui.screenshot('screenshot' + str(i) + '.png')


def delete_last_file():
    global i
    os.remove('screenshot' + str(i) + '.png')
    i -= 1


def delete_screenshot():
    global i
    while i != 0:
        os.remove('screenshot' + str(i) + '.png')
        i -= 1


screenshot_button = tk.Button(text='Take Screenshot', command=capture_screenshot, bg='maroon', fg='white', font=10)
window_frame.create_window(90, 20, window=screenshot_button)

clear_button = tk.Button(text='Clear All', command=delete_screenshot, bg='red', fg='white', font=10)
window_frame.create_window(220, 20, window=clear_button)

delete_button = tk.Button(text='Delete Last One', command=delete_last_file, bg='black', fg='white', font=10)
window_frame.create_window(350, 20, window=delete_button)

root.mainloop()

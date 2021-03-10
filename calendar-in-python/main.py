import calendar
import tkinter
from tkinter import messagebox
import tkinter.font as text_font
from tkinter import ttk
from datetime import date

root = tkinter.Tk()
root.title("Calendar in Python")
heading_font = text_font.Font(size=25)
subheading_font = text_font.Font(size=12)


today = date.today()
this_month = int(today.strftime("%m"))
this_year = int(today.strftime("%Y"))
new_month_val = 0
new_year_val = 0
year_val = int(today.strftime("%Y"))
month_combo_box_val = int(today.strftime("%m"))

window_frame = tkinter.Canvas(root, width=500, height=500)
window_frame.pack()


def only_numbers(char):
    return char.isdigit()


validation = root.register(only_numbers)

heading = tkinter.Label(root, text='Calendar in Python', font=heading_font)
window_frame.create_window(250, 20, window=heading)

year_label = tkinter.Label(root, text='Enter the year: ', font=subheading_font)
window_frame.create_window(80, 80, window=year_label)

year_field = tkinter.Entry(root, validate="key", validatecommand=(validation, '%S'))
window_frame.create_window(220, 80, window=year_field)

month_label = tkinter.Label(root, text='Select the month: ', font=subheading_font)
window_frame.create_window(80, 120, window=month_label)

month_combo_box = tkinter.ttk.Combobox(root, values=('January', 'February', 'March', 'April', 'May', 'June', 'July',
                                                     'August', 'September', 'October', 'November', 'December'))
month_combo_box.insert(tkinter.END, 'Select Your Month')
month_combo_box.bind("<<>ComboboxSelected>")
window_frame.create_window(220, 120, window=month_combo_box)


def clear_data():
    result_field.delete(1.0, tkinter.END)


def reset():
    result_field.delete(1.0, tkinter.END)
    year_field.delete(0, 'end')
    month_combo_box.set('Select Your Month')


def today_calendar():
    reset()
    result_field.insert(tkinter.END, calendar.month(this_year, this_month))


result_field = tkinter.Text(root)
window_frame.create_window(140, 300, width=165, height=120, window=result_field)
today_calendar()


def next_month():
    global year_val
    global month_combo_box_val
    global new_month_val
    try:
        year_val = int(year_field.get())
        new_month_val += 1
        month_combo_box_val = new_month_val + month_combo_box.current() + 1
        if month_combo_box_val == 13:
            year_field.delete(0, 'end')
            year_val += 1
            year_field.insert(tkinter.END, str(year_val))
            month_combo_box.set('January')
            new_month_val = 0
            month_combo_box_val = new_month_val + month_combo_box.current() + 1
            calculation_func()
        else:
            calculation_func()
    except:
        messagebox.showerror('No Data', 'Please Enter Appropriate Fields')


def previous_month():
    global year_val
    global month_combo_box_val
    global new_month_val
    try:
        year_val = int(year_field.get())
        new_month_val -= 1
        month_combo_box_val = new_month_val + month_combo_box.current() + 1
        if month_combo_box_val == 0:
            year_field.delete(0, 'end')
            year_val -= 1
            year_field.insert(tkinter.END, str(year_val))
            month_combo_box.set('December')
            new_month_val = 0
            month_combo_box_val = new_month_val + month_combo_box.current() + 1
            calculation_func()
        else:
            calculation_func()

    except:
        messagebox.showerror('No Data', 'Please Enter Appropriate Fields')


def next_year():
    global year_val
    global month_combo_box_val
    try:
        if year_val == int(today.strftime("%Y")) and month_combo_box_val == int(today.strftime("%m")):
            year_field.delete(0, 'end')
            year_field.insert(0, today.strftime("%Y"))
            year_val = int(year_field.get())
            month_combo_box.set(today.strftime("%B"))
            month_combo_box_val = month_combo_box.current() + 1
            year_field.delete(0, 'end')
            year_val += 1
            year_field.insert(tkinter.END, str(year_val))
            calculation_func()
        else:
            year_val = int(year_field.get())
            month_combo_box_val = month_combo_box.current() + 1
            year_field.delete(0, 'end')
            year_val += 1
            year_field.insert(tkinter.END, str(year_val))
            calculation_func()

    except:
        messagebox.showerror('No Data', 'Please Enter Appropriate Fields')


def previous_year():
    global year_val
    global month_combo_box_val
    try:
        if year_val == int(today.strftime("%Y")) and month_combo_box_val == int(today.strftime("%m")):
            year_field.delete(0, 'end')
            year_field.insert(0, today.strftime("%Y"))
            year_val = int(year_field.get())
            month_combo_box.set(today.strftime("%B"))
            month_combo_box_val = month_combo_box.current() + 1
            year_field.delete(0, 'end')
            year_val -= 1
            year_field.insert(tkinter.END, str(year_val))
            calculation_func()
        else:
            year_val = int(year_field.get())
            month_combo_box_val = month_combo_box.current() + 1
            year_field.delete(0, 'end')
            year_val -= 1
            year_field.insert(tkinter.END, str(year_val))
            calculation_func()

    except:
        messagebox.showerror('No Data', 'Please Enter Appropriate Fields')


def get_values():
    global year_val
    global month_combo_box_val
    try:
        year_val = int(year_field.get())
        month_combo_box_val = month_combo_box.current() + 1
        calculation_func()
    except:
        messagebox.showerror('No Data', 'Please Enter Appropriate Fields')


def special_days(which_month):
    if which_month == 7:
        special_day_field.delete(0.0, tkinter.END)
        special_day_field.insert(tkinter.END, 'Middle Day in Year')
    elif which_month == 0:
        special_day_field.delete(1.0, tkinter.END)


special_day_field = tkinter.Text(root)
window_frame.create_window(360, 300, width=250, height=120, window=special_day_field)


def calculation_func():
    global month_combo_box_val
    global year_val
    if month_combo_box_val == 7:
        special_days(7)
        cal_val_july = calendar.month(year_val, month_combo_box_val)
        clear_data()
        result_field.insert(tkinter.END, cal_val_july)
        birthday = "2"
        if birthday:
            first_index = '2.0'
            while 1:
                first_index = result_field.search(birthday, first_index, nocase=1, stopindex='4.8')
                if not first_index:
                    break
                last_index = '%s+%dc' % (first_index, len(birthday))
                result_field.tag_add('found', first_index, last_index)
                first_index = last_index
                result_field.see(first_index)
            result_field.tag_config('found', foreground='red')
    else:
        special_days(0)
        cal_val = calendar.month(year_val, month_combo_box_val)
        clear_data()
        result_field.insert(tkinter.END, cal_val)


button = tkinter.ttk.Button(root, text='Click Me!', command=get_values)
window_frame.create_window(80, 160, window=button)

today_button = tkinter.ttk.Button(root, text='Today\'s Calender', command=today_calendar)
window_frame.create_window(200, 160, window=today_button)

next_month_button = tkinter.ttk.Button(root, text='>', command=next_month)
window_frame.create_window(185, 227, window=next_month_button)

previous_month_button = tkinter.ttk.Button(root, text='<', command=previous_month)
window_frame.create_window(96, 227, window=previous_month_button)

reset_button = tkinter.ttk.Button(root, text='Reset', command=reset)
window_frame.create_window(320, 160, window=reset_button)

next_year_button = tkinter.ttk.Button(root, text='>>', command=next_year)
window_frame.create_window(185, 372, window=next_year_button)

previous_year_button = tkinter.ttk.Button(root, text='<<', command=previous_year)
window_frame.create_window(96, 372, window=previous_year_button)


root.mainloop()


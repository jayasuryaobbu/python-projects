from tkinter import *
from tkinter import messagebox


def clear_all():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)


def check_error():
    if (dayField.get() == "" or monthField.get() == ""
            or yearField.get() == "" or givenDayField.get() == ""
            or givenMonthField.get() == "" or givenYearField.get() == ""):
        messagebox.showerror("Input Error")
        clear_all()
        return -1


def calculate_age():
    value = check_error()
    if value == -1:
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if birth_day > given_day:
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        if birth_month > given_month:
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))


if __name__ == '__main__':

    root = Tk()
    root.config(background='light green')
    root.title('Age Calculator')
    root.geometry('525x260')

    dob = Label(root, bg='blue')
    givenDate = Label(root, text='Given Date', bg='blue')
    birthDate = Label(root, text='Birth Date', bg='blue')

    day = Label(root, text='Day', bg='light green')
    month = Label(root, text='Month', bg='light green')
    year = Label(root, text='Year', bg='light green')

    givenDay = Label(root, text="Given Day", bg="light green")
    givenMonth = Label(root, text="Given Month", bg="light green")
    givenYear = Label(root, text="Given Year", bg="light green")

    rsltYear = Label(root, text="Years", bg="light green")
    rsltMonth = Label(root, text="Month", bg="light green")
    rsltDay = Label(root, text="Days", bg="light green")

    dayField = Entry(root)
    monthField = Entry(root)
    yearField = Entry(root)

    givenDayField = Entry(root)
    givenMonthField = Entry(root)
    givenYearField = Entry(root)

    rsltYearField = Entry(root)
    rsltMonthField = Entry(root)
    rsltDayField = Entry(root)

    resultantAge = Button(root, text="Resultant Age", fg="Black", bg="Red", command=calculate_age)

    clearAllEntry = Button(root, text="Clear All Output", fg='Black', bg='Red', command=clear_all)

    dob.grid(row=0, column=1)
    day.grid(row=1, column=0)
    dayField.grid(row=1, column=1)
    month.grid(row=2, column=0)
    monthField.grid(row=2, column=1)
    year.grid(row=3, column=0)
    yearField.grid(row=3, column=1)
    givenDate.grid(row=0, column=4)
    birthDate.grid(row=0, column=1)
    givenDay.grid(row=1, column=3)
    givenDayField.grid(row=1, column=4)
    givenMonth.grid(row=2, column=3)
    givenMonthField.grid(row=2, column=4)
    givenYear.grid(row=3, column=3)
    givenYearField.grid(row=3, column=4)
    resultantAge.grid(row=4, column=2)
    rsltYear.grid(row=5, column=2)
    rsltYearField.grid(row=6, column=2)
    rsltMonth.grid(row=7, column=2)
    rsltMonthField.grid(row=8, column=2)
    rsltDay.grid(row=9, column=2)
    rsltDayField.grid(row=10, column=2)
    clearAllEntry.grid(row=12, column=2)

    root.mainloop()

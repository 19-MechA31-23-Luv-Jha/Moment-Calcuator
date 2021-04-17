from tkinter import *
from tkinter import messagebox


def get_mass():
    mass = float(ENTRY3.get())
    return mass


def get_radius_1():
    radius1 = float(ENTRY1.get())
    return radius1


def get_radius_2():
    radius2 = float(ENTRY2.get())
    return radius2


def moment_of_inertia_of_angular_pipe(a = " "):
    try:

        mass = get_mass()
        radius1 = get_radius_1()
        radius2 = get_radius_2()

        moment = mass * (pow(radius1, 2) + pow(radius2, 2)) / 2
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")

    else:
        messagebox.showinfo("Result", moment)


if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", moment_of_inertia_of_angular_pipe)
    TOP.geometry("400x400")
    TOP.configure(background="#307678")
    TOP.title("Moment Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#307678", text="Welcome to Moment Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter radius_1:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter radius_2:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=55, y=121)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=121)
    LABLE3 = Label(TOP, bg="#cef0f1", text="Enter mass:", bd=6,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE3.place(x=55, y=171)
    ENTRY3 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY3.place(x=240, y=171)
    BUTTON = Button(bg="#2187e7", bd=12, text="Moment", padx=33, pady=15, command=moment_of_inertia_of_angular_pipe,
                    font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=250)
    TOP.mainloop()
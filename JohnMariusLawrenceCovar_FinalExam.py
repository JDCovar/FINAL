def main():
    from tkinter import *
    window = Tk()
    # Find the least number among three numbers
    L = []
    window.title(num1 = eval(input("Enter the first number:")))
    window.geometry("500x300")
    btn=Button(window, text = "Enter the first number:",)
    btn.place(x=200, y=150)

    L.append(num1)
    window.title(num2 = eval(input("Enter the second number:")))
    window.geometry("500x30")
    btn = Button(window, text="Enter the second number:", )
    btn.place(x=200, y=300)

    L.append(num2)
    window.title(num3 = eval(input("Enter the third number:")))
    window.geometry("500x300")
    btn = Button(window, text="Enter the third number:", )
    btn.place(x=200, y=450)

    L.append(num3)
    window.title(print("The smallest number among the three is:",str(min(L))))
    window.geometry("500x300")
    btn = Button(window, text="The smallest number among the three is:", )
    btn.place(x=200, y=600)

    window.mainloop()
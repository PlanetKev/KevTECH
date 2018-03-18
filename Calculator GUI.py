from tkinter import *
import math
master = Tk()
display = Entry(master, width=11, justify='right', bd=0, bg='lightgrey')

master.title("Calculator")


class Calculator:

    def __init__(self):
        self.var1 = ""  # First number
        self.var2 = ""  # Second number
        self.result = 0  # Final Answer
        self.current = 0    # Is it your first number or second number being entered
        self.operator = 0   # Are you multiplying, dividing, subtracting, etc

    def numb_butt(self, index):
        if self.current is 0:  # If you are typing the first number
            self.var1 = str(self.var1 + str(index))   # Makes var1 the user's first number
            display.delete(0, END)
            display.insert(0, string=self.var1)
        else:   # Else you are entering in the second number
            self.var2 = str(self.var2 + str(index))   # Makes var2 the user's second number
            display.delete(0, END)
            display.insert(0, string=self.var2)

    def equate(self):   # Find the final answer
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)   # Add
        elif self.operator is 1:
            self.result = float(self.var1) - float(self.var2)   # Subtract
        elif self.operator is 2:
            self.result = float(self.var1) * float(self.var2)   # Multiply
        elif self.operator is 3:
            self.result = float(self.var1) / float(self.var2)   # Divide
        elif self.operator is 4:
            self.result = float(math.sqrt(float(self.var1)))
        elif self.operator is 5:
            self.result = float(float(self.var1)**2)
        elif self.operator is 6:
            self.result = float(float(self.var1) ** float(self.var2))
        elif self.operator is 7:
            self.result = float(float(self.var1)**3)
        elif self.operator is 8:
            self.result = float(math.factorial(float(self.var1)))
        elif self.operator is 9:
            self.result = round(float(math.sin(float(self.var1))), 3)
        elif self.operator is 10:
            self.result = round(float(math.cos(float(self.var1))), 3)
        elif self.operator is 11:
            self.result = round(float(math.tan(float(self.var1))), 3)

        display.delete(0, END)  # Gets rid of anything on the line
        display.insert(0, string=self.result)   # Updates the display with the final answer

    def set_op(self, op):
        self.operator = op  # Sets operator equal to the input
        display.delete(0, END)  # Clear out display
        if self.current is 0:
            self.current = 1  # Makes sure we're editing the second variable
        else:
            self.equate()
            self.var2 = ""

    def clear(self):     # Clear button
        self.__init__()     # Resets everything and clears the screen
        display.delete(0, END)   # Clears the screen


calc = Calculator()
# Create the number buttons 1-9
b0 = Button(master, text="0", command=lambda: calc.numb_butt(0))
b1 = Button(master, text="1", command=lambda: calc.numb_butt(1))
b2 = Button(master, text="2", command=lambda: calc.numb_butt(2))
b3 = Button(master, text="3", command=lambda: calc.numb_butt(3))
b4 = Button(master, text="4", command=lambda: calc.numb_butt(4))
b5 = Button(master, text="5", command=lambda: calc.numb_butt(5))
b6 = Button(master, text="6", command=lambda: calc.numb_butt(6))
b7 = Button(master, text="7", command=lambda: calc.numb_butt(7))
b8 = Button(master, text="8", command=lambda: calc.numb_butt(8))
b9 = Button(master, text="9", command=lambda: calc.numb_butt(9))

# Button for a decimal point
b_dot = Button(master, text=".", command=lambda: calc.numb_butt("."))

# Operator buttons
plus = Button(master, text="+", command=lambda: calc.set_op(0))
minus = Button(master, text="-", command=lambda: calc.set_op(1))
times = Button(master, text="*", command=lambda: calc.set_op(2))
divide = Button(master, text="/", command=lambda: calc.set_op(3))
sqrt = Button(master, text="√x", command=lambda: calc.set_op(4))
square = Button(master, text="x^2", command=lambda: calc.set_op(5))
nth_power = Button(master, text="x^n", command=lambda: calc.set_op(6))
cube = Button(master, text="x^3", command=lambda: calc.set_op(7))
factorial = Button(master, text="x!", command=lambda: calc.set_op(8))
sine = Button(master, text="sin", command=lambda: calc.set_op(9)).grid(row=0, column=5)
cosine = Button(master, text="cos", command=lambda: calc.set_op(10)).grid(row=1, column=5)
tangent = Button(master, text="tan", command=lambda: calc.set_op(11)).grid(row=2, column=5)
# Equal and Clear Sign
equals = Button(master, text="=", command=calc.equate)
clear = Button(master, text="c", command=calc.clear)

# *** Positioning Button ***
display.place(x=0, y=2)     # Places the display for the result at (0,2)

# Program the specific buttons at specific locations-
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=4, column=0)

b_dot.grid(row=4, column=1)
clear.grid(row=4, column=2)

plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
times.grid(row=2, column=3)
divide.grid(row=3, column=3)
sqrt.grid(row=0, column=4)
equals.grid(row=4, column=3)
square.grid(row=1, column=4)
nth_power.grid(row=3, column=4)
cube.grid(row=2, column=4)
factorial.grid(row=4, column=4)
master.mainloop()    # Initiates the class





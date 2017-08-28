from tkinter import *

class Calculator:

    def __init__(self, master):

            # frame widget created as container for other widgets
        frame = Frame(master)
            # frame uses grid geometry, N+E+W+S sticky makes frame expand
            # on all sides when window is resized
        frame.grid(sticky=N+E+W+S)

            # define and initialize variables for calculator class
            # first_val and second_val are the two numbers being operated on
            # operand denotes the operation to perform on the two values
        self.first_val = 0
        self.second_val = 0
        self.operand = "="       

            # calculator display as a label widget
        self.display = Label(
            frame, text=str(self.first_val), font=("Verdana", 12), anchor=E, justify=RIGHT, \
            fg="black", bg = "white")
            # position calculator display using grid geometry
        self.display.grid(row=0, column=0, columnspan=3, padx = 3, pady = 6, \
        sticky=N+E+W+S)

            # variables used as offsets for grid row/column placement
            # useful if more buttons are to be added (or removed) later
        i, j = 1, 0
        
            # calculator buttons defined as button widgets
            # note that the command (for button press) uses lambda functions
            # this is required to ensure evaluation only happens during
            # runtime when the corresponding button is pressed
        self.num7 = Button(frame, text="7", command=lambda: self.num_press("7"))
        self.num7.grid(row=i+0, column=j+0, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num8 = Button(frame, text="8", command=lambda: self.num_press("8"))
        self.num8.grid(row=i+0, column=j+1, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num9 = Button(frame, text="9", command=lambda: self.num_press("9"))
        self.num9.grid(row=i+0, column=j+2, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num4 = Button(frame, text="4", command=lambda: self.num_press("4"))
        self.num4.grid(row=i+1, column=j+0, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num5 = Button(frame, text="5", command=lambda: self.num_press("5"))
        self.num5.grid(row=i+1, column=j+1, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num6 = Button(frame, text="6", command=lambda: self.num_press("6"))
        self.num6.grid(row=i+1, column=j+2, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num1 = Button(frame, text="1", command=lambda: self.num_press("1"))
        self.num1.grid(row=i+2, column=j+0, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num2 = Button(frame, text="2", command=lambda: self.num_press("2"))
        self.num2.grid(row=i+2, column=j+1, padx = 3, pady = 3, sticky=N+E+W+S)
        self.num3 = Button(frame, text="3", command=lambda: self.num_press("3"))
        self.num3.grid(row=i+2, column=j+2, padx = 3, pady = 3, sticky=N+E+W+S)

        self.num0 = Button(frame, text="0", command=lambda: self.num_press("0"))
        self.num0.grid(row=i+2, column=j+3, padx = 3, pady = 3, sticky=N+E+W+S)

        self.dlt = Button(frame, text="DLT", command=lambda: self.dlt_press())
        self.dlt.grid(row=i-1, column=j+3, padx = 3, pady = 3, sticky=N+E+W+S)
        self.clr = Button(frame, text="CLR", command=lambda: self.clr_press())
        self.clr.grid(row=i-1, column=j+4, padx = 3, pady = 3, sticky=N+E+W+S)

        self.add = Button(frame, text=" + ", command=lambda: self.op_press("+"))
        self.add.grid(row=i+0, column=j+3, padx = 3, pady = 3, sticky=N+E+W+S)
        self.sub = Button(frame, text=" - ", command=lambda: self.op_press("-"))
        self.sub.grid(row=i+0, column=j+4, padx = 3, pady = 3, sticky=N+E+W+S)
        self.mul = Button(frame, text=" * ", command=lambda: self.op_press("*"))
        self.mul.grid(row=i+1, column=j+3, padx = 3, pady = 3, sticky=N+E+W+S)
        self.div = Button(frame, text=" / ", command=lambda: self.op_press("/"))
        self.div.grid(row=i+1, column=j+4, padx = 3, pady = 3, sticky=N+E+W+S)
        self.eql = Button(frame, text=" = ", command=lambda: self.eql_press())
        self.eql.grid(row=i+2, column=j+4, padx = 3, pady = 3, sticky=N+E+W+S)

        # gives each element in frame a non-zero weight in order
        # to allow proper resizing if window is resized
        for p in range(5):
            Grid.columnconfigure(frame, p, weight=1)
        for q in range(4):
            Grid.rowconfigure(frame, q, weight=1)

        # method for changing display when a number button is pressed
    def num_press(self, number):
        if(self.first_val == 0 and self.second_val == 0 and self.operand == "="):
            self.first_val = int(number)
            self.display.config(text=str(self.first_val))
        elif(self.first_val != 0 and self.second_val == 0 and self.operand == "="):
            self.first_val = (10*self.first_val) + int(number)
            self.display.config(text=str(self.first_val))
        elif(self.second_val == 0 and self.operand != "="):
            self.second_val = int(number)
            self.display.config(text=str(self.first_val) + self.operand + str(self.second_val))
        elif(self.second_val != 0 and self.operand != "="):
            self.second_val = (10*self.second_val) + int(number)
            self.display.config(text=str(self.first_val) + self.operand + str(self.second_val))
        else:
            self.display.config(text="error in number entry")

        # method for changing display when an operand button is pressed
        # multiple operand presses does not cause errors
    def op_press(self, op):
        self.second_val = 0
        self.operand = op
        self.display.config(text=str(self.first_val) + self.operand)

        # method for changing display when the clear button is pressed
    def clr_press(self):
        self.first_val = 0
        self.second_val = 0
        self.operand = "="
        self.display.config(text=str(self.first_val))

        # method for changing display when the delete button is pressed
        # first elif is edge case for first_val being a negative number
        # due to the last performed operation, changes display to zero
    def dlt_press(self):
        if(self.first_val == 0 and self.second_val == 0 and self.operand == "="):
            pass
        elif(self.first_val < 0 and self.second_val == 0):
            self.first_val = 0
            self.display.config(text=str(self.first_val))
        elif(self.first_val != 0 and self.second_val == 0 and self.operand == "="):
            self.first_val = (self.first_val // 10)
            self.display.config(text=str(self.first_val))
        elif(self.first_val != 0 and self.second_val == 0 and self.operand != "="):
            self.operand = "="
            self.display.config(text=str(self.first_val))
        elif(self.first_val != 0 and self.second_val != 0 and self.operand != "="):
            self.second_val = (self.second_val // 10)
            self.display.config(text=str(self.first_val) + self.operand + str(self.second_val))
        else:
            self.display.config(text="error in deleting number")

        # method for performing calculation and changing display to show 
        # the result when the '=' button is pressed
        # passes if operand is not +,-,* or / and changes operand to default
        # value of '=' to prevent multiple '=' presses from causing errors
    def eql_press(self):
        if(self.operand == "+"):
            self.first_val = self.first_val + self.second_val
            self.second_val = 0
            self.display.config(text=str(self.first_val))
        elif(self.operand == "-"):
            self.first_val = self.first_val - self.second_val
            self.second_val = 0
            self.display.config(text=str(self.first_val))
        elif(self.operand == "*"):
            self.first_val = self.first_val * self.second_val
            self.second_val = 0
            self.display.config(text=str(self.first_val))
        elif(self.operand == "/"):
            self.first_val = self.first_val // self.second_val
            self.second_val = 0
            self.display.config(text=str(self.first_val))
        else:
            pass
        self.operand = "="


if __name__ == "__main__":
    
        # create root window
    root = Tk()
    root.wm_title("Simple Calculator")
        # assign weight root grid (not really needed in this case)
    Grid.columnconfigure(root, 0, weight=1)
    Grid.rowconfigure(root, 0, weight=1)
        # create calculator app as child of root
    calc = Calculator(root)

    root.update()
        # ensures calculator is centered on screen when opened
    rw, rh = root.winfo_width(), root.winfo_height()
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (sw/2)-(rw), (sh/2)-(rh)
    root.geometry('%dx%d+%d+%d' % (2*rw,2*rh,x,y))
    
        # event loop for program
    root.mainloop()


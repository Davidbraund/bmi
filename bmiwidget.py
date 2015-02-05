import tkinter
import tkinter.filedialog
import tkinter.messagebox
import bmiutils


class bmi_window(): 
    def __init__(self): 
        self.app = tkinter.Tk()

        self.setup_ui()
        
        # Confirm quitting the application
        self.app.wm_protocol("WM_DELETE_WINDOW", self.confirm_quit)

        self.app.mainloop()


    def confirm_quit(self):
        """ Ask the user for confirmation they want to close the program """
        if(tkinter.messagebox.askokcancel(
                                          "Quit", 
                                          "Do you really want to quit?")):
            self.app.destroy()


    def setup_ui(self):

        # Yes this is somewhat of a long function
        # Todo: Clean up
        self.weight_label = tkinter.Label(
            self.app,
            text = "Weight (kg)",
            justify = tkinter.LEFT
        )

        self.weight_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT
        )

        self.length_label = tkinter.Label(
            self.app,
            text = "Length (m)",
            justify = tkinter.LEFT
        )

        self.length_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT
        )

        self.calculate_button = tkinter.Button(
            self.app,
            text = "Calculate",
            command = self.calculate,
            justify = tkinter.RIGHT
        )

        self.bmi_label = tkinter.Label(
            self.app,
            text = "BMI",
            justify = tkinter.LEFT
        )

        self.bmi_result = tkinter.Label(
            self.app,
            text = "0",
            justify = tkinter.RIGHT,
        )

        self.weight_label.grid(row = 0, column = 0)
        self.weight_entry.grid(row = 0, column = 1)
        self.length_label.grid(row = 1, column = 0)
        self.length_entry.grid(row = 1, column = 1)
        self.calculate_button.grid(row = 2, column = 1, sticky = tkinter.E, 
                                   padx = 20)
        self.bmi_label.grid(row = 4, column = 0)
        self.bmi_result.grid(row = 4, column = 1, sticky = tkinter.E, 
                             padx = 20)

    def calculate(self):
        self.bmi_result.config(text = bmiutils.bmi(self.length_entry, self.weight_entry))

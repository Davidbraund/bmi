import tkinter
import tkinter.messagebox
import bmiutils


class BmiWindow(): 
    def __init__(self):
        self.app = tkinter.Tk()

        self.setup_ui()

        # Confirm quitting the application
        #self.app.wm_protocol("WM_DELETE_WINDOW", self.confirm_quit)

        # Bind Enter to calculate
        self.app.bind('<Return>', self.calculate)

        self.app.mainloop()


    def setup_ui(self):
        """ Sets up the UI itself. Placing the buttons and entry
        fields """

        # Todo: Clean up to make shorter
        self.length_label = tkinter.Label(
            self.app,
            text = "Length (cm)",
            justify = tkinter.LEFT
        )

        self.length_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
        )

        self.weight_label = tkinter.Label(
            self.app,
            text = "Weight (kg)",
            justify = tkinter.LEFT
        )

        self.weight_entry = tkinter.Entry(
            self.app,
            justify = tkinter.RIGHT,
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

        self.length_label.grid(row = 0, column = 0)
        self.length_entry.grid(row = 0, column = 1)
        self.weight_label.grid(row = 1, column = 0)
        self.weight_entry.grid(row = 1, column = 1)
        self.calculate_button.grid(row = 2, column = 1, sticky = tkinter.E, 
                                   padx = 20)
        self.bmi_label.grid(row = 4, column = 0)
        self.bmi_result.grid(row = 4, column = 1, sticky = tkinter.E, 
                             padx = 20)


    def calculate(self, event = None):
        """ Calculates and updates the BMI result """
        self.bmi_result.config(text = "{0:.1f}".format(bmiutils.bmi(
            self.length_entry.get(),
            self.weight_entry.get())))


    def confirm_quit(self):
        """ Ask the user for confirmation they want to close the
        program """
        if(tkinter.messagebox.askokcancel("Quit",
                                          "Do you really want to quit?")):
            self.app.destroy()


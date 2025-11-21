# MPG Calculator
# Dalila Spencer
# 2025-11-19

import tkinter as tk
import tkinter.messagebox

class MpgCalculator:
    def __init__(self, window):

        # create main window
        self.main_window = tk.Tk()

        # create frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # create top frame widgets
        self.prompt1_label = tk.Label(self.top_frame, text='How many gallons of gas can the car hold?: ')
        self.gallons_entry = tk.Entry(self.top_frame, width=10)

        # pack top frame
        self.prompt1_label.pack(side='left', pady=5)
        self.gallons_entry.pack(side='left', pady=5)

        # create middle frame widgets
        self.prompt2_label = tk.Label(self.mid_frame, text='How many miles can the car drive on a full tank?: ')
        self.miles_entry = tk.Entry(self.mid_frame, width=10)

        # pack mid frame
        self.prompt2_label.pack(side='left',pady=5)
        self.miles_entry.pack(side='left',pady=5)

        # create bottom frame button widgets
        self.calc_button = tk.Button(self.bottom_frame, text='Calculate', command=self.calculate)

        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        # pack buttons
        self.calc_button.pack(side='left', padx=10, pady=10)
        self.quit_button.pack(side='left', padx=10, pady=10)

        # pack frames
        self.top_frame.pack(side='top', padx=10, pady=10)
        self.mid_frame.pack(side='top', padx=10, pady=10)
        self.bottom_frame.pack(side='top', padx=10, pady=10)

        # enter main loop
        tk.mainloop()

    def calculate(self):
        # get tank size
        gallons = float(self.gallons_entry.get())
        # get number of miles
        miles = float(self.miles_entry.get())

        # calculate miles per gallon
        mpg = miles / gallons

        mpg = round(mpg, 2)

        # display results
        tk.messagebox.showinfo('Results', 'Your car can drive ' + str(mpg) + ' miles on one gallon of gas.')

# create instance
if __name__ == '__main__':
    MPG = MpgCalculator(tk)



# Joe's Automotive
# Dalila Spencer
# 2025-11-20

import tkinter as tk
import tkinter.messagebox

class Automotive:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Joe\'s Automotive")

        # creates frames
        self.desc_frame = tk.Frame(self.window)
        self.cb_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)

        # creates desc label
        self.desc = tk.Label(self.desc_frame, text="What maintenance would you like?: ")

        # pack desc
        self.desc.pack(side= 'left', padx = 10, pady = 10)

        # create intvars
        self.oil_var = tk.IntVar()
        self.lube_var = tk.IntVar()
        self.radiator_var = tk.IntVar()
        self.fluid_var = tk.IntVar()
        self.inspect_var = tk.IntVar()
        self.muffler_var = tk.IntVar()
        self.tire_var = tk.IntVar()

        # set intvars to 0
        self.oil_var.set(0)
        self.lube_var.set(0)
        self.radiator_var.set(0)
        self.fluid_var.set(0)
        self.inspect_var.set(0)
        self.muffler_var.set(0)
        self.tire_var.set(0)

        # create cb widgets
        self.oil_cb = tk.Checkbutton(self.cb_frame, text="Oil Change - $30.00", variable=self.oil_var)
        self.lube_cb = tk.Checkbutton(self.cb_frame, text="Lube Job - $20.00", variable=self.lube_var)
        self.radiator_cb = tk.Checkbutton(self.cb_frame, text="Radiator Flush - $40.00", variable=self.radiator_var)
        self.fluid_cb = tk.Checkbutton(self.cb_frame, text="Transmission Fluid - $100.00", variable=self.fluid_var)
        self.inspect_cb = tk.Checkbutton(self.cb_frame, text="Inspection - $35.00", variable=self.inspect_var)
        self.muffler_cb = tk.Checkbutton(self.cb_frame, text="Muffler replacement - $200.00", variable=self.muffler_var)
        self.tire_cb = tk.Checkbutton(self.cb_frame, text="Tire Rotation - $20.00", variable=self.tire_var)

        # pack cbs
        self.oil_cb.pack(padx = 20)
        self.lube_cb.pack(padx = 20)
        self.radiator_cb.pack(padx = 20)
        self.fluid_cb.pack(padx = 20)
        self.inspect_cb.pack(padx = 20)
        self.muffler_cb.pack(padx = 20)
        self.tire_cb.pack(padx = 20)

        # create ok and quit buttons
        self.ok_button = tk.Button(self.button_frame, text='Ok', command=self.calc_cost)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.window.destroy)

        # pack buttons
        self.ok_button.pack(side = 'left', padx = 10, pady = 20)
        self.quit_button.pack(side = 'left', padx = 10, pady = 20)

        # pack frames
        self.desc_frame.pack()
        self.cb_frame.pack()
        self.button_frame.pack()

        # mainloop
        self.window.mainloop()

    def calc_cost(self):

        total = 0.0

        if self.oil_var.get() == 1:
            total += 30.00
        if self.lube_var.get() == 1:
            total += 20.00
        if self.radiator_var.get() == 1:
            total += 40.00
        if self.fluid_var.get() == 1:
            total += 100.00
        if self.inspect_var.get() == 1:
            total += 35.00
        if self.muffler_var.get() == 1:
            total += 200.00
        if self.tire_var.get() == 1:
            total += 20.00

        tkinter.messagebox.showinfo('Total', f'Your total cost is: ${total:.2f}' )

if __name__ == '__main__':
    automotive = Automotive()



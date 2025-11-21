# Long-Distance Calls
# Dalila Spencer
# 2025-11-20

import tkinter as tk
import tkinter.messagebox

class Calls:
    def __init__(self):
        self.window = tk.Tk()

        # create frames
        self.left_frame = tk.Frame(self.window)
        self.right_frame = tk.Frame(self.window)
        self.middle_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        # create desc labels
        self.time_label = tk.Label(self.left_frame, text="Rate Category")
        self.rate_label = tk.Label(self.right_frame, text="Rate per Minute")

        # create intvar for radio button
        self.radio_var = tk.IntVar()

        # set intvar
        self.radio_var.set(1)

        # create rb widgets
        self.daytime = tk.Radiobutton(self.left_frame, text='Daytime (6:00 A.M. through 5:59 P.M.)', variable=self.radio_var, value=1)
        self.evening = tk.Radiobutton(self.left_frame, text='Evening (6:00 P.M.  through 11:59 P.M.)', variable=self.radio_var, value=2)
        self.off_peak = tk.Radiobutton(self.left_frame, text='Off-Peak (midnight through 5:59 A.M.)', variable=self.radio_var, value=3)

        # create rate labels
        self.day_rate = tk.Label(self.right_frame, text='$0.02')
        self.evening_rate = tk.Label(self.right_frame, text='$0.12')
        self.off_peak_rate = tk.Label(self.right_frame, text='$0.05')

        # pack left frame
        self.time_label.pack(side='top', padx=50, pady=10)
        self.daytime.pack(side='top', padx=50, pady=10)
        self.evening.pack(side='top', padx=50, pady=10)
        self.off_peak.pack(side='top', padx=50, pady=10)

        # pack right frame
        self.rate_label.pack(side='top', padx=50, pady=10)
        self.day_rate.pack(side='top', padx=50, pady=10)
        self.evening_rate.pack(side='top', padx=50, pady=10)
        self.off_peak_rate.pack(side='top', padx=50, pady=10)

        # create minutes prompt and entry box
        self.minutes_label = tk.Label(self.middle_frame, text="How many minutes long is your call?:")
        self.minutes_entry = tk.Entry(self.middle_frame, width=10)

        # pack middle frame
        self.minutes_label.pack(side='left', pady=20)
        self.minutes_entry.pack(side='left', pady=20)

        # create ok and quit buttons
        self.ok_button = tk.Button(self.bottom_frame, text='Ok', command=self.calc_fee)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.window.destroy)

        # pack bottom frame
        self.ok_button.pack(side='left', padx=20, pady=20)
        self.quit_button.pack(side='left', padx=20, pady=20)

        # pack frames
        self.left_frame.pack(side='left')
        self.right_frame.pack(side='left')
        self.middle_frame.pack(side='top', padx=20, pady=20)
        self.bottom_frame.pack(side='top', padx=20, pady=20)

        # mainloop
        self.window.mainloop()

    def calc_fee(self):

        rate = 0.0

        if self.radio_var.get() == 1:
            rate = 0.02
        if self.radio_var.get() == 2:
            rate = 0.12
        if self.radio_var.get() == 3:
            rate = 0.05

        fee = float(self.minutes_entry.get()) * rate

        tk.messagebox.showinfo('Total Fee', f'Your total fee is: ${fee:.2f}')
# create instance
if __name__ == '__main__':
    calls = Calls()



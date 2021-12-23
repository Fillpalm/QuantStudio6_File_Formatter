from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functions96to96r import *
import pandas as pd


#modified from https://www.youtube.com/watch?v=ytPw-_EE4KE&ab_channel=ParwizForogh
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Plate Maker")
        self.minsize(640,400)

        self.labelFrame = ttk.LabelFrame(self, text="Select a file")
        self.labelFrame.grid(column = 0 ,row = 1, padx=20, pady=20)

        self.button()
        self.button4()


        self.filename=""


    def button(self):
        self.label = ttk.Label(self.labelFrame, text="Plate:")
        self.label.grid(column=1, row=0)
        self.button= ttk.Button(self.labelFrame, text="Browse", command=self.fileDialog)
        self.button.grid(column=1,row=1)
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/Downloads",title="select a file")
        self.label=ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1,row=2)
        self.label.configure(text=self.filename)

    # converter button to convert the four selected files and put the output on desktop
    def button4(self):
        self.button4 = ttk.Button(self.labelFrame, text="Convert", command=self.converter)
        self.button4.grid(column=3, row=5)

    def converter(self):
        # get File destination and name
        self.fileOut = filedialog.asksaveasfilename(initialdir="/Users/INSTR-ADMIN/Desktop/QS 6 Import Files", title="select a destination",defaultextension=".txt",filetypes=(("txt","*.txt"),("all","*.*")))

        # Convert the file
        df = convert_file(self.filename)
        df = df.sort_values(by="Well")

        f = open(self.fileOut, "w")
        input = "[Sample Setup]" + "\n"
        f.write(input)
        f.close()

        df.to_csv(self.fileOut, sep='\t', index=False,mode='a') # write out
        #add pc and nc lines
        target = ["IC", "RNaseP", "SARS"]
        reporter = ["TAMRA", "CY5", "FAM"]
        a = ["95", "NC", "H11"]
        b = ["96", "PC", "H12"]
        lasts = [a, b]

        f = open(self.fileOut, "a")
        for y in lasts:
            for x in range(0, 3):
                lastline = y[0] + "\t" + y[2] + "\t" + y[1] + "\t" + target[x] + "\t" + "UNKNOWN" + "\t" + reporter[
                    x] + "\t" + "none"+'\n'
                f.write(lastline)
        f.close()

        # confirmation message once completed
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=3, row=7)
        self.label.configure(text="File Created!")


if __name__=="__main__":
    root = Root()
    root.mainloop()
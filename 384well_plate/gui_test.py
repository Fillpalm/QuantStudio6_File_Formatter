from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functions import *
import pandas as pd


#modified from https://www.youtube.com/watch?v=ytPw-_EE4KE&ab_channel=ParwizForogh
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Plate Maker")
        self.minsize(640,400)

        self.labelFrame = ttk.LabelFrame(self, text="Select 1-4 files")
        self.labelFrame.grid(column = 0 ,row = 1, padx=20, pady=20)

        self.button()
        self.button1()
        self.button2()
        self.button3()
        self.button4()

        self.filename=""
        self.filename1 = ""
        self.filename2 = ""
        self.filename3 = ""

    def button(self):
        self.label = ttk.Label(self.labelFrame, text="Plate1:")
        self.label.grid(column=1, row=0)
        self.button= ttk.Button(self.labelFrame, text="Browse", command=self.fileDialog)
        self.button.grid(column=1,row=1)
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/Downloads",title="select a file")
        self.label=ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1,row=2)
        self.label.configure(text=self.filename)

    def button1(self):
        self.label = ttk.Label(self.labelFrame, text="Plate2:")
        self.label.grid(column=1, row=3)
        self.button1= ttk.Button(self.labelFrame, text="Browse", command=self.fileDialog1)
        self.button1.grid(column=1,row=4)
    def fileDialog1(self):
        self.filename1 = filedialog.askopenfilename(initialdir="/Downloads",title="select a file")
        self.label=ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1,row=5)
        self.label.configure(text=self.filename1)

    def button2(self):
        self.label = ttk.Label(self.labelFrame, text="Plate3:")
        self.label.grid(column=1, row=6)
        self.button2 = ttk.Button(self.labelFrame, text="Browse", command=self.fileDialog2)
        self.button2.grid(column=1, row=7)
    def fileDialog2(self):
        self.filename2 = filedialog.askopenfilename(initialdir="/Downloads", title="select a file")
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=8)
        self.label.configure(text=self.filename2)

    def button3(self):
        self.label = ttk.Label(self.labelFrame, text="Plate4:")
        self.label.grid(column=1, row=9)
        self.button3 = ttk.Button(self.labelFrame, text="Browse", command=self.fileDialog3)
        self.button3.grid(column=1, row=10)
    def fileDialog3(self):
        self.filename3 = filedialog.askopenfilename(initialdir="/Downloads", title="select a file")
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=11)
        self.label.configure(text=self.filename3)



#converter button to convert the four selected files and put the output on desktop
    def button4(self):
        self.button4 = ttk.Button(self.labelFrame, text="Convert", command=self.converter)
        self.button4.grid(column=3, row=5)
    def converter(self):
        #get File destination and name
        self.fileOut = filedialog.asksaveasfilename(initialdir="/Users/INSTR-ADMIN/Desktop/QS 6 Import Files", title="select a destination",defaultextension=".txt",filetypes=(("txt","*.txt"),("all","*.*")))

        #Convert the four files to one
        dfs=[]
        df1 = convert_file(1, self.filename)
        dfs.append(df1)
        try:
            df2 = convert_file(2, self.filename1)
            dfs.append(df2)
        except:
            pass
        try:
            df3 = convert_file(3, self.filename2)
            dfs.append(df3)
        except:
            pass
        try:
            df4 = convert_file(4, self.filename3)
            dfs.append(df4)
        except:
            pass
        df = pd.concat(dfs)
        df = df.sort_values(by="Well")

        f = open(self.fileOut, "w")
        input="[Sample Setup]"+"\n"
        f.write(input)
        f.close()

        #write df to csv
        df.to_csv(self.fileOut, sep='\t', index=False, mode='a')

        #add controls at the end
        target = ["IC", "RNaseP", "SARS"]
        reporter = ["TAMRA", "CY5", "FAM"]
        a = ["360", "NC", "O24"]
        b = ["383", "NC", "P23"]
        c = ["384", "PC", "P24"]
        d = ["359", "PC", "O23"]
        lasts = [a, b, c, d]

        f = open(self.fileOut, "a")
        for y in lasts:
            for x in range(0, 3):
                lastline = y[0] + "\t" + y[2] + "\t" + y[1] + "\t" + target[x] + "\t" + "UNKNOWN" + "\t" + reporter[
                    x] + "\t" + "none"+'\n'
                f.write(lastline)
        f.close()

        #confirmation message once completed
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=3, row=7)
        self.label.configure(text="File Created!")



if __name__=="__main__":
    root = Root()
    root.mainloop()



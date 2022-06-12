import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
class App:
    def __init__(self, root):
        #setting title
        root.title("E-Defter Module")
        #setting window size
        width=864
        height=569
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.coveredDate_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.coveredDate=tk.Checkbutton(root, variable=self.coveredDate_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(1, self.coveredDate_var, "Covered Date"))
        self.coveredDate.place(x=30,y=40,width=130,height=15)

        self.coveredDate_start_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.coveredDate_start=tk.Checkbutton(root, variable=self.coveredDate_start_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date Start", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(2, self.coveredDate_start_var, "Covered Date Start"))
        self.coveredDate_start.place(x=60,y=70,width=130,height=20)

        self.coveredDate_end_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.coveredDate_end=tk.Checkbutton(root, variable=self.coveredDate_end_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date End", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(3, self.coveredDate_end_var, "Covered Date End"))
        self.coveredDate_end.place(x=60,y=100,width=130,height=20)

        self.fiscalYear_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.fiscalYear=tk.Checkbutton(root, variable=self.fiscalYear_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(4, self.fiscalYear_var, "Fiscal Year"))
        self.fiscalYear.place(x=245,y=40,width=130,height=20)

        self.fiscalYear_start_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.fiscalYear_start=tk.Checkbutton(root, variable=self.fiscalYear_start_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year Start", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(5, self.fiscalYear_start_var, "Fiscal Year Start"))
        self.fiscalYear_start.place(x=285,y=70,width=120,height=20)

        self.fiscalYear_end_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.fiscalYear_end=tk.Checkbutton(root, variable=self.fiscalYear_end_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year End", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(6, self.fiscalYear_end_var, "Fiscal Year End"))
        self.fiscalYear_end.place(x=285,y=100,width=120,height=20)

        self.enteredDate_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.enteredDate=tk.Checkbutton(root, variable=self.enteredDate_var, font=ft, fg="#000000", 
        justify="center", text="Entered Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(7, self.enteredDate_var, "Entered Date"))
        self.enteredDate.place(x=440,y=40,width=130,height=20)

        self.entry_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.entry=tk.Checkbutton(root, variable=self.entry_var, font=ft, fg="#000000", 
        justify="center", text="Entries", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(8, self.entry_var, "Entries"))
        self.entry.place(x=630,y=40,width=130,height=20)

        self.entry_comment_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.entry_comment=tk.Checkbutton(root, variable=self.entry_comment_var, font=ft, fg="#000000", 
        justify="center", text="Entry Comment", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(9, self.entry_comment_var, "Entry Comment"))
        self.entry_comment.place(x=680,y=70,width=117,height=20)

        self.entry_number_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.entry_number=tk.Checkbutton(root, variable=self.entry_number_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(10, self.entry_number_var, "Entry Number"))
        self.entry_number.place(x=680,y=100,width=110,height=20)

        self.totalCredit_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.totalCredit=tk.Checkbutton(root, variable=self.totalCredit_var, font=ft, fg="#000000", 
        justify="center", text="Total Credit", offvalue="0", onvalue="1",
        command=lambda: self.checkboxPressed(11, self.totalCredit_var, "Total Credit"))
        self.totalCredit.place(x=30,y=170,width=112,height=20)

        self.totalDebit_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.totalDebit=tk.Checkbutton(root, variable=self.totalDebit_var, font=ft, fg="#000000", 
        justify="center", text="Total Debit", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(12, self.totalDebit_var, "Total Debit"))
        self.totalDebit.place(x=30,y=210,width=110,height=20)

        self.entryNumberCounter_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.entryNumberCounter=tk.Checkbutton(root, variable=self.entryNumberCounter_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number Counter", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(13, self.entryNumberCounter_var, "Entry Number Counter"))
        self.entryNumberCounter.place(x=30,y=250,width=170,height=20)

        self.debitCardCode_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.debitCardCode=tk.Checkbutton(root, variable=self.debitCardCode_var, font=ft, fg="#000000", 
        justify="center", text="Debit Card Code", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(14, self.debitCardCode_var, "Debit Card Code"))
        self.debitCardCode.place(x=30,y=290,width=140,height=20)

        self.postingDate_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.postingDate=tk.Checkbutton(root, variable=self.postingDate_var, font=ft, fg="#000000", 
        justify="center", text="Posting Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(15, self.postingDate_var, "Posting Date"))
        self.postingDate.place(x=30,y=330,width=120,height=20)

        self.documentReference_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.documentReference=tk.Checkbutton(root, variable=self.documentReference_var, font=ft, fg="#000000", 
        justify="center", text="Document Reference", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(16, self.documentReference_var, "Document Reference"))
        self.documentReference.place(x=30,y=370,width=160,height=20)

        self.detailComment_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.detailComment=tk.Checkbutton(root, variable=self.detailComment_var, font=ft, fg="#000000", 
        justify="center", text="Detail Comment", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(17, self.detailComment_var, "Detail Comment"))
        self.detailComment.place(x=30,y=410,width=130,height=20)

        self.selectAll_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=16)
        self.selectAll=tk.Checkbutton(root, variable=self.selectAll_var, font=ft, fg="#000000", 
        justify="center", text="Select All", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(18, self.selectAll_var, "Select All"))
        self.selectAll.place(x=50,y=470,width=130,height=20)
        

    def checkboxPressed(self, columnNum, varName, textDesc):
        print("Value is", varName.get())
        print("Column Value is", columnNum)
        print(textDesc)
        

    # def totalCredit_command(self):
    #     print("Value is", self.totalCredit_var.get())
    #     print("Total Credit")
        

    # def entry_number_command(self):
    #     print("Value is", self.entry_number_var.get())
    #     print("Entry Number")
        

    # def entry_comment_command(self):
    #     print("Value is", self.entry_comment_var.get())
    #     print("Entry Comment")
        

    # def entry_command(self):
    #     print("Value is", self.entry_var.get())
    #     print("Entries")
        

    # def enteredDate_command(self):
    #     print("Value is", self.enteredDate_var.get())
    #     print("Entered Date")
        

    # def fiscalYear_end_command(self):
    #     print("Value is", self.fiscalYear_end_var.get())
    #     print("fiscal Year end")
        

    # def fiscalYear_start_command(self):
    #     print("Value is", self.fiscalYear_start_var.get())
    #     print("fiscal Year Start")
        

    # def fiscalYear_command(self):
    #     print("Value is", self.fiscalYear_var.get())
    #     print("fiscal Year")
        

    # def coveredDate_end_command(self):
    #     print("Value is", self.coveredDate_end_var.get())
    #     print("covered date End")

    # def coveredDate_start_command(self):
    #     print("Value is", self.coveredDate_start_var.get())
    #     print("covered date start")

    # def coveredDate_command(self):
    #     print("Value is", self.coveredDate_var.get())
    #     print("covered date")

if __name__ == "__main__":
    root = tk.Tk()
    canvas=Canvas(root, width=1000, height=1000)
    
    # This is for Covered Date
    canvas.create_line(54, 45, 54, 110, fill="black", width=1)
    canvas.create_line(55, 79, 65, 79, fill="black", width=1)
    canvas.create_line(55, 109, 65, 109, fill="black", width=1)

    # This is for Fiscal Year
    canvas.create_line(277, 45, 277, 110, fill="black", width=1)
    canvas.create_line(277, 79, 283, 79, fill="black", width=1)
    canvas.create_line(277, 109, 283, 109, fill="black", width=1)

    # This is for Entry
    canvas.create_line(672, 45, 672, 110, fill="black", width=1)
    canvas.create_line(672, 79, 680, 79, fill="black", width=1)
    canvas.create_line(672, 109, 680, 109, fill="black", width=1)
    canvas.pack()
    app = App(root)
    root.mainloop()

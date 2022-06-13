import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from pathlib import PurePosixPath
import xml.etree.ElementTree as ET
from tkinter import filedialog as fd
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

        # This is for the Lines =======================
        canvas=Canvas(root, width=864, height=569)
    
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

        # This is for Line
        canvas.create_line(278, 180, 278, 240, fill="black", width=1)
        canvas.create_line(278, 210, 284, 210, fill="black", width=1)
        canvas.create_line(278, 240, 284, 240, fill="black", width=1)

        # This is for Account
        canvas.create_line(470, 170, 470, 331, fill="black", width=1)
        canvas.create_line(470, 331, 478, 331, fill="black", width=1)
        canvas.create_line(470, 301, 478, 301, fill="black", width=1)
        canvas.create_line(470, 271, 478, 271, fill="black", width=1)
        canvas.create_line(470, 241, 478, 241, fill="black", width=1)
        canvas.create_line(470, 211, 478, 211, fill="black", width=1)
        canvas.pack()

        # END of Lines ====================

        self.coveredDate_var = tk.IntVar()
        self.coveredDate_start_var = tk.IntVar()
        self.coveredDate_end_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)

        listOfAllChildren = []

        coveredDateChildren = [self.coveredDate_start_var, self.coveredDate_end_var]
        self.coveredDate=tk.Checkbutton(root, variable=self.coveredDate_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.coveredDate_var, coveredDateChildren, True))
        self.coveredDate.place(x=30,y=40,width=130,height=15)
        listOfAllChildren.append(self.coveredDate_var)
        listOfAllChildren.extend(coveredDateChildren)

        self.coveredDate_start=tk.Checkbutton(root, variable=self.coveredDate_start_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date Start", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.coveredDate_var, [self.coveredDate_start_var], False))
        self.coveredDate_start.place(x=60,y=70,width=130,height=20)
        
        self.coveredDate_end=tk.Checkbutton(root, variable=self.coveredDate_end_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date End", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.coveredDate_var, [self.coveredDate_end_var], False))
        self.coveredDate_end.place(x=60,y=100,width=130,height=20)


        self.fiscalYear_var = tk.IntVar()
        self.fiscalYear_start_var = tk.IntVar()
        self.fiscalYear_end_var = tk.IntVar()

        fiscalYearChildren = [self.fiscalYear_start_var, self.fiscalYear_end_var]
        self.fiscalYear=tk.Checkbutton(root, variable=self.fiscalYear_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.fiscalYear_var, fiscalYearChildren, True))
        self.fiscalYear.place(x=245,y=40,width=130,height=20)
        listOfAllChildren.append(self.fiscalYear_var)
        listOfAllChildren.extend(fiscalYearChildren)

        self.fiscalYear_start=tk.Checkbutton(root, variable=self.fiscalYear_start_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year Start", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.fiscalYear_var, [self.fiscalYear_start_var], False))
        self.fiscalYear_start.place(x=285,y=70,width=120,height=20)
        
        self.fiscalYear_end=tk.Checkbutton(root, variable=self.fiscalYear_end_var, font=ft, fg="#000000", 
        justify="center", text="Fiscal Year End", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.fiscalYear_var, [self.fiscalYear_end_var], False))
        self.fiscalYear_end.place(x=285,y=100,width=120,height=20)

        self.enteredDate_var = tk.IntVar()
        self.enteredDate=tk.Checkbutton(root, variable=self.enteredDate_var, font=ft, fg="#000000", 
        justify="center", text="Entered Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(7, self.enteredDate_var, "Entered Date"))
        self.enteredDate.place(x=440,y=40,width=130,height=20)

        self.entry_var = tk.IntVar()
        self.entry=tk.Checkbutton(root, variable=self.entry_var, font=ft, fg="#000000", 
        justify="center", text="Entries", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(8, self.entry_var, "Entries"))
        self.entry.place(x=630,y=40,width=130,height=20)

        self.entry_comment_var = tk.IntVar()
        self.entry_comment=tk.Checkbutton(root, variable=self.entry_comment_var, font=ft, fg="#000000", 
        justify="center", text="Entry Comment", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(9, self.entry_comment_var, "Entry Comment"))
        self.entry_comment.place(x=680,y=70,width=117,height=20)

        self.entry_number_var = tk.IntVar()
        self.entry_number=tk.Checkbutton(root, variable=self.entry_number_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(10, self.entry_number_var, "Entry Number"))
        self.entry_number.place(x=680,y=100,width=110,height=20)

        self.totalCredit_var = tk.IntVar()
        self.totalCredit=tk.Checkbutton(root, variable=self.totalCredit_var, font=ft, fg="#000000", 
        justify="center", text="Total Credit", offvalue="0", onvalue="1",
        command=lambda: self.checkboxPressed(11, self.totalCredit_var, "Total Credit"))
        self.totalCredit.place(x=30,y=170,width=112,height=20)

        self.totalDebit_var = tk.IntVar()
        self.totalDebit=tk.Checkbutton(root, variable=self.totalDebit_var, font=ft, fg="#000000", 
        justify="center", text="Total Debit", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(12, self.totalDebit_var, "Total Debit"))
        self.totalDebit.place(x=30,y=210,width=110,height=20)

        self.entryNumberCounter_var = tk.IntVar()
        self.entryNumberCounter=tk.Checkbutton(root, variable=self.entryNumberCounter_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number Counter", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(13, self.entryNumberCounter_var, "Entry Number Counter"))
        self.entryNumberCounter.place(x=30,y=250,width=170,height=20)

        self.debitCardCode_var = tk.IntVar()
        self.debitCardCode=tk.Checkbutton(root, variable=self.debitCardCode_var, font=ft, fg="#000000", 
        justify="center", text="Debit Card Code", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(14, self.debitCardCode_var, "Debit Card Code"))
        self.debitCardCode.place(x=30,y=290,width=140,height=20)

        self.postingDate_var = tk.IntVar()
        self.postingDate=tk.Checkbutton(root, variable=self.postingDate_var, font=ft, fg="#000000", 
        justify="center", text="Posting Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(15, self.postingDate_var, "Posting Date"))
        self.postingDate.place(x=30,y=330,width=120,height=20)

        self.documentReference_var = tk.IntVar()
        self.documentReference=tk.Checkbutton(root, variable=self.documentReference_var, font=ft, fg="#000000", 
        justify="center", text="Document Reference", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(16, self.documentReference_var, "Document Reference"))
        self.documentReference.place(x=30,y=370,width=160,height=20)

        self.detailComment_var = tk.IntVar()
        self.detailComment=tk.Checkbutton(root, variable=self.detailComment_var, font=ft, fg="#000000", 
        justify="center", text="Detail Comment", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(17, self.detailComment_var, "Detail Comment"))
        self.detailComment.place(x=30,y=410,width=130,height=20)

        self.selectAll_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=16)
        self.selectAll=tk.Checkbutton(root, variable=self.selectAll_var, font=ft, fg="#000000", 
        justify="center", text="Select All", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.selectAll_var, listOfAllChildren, True))
        self.selectAll.place(x=50,y=470,width=130,height=20)

        self.line_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=10)
        self.line=tk.Checkbutton(root, variable=self.line_var, font=ft, fg="#000000", 
        justify="center", text="Line", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(19, self.line_var, "Line"))
        self.line.place(x=240,y=170,width=110,height=20)

        self.line_number_var = tk.IntVar()
        self.line_number=tk.Checkbutton(root, variable=self.line_number_var, font=ft, fg="#000000", 
        justify="center", text="Line Number", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(20, self.line_number_var, "Line Number"))
        self.line_number.place(x=285,y=200,width=110,height=20)

        self.line_counter_var = tk.IntVar()
        self.line_counter=tk.Checkbutton(root, variable=self.line_counter_var, font=ft, fg="#000000", 
        justify="center", text="Line Counter", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(21, self.line_counter_var, "Line Counter"))
        self.line_counter.place(x=285,y=230,width=117,height=20)

        self.account_var = tk.IntVar()
        self.account=tk.Checkbutton(root, variable=self.account_var, font=ft, fg="#000000", 
        justify="center", text="Account", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(22, self.account_var, "Account"))
        self.account.place(x=440,y=170,width=117,height=20)

        self.account_mainID_var = tk.IntVar()
        self.account_mainID=tk.Checkbutton(root, variable=self.account_mainID_var, font=ft, fg="#000000", 
        justify="center", text="Account Main ID", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(23, self.account_mainID_var, "Account Main ID"))
        self.account_mainID.place(x=485,y=200,width=117,height=20)

        self.account_mainDesc_var = tk.IntVar()
        self.account_mainDesc=tk.Checkbutton(root, variable=self.account_mainDesc_var, font=ft, fg="#000000", 
        justify="center", text="Account Main Description", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(24, self.account_mainDesc_var, "Account Main Description"))
        self.account_mainDesc.place(x=485,y=230,width=170,height=20)

        self.account_subID_var = tk.IntVar()
        self.account_subID=tk.Checkbutton(root, variable=self.account_subID_var, font=ft, fg="#000000", 
        justify="center", text="Account Sub ID", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(25, self.account_subID_var, "Account Sub ID"))
        self.account_subID.place(x=485,y=260,width=112,height=20)

        self.account_subDesc_var = tk.IntVar()
        self.account_subDesc=tk.Checkbutton(root, variable=self.account_subDesc_var, font=ft, fg="#000000", 
        justify="center", text="Account Sub Description", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(26, self.account_subDesc_var, "Account Sub Description"))
        self.account_subDesc.place(x=485,y=290,width=162,height=20)

        self.account_amount_var = tk.IntVar()
        self.account_amount=tk.Checkbutton(root, variable=self.account_amount_var, font=ft, fg="#000000", 
        justify="center", text="Amount", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed(27, self.account_amount_var, "Amount"))
        self.account_amount.place(x=485,y=320,width=70,height=20)

        self.text = Text(root, state='disabled', width=40, height=5, wrap=WORD)
        self.text.place(x = 450, y = 390)

        self.file = None # this will store the file that will be imported
        self.fileCounter = 1
        self.fileList = []
        
        selectFile_button = Button(root, text = "Choose File", command=self.selectFile).place(x = 530, y = 480)
        ok_button = Button(root, text = "OK", command=self.okButtonCommand).place(x = 670, y = 480)

    def parentPressed(self, parentVar, children, isParent):
        if ((parentVar.get() == 1) and (isParent == True)):
            for child in children:
                child.set(1)
        for child in children:
            if child.get() == 0:
                parentVar.set(0)
                self.selectAll_var.set(0)

    def fiscalYearPressed(self, columnNum, varName, textDesc):
        if (columnNum == 4 and varName.get() == 1 ): 
            # columnNum indicates which field, varName.get() indicates whether it is on or off
            self.coveredDate_start_var.set(1)
            self.coveredDate_end_var.set(1)
                
        if ((columnNum == 5 and varName.get() == 0) or (columnNum == 6 and varName.get() == 0)):
            # If one of the children is unchecked, we uncheck the parent
            self.coveredDate_var.set(0)
        
    def checkboxPressed(self, columnNum, varName, textDesc):
        if (columnNum == 1 and varName.get() == 1 ): 
            # columnNum indicates which field, varName.get() indicates whether it is on or off
            self.coveredDate_start_var.set(1)
            self.coveredDate_end_var.set(1)
            self.coveredDate_start.configure(state='disabled')

    def selectFile(self):
        filetypes = (
            ('XML files', '*.xml'),
        )
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='D:\Bilkent Uni\MED_IDEA Internship\e-defter Module\Code\Sample Data',
            filetypes=filetypes
        )
        self.file = filename
        self.fileList.append(filename)
        self.text.configure(state='normal')
        if filename != "":
            self.text.insert('end', str(self.fileCounter) + "- " + PurePosixPath(filename).name + "\n")
            self.fileCounter += 1
        self.text.configure(state='disabled')

    def okButtonCommand(self):
        for filePath in self.fileList:
            tree = ET.parse(filePath)
            root = tree.getroot()
            for child in root[0][1][0]:
                print(child.tag, child.attrib)
                print()
            # print(root[0][1][0])
            # print()
            # print(i)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

import tkinter as tk
import tkinter.font as tkFont
import xml.etree.ElementTree as ET
import pandas as pd
import win32com.client as win32ComClient
import os
from tkinter import *
from pathlib import PurePosixPath, Path
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

        # ====================================
        # =========== START OF UI ============
        # P.S You should not need to change
        # These parts, so you can skip them
        # =========== START OF UI =============
        # =====================================

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
        listOfAllChildren_var = []

        coveredDateChildren = [self.coveredDate_start_var, self.coveredDate_end_var]
        self.coveredDate=tk.Checkbutton(root, variable=self.coveredDate_var, font=ft, fg="#000000", 
        justify="center", text="Covered Date", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.coveredDate_var, coveredDateChildren, True))
        self.coveredDate.place(x=30,y=40,width=130,height=15)

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
        command=lambda: self.checkboxPressed(self.enteredDate_var))
        self.enteredDate.place(x=440,y=40,width=130,height=20)

        self.entry_var = tk.IntVar()
        self.entry_comment_var = tk.IntVar()
        self.entry_number_var = tk.IntVar()
        entryChildren = [self.entry_comment_var, self.entry_number_var]
        self.entry=tk.Checkbutton(root, variable=self.entry_var, font=ft, fg="#000000", 
        justify="center", text="Entries", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.entry_var, entryChildren, True))
        self.entry.place(x=630,y=40,width=130,height=20)
        
        self.entry_comment=tk.Checkbutton(root, variable=self.entry_comment_var, font=ft, fg="#000000", 
        justify="center", text="Entry Comment", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.entry_var, [self.entry_comment_var], False))
        self.entry_comment.place(x=680,y=70,width=117,height=20)

        self.entry_number=tk.Checkbutton(root, variable=self.entry_number_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.entry_var, [self.entry_number_var], False))
        self.entry_number.place(x=680,y=100,width=110,height=20)

        self.totalCredit_var = tk.IntVar()
        self.totalCredit=tk.Checkbutton(root, variable=self.totalCredit_var, font=ft, fg="#000000", 
        justify="center", text="Total Credit", offvalue="0", onvalue="1",
        command=lambda: self.checkboxPressed( self.totalCredit_var))
        self.totalCredit.place(x=30,y=170,width=112,height=20)

        self.totalDebit_var = tk.IntVar()
        self.totalDebit=tk.Checkbutton(root, variable=self.totalDebit_var, font=ft, fg="#000000", 
        justify="center", text="Total Debit", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.totalDebit_var))
        self.totalDebit.place(x=30,y=210,width=110,height=20)

        self.entryNumberCounter_var = tk.IntVar()
        self.entryNumberCounter=tk.Checkbutton(root, variable=self.entryNumberCounter_var, font=ft, fg="#000000", 
        justify="center", text="Entry Number Counter", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.entryNumberCounter_var))
        self.entryNumberCounter.place(x=30,y=250,width=170,height=20)

        self.debitCardCode_var = tk.IntVar()
        self.debitCardCode=tk.Checkbutton(root, variable=self.debitCardCode_var, font=ft, fg="#000000", 
        justify="center", text="Debit Card Code", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.debitCardCode_var))
        self.debitCardCode.place(x=30,y=290,width=140,height=20)        

        self.postingDate_var = tk.IntVar()
        self.postingDate=tk.Checkbutton(root, variable=self.postingDate_var, font=ft, fg="#000000", 
        justify="center", text="Posting Date", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.postingDate_var))
        self.postingDate.place(x=30,y=330,width=120,height=20)

        self.documentReference_var = tk.IntVar()
        self.documentReference=tk.Checkbutton(root, variable=self.documentReference_var, font=ft, fg="#000000", 
        justify="center", text="Document Reference", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.documentReference_var))
        self.documentReference.place(x=30,y=370,width=160,height=20)

        self.detailComment_var = tk.IntVar()
        self.detailComment=tk.Checkbutton(root, variable=self.detailComment_var, font=ft, fg="#000000", 
        justify="center", text="Detail Comment", offvalue="0", onvalue="1", 
        command=lambda: self.checkboxPressed( self.detailComment_var))
        self.detailComment.place(x=30,y=410,width=130,height=20)

        self.line_var = tk.IntVar()
        self.line_number_var = tk.IntVar()
        self.line_counter_var = tk.IntVar()
        lineChidlren = [self.line_number_var, self.line_counter_var]
        ft = tkFont.Font(family='Times',size=10)
        self.line=tk.Checkbutton(root, variable=self.line_var, font=ft, fg="#000000", 
        justify="center", text="Line", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.line_var, lineChidlren, True))
        self.line.place(x=240,y=170,width=110,height=20)
        
        self.line_number=tk.Checkbutton(root, variable=self.line_number_var, font=ft, fg="#000000", 
        justify="center", text="Line Number", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.line_var, [self.line_number_var], False))
        self.line_number.place(x=285,y=200,width=110,height=20)

        self.line_counter=tk.Checkbutton(root, variable=self.line_counter_var, font=ft, fg="#000000", 
        justify="center", text="Line Counter", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.line_var, [self.line_counter_var], False))
        self.line_counter.place(x=285,y=230,width=117,height=20)

        self.account_var = tk.IntVar()
        self.account_mainID_var = tk.IntVar()
        self.account_mainDesc_var = tk.IntVar()
        self.account_subID_var = tk.IntVar()
        self.account_subDesc_var = tk.IntVar()
        self.account_amount_var = tk.IntVar()
        accountChildren = [self.account_mainID_var, self.account_mainDesc_var, self.account_subID_var, self.account_subDesc_var, self.account_amount_var]
        self.account=tk.Checkbutton(root, variable=self.account_var, font=ft, fg="#000000", 
        justify="center", text="Account", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, accountChildren, True))
        self.account.place(x=440,y=170,width=117,height=20)
        
        self.account_mainID=tk.Checkbutton(root, variable=self.account_mainID_var, font=ft, fg="#000000", 
        justify="center", text="Account Main ID", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, [self.account_mainID_var], False))
        self.account_mainID.place(x=485,y=200,width=117,height=20)
        
        self.account_mainDesc=tk.Checkbutton(root, variable=self.account_mainDesc_var, font=ft, fg="#000000", 
        justify="center", text="Account Main Description", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, [self.account_mainDesc_var], False))
        self.account_mainDesc.place(x=485,y=230,width=170,height=20)
        
        self.account_subID=tk.Checkbutton(root, variable=self.account_subID_var, font=ft, fg="#000000", 
        justify="center", text="Account Sub ID", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, [self.account_subID_var], False))
        self.account_subID.place(x=485,y=260,width=112,height=20)
        
        self.account_subDesc=tk.Checkbutton(root, variable=self.account_subDesc_var, font=ft, fg="#000000", 
        justify="center", text="Account Sub Description", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, [self.account_subDesc_var], False))
        self.account_subDesc.place(x=485,y=290,width=162,height=20)

        self.account_amount=tk.Checkbutton(root, variable=self.account_amount_var, font=ft, fg="#000000", 
        justify="center", text="Amount", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.account_var, [self.account_amount_var], False))
        self.account_amount.place(x=485,y=320,width=70,height=20)

        self.text = Text(root, state='disabled', width=40, height=5, wrap=WORD)
        self.text.place(x = 450, y = 390)

        self.selectAll_var = tk.IntVar()
        ft = tkFont.Font(family='Times',size=16)
        self.selectAll=tk.Checkbutton(root, variable=self.selectAll_var, font=ft, fg="#000000", 
        justify="center", text="Select All", offvalue="0", onvalue="1", 
        command=lambda: self.parentPressed(self.selectAll_var, listOfAllChildren_var, True))
        self.selectAll.place(x=50,y=470,width=130,height=20)

        selectFile_button = Button(root, text = "Choose File", command=self.selectFile).place(x = 530, y = 480)
        ok_button = Button(root, text = "OK", command=lambda: self.okButtonCommand(listOfAllChildren)).place(x = 670, y = 480)

        listOfAllChildren.append((self.coveredDate_start_var, 1, 'periodCoveredStart')) # The 1 here is column number in the cleaned version of the XML)
        listOfAllChildren.append((self.coveredDate_end_var, 2, 'periodCoveredEnd'))
        listOfAllChildren.append((self.fiscalYear_start_var, 3, 'fiscalYearStart'))
        listOfAllChildren.append((self.fiscalYear_end_var, 4, 'fiscalYearEnd'))
        listOfAllChildren.append((self.enteredDate_var, 5, 'enteredDate'))
        listOfAllChildren.append((self.entry_number_var, 6, 'entryNumber'))
        listOfAllChildren.append((self.entry_comment_var, 7, 'entryComment'))
        listOfAllChildren.append((self.totalDebit_var, 8, 'totalDebit'))
        listOfAllChildren.append((self.totalCredit_var, 9, 'totalCredit'))
        listOfAllChildren.append((self.entryNumberCounter_var, 10, 'entryNumberCounter'))
        listOfAllChildren.append((self.line_number_var, 11, 'lineNumber'))
        listOfAllChildren.append((self.line_counter_var, 12, 'lineNumberCounter'))
        listOfAllChildren.append((self.account_mainID_var, 13, 'accountMainID'))
        listOfAllChildren.append((self.account_mainDesc_var, 14, 'accountMainDescription'))
        listOfAllChildren.append((self.account_subDesc_var, 15, 'accountSubDescription'))
        listOfAllChildren.append((self.account_subID_var, 16, 'accountSubID'))
        listOfAllChildren.append((self.account_amount_var, 17, 'amount'))
        listOfAllChildren.append((self.debitCardCode_var, 18, 'debitCreditCode'))
        listOfAllChildren.append((self.postingDate_var, 19, 'postingDate'))
        listOfAllChildren.append((self.documentReference_var, 20, 'documentReference'))
        listOfAllChildren.append((self.detailComment_var, 21, 'detailComment'))

        # ====================================
        # =========== END OF UI ============
        # P.S Check the comments below to 
        # see what variables you are available
        # =========== END OF UI =============
        # =====================================

        ''' 
            There is the list called listOfAllChildren, it contains 21 tuples
            representing the 21 columns, each of the tuple has the format of
            (checkBox varibale, column number, name of column )
            checkBox variable: it is used to read/write the value of the check box
            column number: the index of the column after the XML is cleaned (may need to revised, check above)
            name of the column: The EXACT name of the field as it appears in the .XML file
        '''

        ''' 
            The other variable is listOfAllChildren_var, it contains only the 
            check box variables used to access the checkboxes, this is only
            used for the selectAll button above
        '''

        listOfAllChildren_var = [(child[0]) for child in listOfAllChildren]
        
        self.file = None # this will store the file that will be imported
        self.fileCounter = 1
        self.fileList = []

    def parentPressed(self, parentVar, children, isParent):
        if ((parentVar.get() == 1) and (isParent == True)):
            for child in children:
                child.set(1)
        for child in children:
            if child.get() == 0:
                parentVar.set(0)
                self.selectAll_var.set(0)
        
    def checkboxPressed(self, varName):
        if varName.get() == 0:
            self.selectAll_var.set(0)

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

    def okButtonCommand(self, childrenList):
        listOfChosenColumns = [child[2] for child in childrenList if child[0].get() == 1]
        # self.fileList = ['D:/Bilkent Uni/MED_IDEA Internship/e-defter Module/Code/Sample Data/6080044835-202101-Y-000000.xml']
        for filePath in self.fileList:
            filteredData = self.xmlToDataFrame(filePath, listOfChosenColumns)

            # conversion of the DataFrame to a cleaned/filtered XML
            fileName = Path(filePath).stem
            fileName_clean = fileName + 'clean.xml'
            filteredData.to_xml(fileName_clean, index = False)
            filePath_clean = os.getcwd() + '\\' + fileName_clean
            # print (filePath_clean, '---', fileName)
            self.importXMLToIdea(filePath = filePath_clean, fileName = fileName)

    def xmlToDataFrame (self, filePath, listOfChosenColumns):
        tree = ET.parse(filePath)
        root = tree.getroot()
        limit = 3
        counter = 0
        filteredData = pd.DataFrame()
        isThereNone = True
        dataRow = {column : None for column in listOfChosenColumns}

        for child in root.iter():
            if limit == counter:
                break
            filteredChildtag = child.tag.split('}', 1)[1]
            # entryDetail indicates the beginning of a new record
            # isThereNone makes sure that no values in the dictionary are None
            # i.e. ensures all the fields are populated
            if (filteredChildtag == "entryDetail") and not isThereNone:
                # we have the data row here, we need to append it to a DataFrame
                filteredData = filteredData.append(dataRow, ignore_index=True)
                counter += 1
            if filteredChildtag in listOfChosenColumns:
                dataRow[filteredChildtag] = child.text
                isThereNone = not all(dataRow.values()) # returns false if not elements are None, returns true if there is 1 or more None values
        
        return filteredData
    
    # filePath is the path to the XML file that holds the cleaned/filtered data
    # fileName is the name you want to be given to the new .IMD DB
    def importXMLToIdea (self, filePath = None, fileName = None):
        try:
            print('step1')
            idea = win32ComClient.Dispatch(dispatch="Idea.IdeaClient")
            print('step2')
            task = idea.GetImportTask ("ImportXML")
            print('step3')
            task.InputFileName = filePath
            print('step4')
            task.OutputFileName = fileName
            print('step5')
            projectFolder = idea.WorkingDirectory
            self.deleteIfExists(projectFolder + '\\' + fileName + '.IMD')
            task.PerformTask()
            print('step6')

            # deleted the temp cleaned XML file
            os.remove(filePath)
            print('step7')
        finally:
            task = None
            db = None
            idea = None

    def deleteIfExists (self, path = None):
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

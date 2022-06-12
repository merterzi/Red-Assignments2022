Begin Dialog NewDialog 50,50,150,150,"NewDialog", .NewDialog
End Dialog
Dim FilePath As String 'variable to hold the filename

Sub Main
	
Call createDatabase ()
Call insertData()

End Sub

Function createDatabase()
	' Create a table.
	Dim NewTable As Table
	Set NewTable = Client.NewTableDef
	
	' Define a field for the table.
	Dim AddedField As Field
	Set AddedField = NewTable.NewField
	AddedField.Name = "ACIKLAMALAR"
	AddedField.Type = WI_CHAR_FIELD
	AddedField.Length = 200
	
	' Add the field to the table.
	NewTable.AppendField AddedField
	
	' Perform the same steps for a second field.
	Set AddedField = NewTable.NewField
	AddedField.Name = "CARI_DONEM"
	AddedField.Type = WI_NUM_FIELD
	AddedField.Decimals = 0
	NewTable.AppendField AddedField
	
	Set AddedField = NewTable.NewField
	AddedField.Name = "ONCEKI_DONEM"
	AddedField.Type = WI_NUM_FIELD
	AddedField.Decimals = 0
	NewTable.AppendField AddedField
	
	' Change the table settings to allow writing.
	NewTable.Protect = False
	
	' Create the database.
	Dim db As Database
	Dim Path As String

	Set db = Client.NewDatabase("Ahmet_Salman_test.IMD", "", NewTable)
	
	' Commit the database.
	db.CommitDatabase
	
	Set db = Nothing
	Set AddedField = Nothing
	Set NewTable = Nothing
End Function

Function insertData()
	Dim Path As String
	Path = "D:\Bilkent Uni\MED_IDEA Internship\Red-Assignments2022\Assignment1\"
	Dim dbName As String
	'dbName = Client.LocateInputFile (Path + "4- BOBI FRS Nakit Akis Tablosu - Dolayli Yöntem (Konsolide).xlsx")
	dbName = Client.LocateInputFile (Path + "test2.xlsx")
	Dim task As ImportExcel
	Set task = Client.GetImportTask("ImportExcel")
	task.FileToImport = dbName
	'task.SheetToImport = "BOBI FRS NAT Dolayli Konsolide"
	task.SheetToImport = "Sheet1"
	task.OutputFilePrefix = "Excel"
	task.FirstRowIsFieldName = "False"
	task.EmptyNumericFieldAsZero = "False"
	task.PerformTask
	Path = "D:\MED_IDEA_Internsip\Managed_Projects\TestingCreation\"
	'DeleteOld Path + "Excel-Sheet1.imd"
	
	Set task = Nothing
	
	Dim db1 As Database
	'Set db1 = OpenDB(Path + "Excel-BOBI FRS NAT Dolayli Konsolide.IMD")
	Set db1 = OpenDB(Path + "Excel-Sheet1.IMD")
	' Access the RecordSet.
	Dim RS1 As RecordSet
	Set RS1 = db1.RecordSet
	' Move to the first record.
	RS1.ToFirst
	RS1.Next
	RS1.Next
	RS1.Next
	RS1.Next
	
	Dim currentText As String
	Dim col2Val As String
	Dim col3Val As String
	Dim col4Val As String
	
	Dim NewTable As Table
	Set NewTable = Client.NewTableDef
	
	' Create the database.
	Dim db As Database
	Set db = Client.OpenDatabase("Ahmet_Salman_test.IMD")
	
	' Obtain the recordset.
	Dim rs As RecordSet
	Set rs = db.RecordSet
	
	' Obtain a new record.
	Dim rec As Record
	Set rec = rs.NewRecord
	
	For Count = 1 To 68
		col3Val = RS1.ActiveRecord.GetCharValue("COL3")
		col4Val = RS1.ActiveRecord.GetCharValue("COL4")
		col5Val = RS1.ActiveRecord.GetCharValue("COL5")
		If col3Val <> "" Then
			rec.SetCharValue"ACIKLAMALAR", col3Val
		ElseIf col4Val <> "" Then
			rec.SetCharValue"ACIKLAMALAR", col4Val
		ElseIf col5Val <> "" Then
			rec.SetCharValue"ACIKLAMALAR", col5Val
		End If
		'currentText = RS1.ActiveRecord.GetCharValue("COL3")
		'If currentText = "" Then
		'	currentText = RS1.ActiveRecord.GetCharValue("COL4")
		'End If
		
		'If currentText = "" Then
		'	RS1.ActiveRecord.GetCharValue("COL5")
		'End If
		'MsgBox "col2 " + col2Val + "  col3 " + col3Val + "  col4 " + col4Val
		' Use the field name method to add data.
		'rec.SetCharValue"ACIKLAMALAR", currentText
		rec.SetCharValue "CARI_DONEM", 0
		rec.SetCharValue "ONCEKI_DONEM", 0
		rs.AppendRecord rec
		RS1.Next
	Next
	
	col3Val = RS1.ActiveRecord.GetCharValue("COL3")
	col4Val = RS1.ActiveRecord.GetCharValue("COL4")
	col5Val = RS1.ActiveRecord.GetCharValue("COL5")
	If col3Val <> "" Then
		rec.SetCharValue"ACIKLAMALAR", col3Val
	ElseIf col4Val <> "" Then
		rec.SetCharValue"ACIKLAMALAR", col4Val
	ElseIf col5Val <> "" Then
		rec.SetCharValue"ACIKLAMALAR", col5Val
	End If
	rec.SetCharValue "CARI_DONEM", 0
	rec.SetCharValue "ONCEKI_DONEM", 0
	rs.AppendRecord rec
	
	
	db.CommitDatabase
	db.close
	Client.OpenDatabase "Ahmet_Salman_test.IMD"
	
	Set db = Nothing
	Set AddedField = Nothing
	Set NewTable = Nothing

End Function

Function OpenDB(DBPath As String) As Database
	' Verify that the database exists.
	Dim PathCheck As String
	PathCheck = Dir( DBPath )
	' Define a database object.
	Dim db As Database
	' Open the database using the default client folder.
	Set db = Client.OpenDatabase(DBPath)
	' Return the database object.
	OpenDB = db
	' Clear the memory used by db.
	Set db = Nothing
End Function

Sub DeleteOld(Filepath As String)
	' Determine if the file exists.
	Dim PathCheck As String
	PathCheck = Dir( Filepath )
'	' Delete the file if it exists.
	If Len(PathCheck) > 1 Then
	MsgBox "Deleting old copy of " + PathCheck
	Kill Filepath
	End If
End Sub


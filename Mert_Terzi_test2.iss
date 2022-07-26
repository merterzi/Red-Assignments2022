
Option Explicit


Dim db As Object
Dim table As Object
Dim field As Object
Dim task As Task



Sub Main
	Call CreateTable()
	Call AddData()
	Call DeleteDatabase()
End Sub


Function CreateTable()

	Set table = Client.NewTableDef
	
	Set field = table.NewField
	field.Name = "ACIKLAMALAR"
	field.Type= WI_EDIT_CHAR 
	field.Length= 150
	table.AppendField field
	
	Set field = table.NewField
	field.Name = "CARI_DONEM"
	field.Type = WI_EDIT_NUM 
	field.Decimals = 2
	table.AppendField field
	
	Set field = table.NewField
	field.Name = "ONCEKI_DONEM"
	field.Type = WI_EDIT_NUM 
	field.Decimals = 2
	table.AppendField field
	
	
	table.Protect = False     
	
	Set db = Client.NewDatabase("Mert_Terzi_test.IMD", "", table )  
	
	table.Protect = True
	
	
	Set db = Nothing
	Set field = Nothing
	Set table = Nothing

End Function


Function AddData()

	Dim dbName As String
	
	Set task = Client.GetImportTask("ImportExcel")
	dbName = "C:\Users\Mert Terzi\Desktop\4- BOBÝ FRS Nakit Akýþ Tablosu - Dolaylý Yöntem (Konsolide).xlsx"
	task.FileToImport = dbName
	task.SheetToImport = "BOBÝ FRS NAT Dolaylý Konsolide"
	task.OutputFilePrefix = "4- BOBÝ FRS Nakit Akýþ Tablosu - Dolaylý Yöntem (Konsolide)"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	dbName = task.OutputFilePath("BOBÝ FRS NAT Dolaylý Konsolide")
	Set task = Nothing
	

	Dim db2 As Database
	Dim rs As RecordSet
	
	Set db2 = Client.OpenDatabase(dbName)
	
	Set rs = db2.RecordSet
	
	rs.ToFirst
	rs.Next
	rs.Next
	rs.Next
	
	Dim col1 As String
	Dim col2 As String
	Dim col3 As String
	
	Dim db3 As Database
	Set db3 = Client.OpenDatabase("Mert_Terzi_test.IMD")
	
	Dim rs2 As RecordSet
	Set rs2 = db3.RecordSet
	
	Dim rec As Record
	Set rec = rs2.NewRecord
	
	Dim count As Integer
	
	For count = 1 To 68
		col1 = rs.ActiveRecord.GetCharValue("COL3")
		col2 = rs.ActiveRecord.GetCharValue("BOBI_FRS_NAKIT_AKýÞ_TABLOSU_DOLAYLý_YÖNT")
		col3 = rs.ActiveRecord.GetCharValue("COL5")
		
		If col1 <> "" Then 
			rec.SetCharValue "ACIKLAMALAR", col1
		ElseIf col2 <> "" Then
			rec.SetCharValue "ACIKLAMALAR", col2
		ElseIf col3 <> "" Then
			rec.SetCharValue "ACIKLAMALAR", col3
		End If
		
		rec.SetNumValue "CARI_DONEM", 0
		rec.SetNumValue "ONCEKI_DONEM", 0
		
		rs2.AppendRecord rec
		rs.Next
	Next count
	
	col1 = rs.ActiveRecord.GetCharValue("COL3")
	col2 = rs.ActiveRecord.GetCharValue("BOBI_FRS_NAKIT_AKýÞ_TABLOSU_DOLAYLý_YÖNT")
	col3 = rs.ActiveRecord.GetCharValue("COL5")
	
	If col1 <> "" Then 
		rec.SetCharValue "ACIKLAMALAR", col1
	ElseIf col2 <> "" Then
		rec.SetCharValue "ACIKLAMALAR", col2
	ElseIf col3 <> "" Then
		rec.SetCharValue "ACIKLAMALAR", col3
	End If
		
	rec.SetNumValue "CARI_DONEM", 0
	rec.SetNumValue "ONCEKI_DONEM", 0
	
	rs2.AppendRecord rec
	
	
	db3.CommitDatabase
	db3.close
	Client.OpenDatabase "Mert_Terzi_test.IMD"
	
	Set db2 = Nothing
	Set db3 = Nothing
	Set rs = Nothing
	Set rs2 = Nothing
	Set rec = Nothing
	
End Function

Function DeleteDatabase()
	Client.DeleteDatabase "4- BOBÝ FRS Nakit Akýþ Tablosu - Dolaylý Yöntem (Konsolide)-BOBÝ FRS NAT Dolaylý Konsolide.IMD"
End Function





























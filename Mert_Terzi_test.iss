
Option Explicit

Dim db As Object
Dim field As Object
Dim table As Object

Dim rs As Object
Dim rec As Object

Dim i As Integer
Const arraySize = 68
Dim descriptions(arraySize) As String



Sub Main
	Call CreateTable()
End Sub


Function CreateTable()
	
	descriptions(0) = "Esas Faaliyetlerden Nakit Ak��lar�"
	descriptions(1) = "D�nem Kar� (Zarar�) (+/-)"
	descriptions(2) = "D�nem Kar� (Zarar�) Mutabakat� �le �lgili D�zeltmeler"
	descriptions(3) = "Amortisman ve �tfa Gideriyle ilgili D�zeltmeler"
	descriptions(4) = "De�er D���kl��� (�ptali) ile ilgili D�zeltmeler (+/-)"
	descriptions(5) = "Kar��l�klarla ilgili D�zeltmeler (+/-)"
	descriptions(6) = "Faiz Gelirleri ve Giderleriyle ilgili D�zeltmeler (+/-)"
	descriptions(7) = "Ger�ekle�memi� Kur Farklar�yla �lgili D�zeltmeler (+/-)"
	descriptions(8) = "Ger�e�e Uygun De�er Kay�plar� (Kazan�lar�)ile ilgili D�zeltmeler (+/-)"
	descriptions(9) = "Stoklardaki Azal��lar (Art��lar) ile ilgili �zeltmeler (+/-)"
	descriptions(10) = "Ticari Alacaklardaki Azal��lar (Art��lar) lle ilgili D�zeltmeler (+/-)"
	descriptions(11) = "Faaliyetler ile ilgili Diger Alacaklardaki Azal��lar (Art��lar) ile ilgili D�zeltmeler (+/-)"
	descriptions(12) = "Ticari Bor�lardaki Art��lar (Azal��lar) Ile ilgili D�zeltmeler (+/-)"
	descriptions(13) = "Faaliyetler ile ilgili Di�er Bor�lardaki Art��lar (Azal��lar) ile ilgili D�zeltmeler (+/-)"
	descriptions(14) = "Ertelenmi� Gelirlerdeki Art��lar (Azal��lar) ile ilgili D�zeltmeler (+/-)"
	descriptions(15) = "Nakit D��� Kalemlere ili�kin Di�er D�zeltmeler (+/-)"
	descriptions(16) = " Duran Varl�klar�n Elden ��kar�lmas�ndan Kay�plar (Kazan�lar) ile ilgili D�zeltmeler (+/-)"
	descriptions(17) = "Yat�r�m ya da Finansman Faaliyetlerinden Nakit Ak��lar�na Neden Olan Diger Kalemlere ili�kin D�zeltmeler (+/-)"
	descriptions(18) = "D�nem Kar� (Zarar�) Mutabakat� ile ilgili Di�er D�zeltmeler (+/-)"
	descriptions(19) = "D�nem Kar� (Zarar�) Mutabakat� ile ilgili Toplma D�zeltmeler (+/-)"
	descriptions(20) = "Faaliyetlerden Kaynaklanan Net Nakit Ak��� (+/-)"
	descriptions(21) = "�denen Kar Paylar� (-)"
	descriptions(22) = "Al�nan Kar Paylar�"
	descriptions(23) = "�denen Faiz (-)"
	descriptions(24) = "Al�nan Faiz"
	descriptions(25) = "Vergi �adeleri (�demeleri) (+/-)"
	descriptions(26) = "Di�er Nakit Giri�leri (��k��lar�) (+/-)"
	descriptions(27) = "Esas Faaliyetlerden Net Nakit Ak��� (+/-)"
	descriptions(28) = "Yat�r�m Faaliyetlerinden Nakit Ak��lar�"
	descriptions(29) = "Ba�l� Ortakl�klardaki Paylar�n Kontrol Kayb�na Neden Olacak �ekilde Elden ��kar�lmas�ndan Nakit Giri�leri"
	descriptions(30) = "Ba�l� Ortakl�k Ediniminden Nakit ��k��lar� (-)"
	descriptions(31) = "��tirak ve M��terek Giri�imlerdeki Paylar�n Elden ��kar�lmas�ndan Nakit Giri�leri"
	descriptions(32) = "��tirak ve M��terek Giri�im Paylar�n�n Ediniminden Nakit ��k��lar� (-)"
	descriptions(33) = "Ba�ka ��letme veya Fon Paylar�n�n veya Bor�lanma Ara�lar�n�n Elden ��kar�lmas�ndan Nakit Giri�leri"
	descriptions(34) = "Ba�ka ��letme veya Fon Paylar�n�n veya Bor�lanma Ara�lar�n�n Ediniminden Nakit ��k��lar� (-)"
	descriptions(35) = "Maddi ve Maddi Olmayan Duran Varl�klar�n Sat���ndan Nakit Giri�leri"
	descriptions(36) = "Maddi ve Maddi Olmayan Duran Varl�k Al�m�ndan Nakit ��k��lar� (-)"
	descriptions(37) = "Di�er Uzun Vadeli Varl�klar�n Sa���ndan Nakit Giri�leri "
	descriptions(38) = "Di�er Uzun Vadeli Varl�k Al�mlar�ndan Nakit ��k��lar� (-)"
	descriptions(39) = "Verilen Nakit Avans ve Bor�lar (-)"
	descriptions(40) = "Verilen Nakit Avans ve Bor�lardan Geri �demeler"
	descriptions(41) = "T�rev Ara�lardan Nakit Giri�leri"
	descriptions(42) = "T�rev Ara�lardan Nakit ��k��lar� (-)"
	descriptions(43) = "Devlet Te�viklerinden Nakit Giri�leri"
	descriptions(44) = "Al�nan Kar Paylar�"
	descriptions(45) = "�denen Faiz (-)"
	descriptions(46) = "Al�nan Faiz"
	descriptions(47) = "Vergi �adeleri (�demeleri) (+/-)"
	descriptions(48) = "Di�er Nakit Giri�leri (��k��lar�) (+/-)"
	descriptions(49) = "Yat�r�m Faaliyetlerinden Net Nakit Ak��� (+/-)"
	descriptions(50) = "Finans Faaliyetlerinden Nakit Ak��lar�"
	descriptions(51) = "Ba�l� Ortakl�klardaki Paylar�n Kontrol Kayb�na Neden Olmayacak �ekilde Elden ��kar�lmas�ndan Nakit Giri�leri"
	descriptions(52) = "Ba�l� Ortakl�klar�n �lave Paylar�n�n Ediniminden Nakit ��k��lar� (-)"
	descriptions(53) = "�zkaynak Ara�lar�n�n �hrac�ndan veya Sermaye Art�r�m�ndan Nakit Giri�leri"
	descriptions(54) = "��letmenin Kendi Paylar�n� ve Di�er �zkaynak Ara�lar�n� Almas�yla veya Sermayenin Azalt�lmas�yla �lgili Nakit ��k��lar� (-)"
	descriptions(55) = "Bor�lanmadan Kaynaklanan Nakit Giri�leri"
	descriptions(56) = "Bor� �demelerinden Nakit ��k��lar� (-)"
	descriptions(57) = "Finansal Kiralama Bor�lar�ndan Nakit ��k��lar� (-)"
	descriptions(58) = "Devlet Te�viklerinden Nakit Giri�leri"
	descriptions(59) = "�denen Kar Paylar� (-)"
	descriptions(60) = "�denen Faiz (-)"
	descriptions(61) = "Vergi �adeleri (�demeleri) (+/-)"
	descriptions(62) = "Di�er Nakit Giri�leri (��k��lar�) (+/-)"
	descriptions(63) = "Finansman Faaliyetlerinden Net Nakit Ak��� (+/-)"
	descriptions(64) = "Kur Farklar�n�n Etkisinden �nce Nakit ve Nakit Benzerlerindeki Safi Art�� (Azal��) (+/-)"
	descriptions(65) = "Kur Farklar�n�n Nakit ve Nakit Benzerleri �zerindeki Etkisi (+/-)"
	descriptions(66) = "Nakit ve Nakit Benzerlerindeki Safi Art�� (Azal��) (+/-)"
	descriptions(67) = "D�nem Ba�� Nakit ve Nakit Benzerleri"
	descriptions(68) = "D�nem Sonu Nakit ve Nakit Benzerleri"
	
	
	
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
	Set rs = db.RecordSet
	Set rec = rs.NewRecord
	
	For i=LBound(descriptions) To UBound(descriptions)
		rec.SetCharValue "ACIKLAMALAR", descriptions(i)
		rec.SetNumValue "CARI_DONEM", 0
		rec.SetNumValue "ONCEKI_DONEM", 0
		rs.AppendRecord rec
	Next
		
	Set table = db.TableDef
	table.Protect = True
		
		
	db.CommitDatabase
	db.close
	Client.OpenDatabase "Mert_Terzi_test.IMD"
		
	Set rec = Nothing
	Set rs = Nothing
	Set db = Nothing
	Set field = Nothing
	Set table = Nothing
	
End Function










































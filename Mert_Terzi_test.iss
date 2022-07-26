
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
	
	descriptions(0) = "Esas Faaliyetlerden Nakit Akýþlarý"
	descriptions(1) = "Dönem Karý (Zararý) (+/-)"
	descriptions(2) = "Dönem Karý (Zararý) Mutabakatý Ýle Ýlgili Düzeltmeler"
	descriptions(3) = "Amortisman ve Ýtfa Gideriyle ilgili Düzeltmeler"
	descriptions(4) = "Deðer Düþüklüðü (Ýptali) ile ilgili Düzeltmeler (+/-)"
	descriptions(5) = "Karþýlýklarla ilgili Düzeltmeler (+/-)"
	descriptions(6) = "Faiz Gelirleri ve Giderleriyle ilgili Düzeltmeler (+/-)"
	descriptions(7) = "Gerçekleþmemiþ Kur Farklarýyla Ýlgili Düzeltmeler (+/-)"
	descriptions(8) = "Gerçeðe Uygun Deðer Kayýplarý (Kazançlarý)ile ilgili Düzeltmeler (+/-)"
	descriptions(9) = "Stoklardaki Azalýþlar (Artýþlar) ile ilgili üzeltmeler (+/-)"
	descriptions(10) = "Ticari Alacaklardaki Azalýþlar (Artýþlar) lle ilgili Düzeltmeler (+/-)"
	descriptions(11) = "Faaliyetler ile ilgili Diger Alacaklardaki Azalýþlar (Artýþlar) ile ilgili Düzeltmeler (+/-)"
	descriptions(12) = "Ticari Borçlardaki Artýþlar (Azalýþlar) Ile ilgili Düzeltmeler (+/-)"
	descriptions(13) = "Faaliyetler ile ilgili Diðer Borçlardaki Artýþlar (Azalýþlar) ile ilgili Düzeltmeler (+/-)"
	descriptions(14) = "Ertelenmiþ Gelirlerdeki Artýþlar (Azalýþlar) ile ilgili Düzeltmeler (+/-)"
	descriptions(15) = "Nakit Dýþý Kalemlere iliþkin Diðer Düzeltmeler (+/-)"
	descriptions(16) = " Duran Varlýklarýn Elden Çýkarýlmasýndan Kayýplar (Kazançlar) ile ilgili Düzeltmeler (+/-)"
	descriptions(17) = "Yatýrým ya da Finansman Faaliyetlerinden Nakit Akýþlarýna Neden Olan Diger Kalemlere iliþkin Düzeltmeler (+/-)"
	descriptions(18) = "Dönem Karý (Zararý) Mutabakatý ile ilgili Diðer Düzeltmeler (+/-)"
	descriptions(19) = "Dönem Karý (Zararý) Mutabakatý ile ilgili Toplma Düzeltmeler (+/-)"
	descriptions(20) = "Faaliyetlerden Kaynaklanan Net Nakit Akýþý (+/-)"
	descriptions(21) = "Ödenen Kar Paylarý (-)"
	descriptions(22) = "Alýnan Kar Paylarý"
	descriptions(23) = "Ödenen Faiz (-)"
	descriptions(24) = "Alýnan Faiz"
	descriptions(25) = "Vergi Ýadeleri (Ödemeleri) (+/-)"
	descriptions(26) = "Diðer Nakit Giriþleri (Çýkýþlarý) (+/-)"
	descriptions(27) = "Esas Faaliyetlerden Net Nakit Akýþý (+/-)"
	descriptions(28) = "Yatýrým Faaliyetlerinden Nakit Akýþlarý"
	descriptions(29) = "Baðlý Ortaklýklardaki Paylarýn Kontrol Kaybýna Neden Olacak Þekilde Elden Çýkarýlmasýndan Nakit Giriþleri"
	descriptions(30) = "Baðlý Ortaklýk Ediniminden Nakit Çýkýþlarý (-)"
	descriptions(31) = "Ýþtirak ve Müþterek Giriþimlerdeki Paylarýn Elden Çýkarýlmasýndan Nakit Giriþleri"
	descriptions(32) = "Ýþtirak ve Müþterek Giriþim Paylarýnýn Ediniminden Nakit Çýkýþlarý (-)"
	descriptions(33) = "Baþka Ýþletme veya Fon Paylarýnýn veya Borçlanma Araçlarýnýn Elden Çýkarýlmasýndan Nakit Giriþleri"
	descriptions(34) = "Baþka Ýþletme veya Fon Paylarýnýn veya Borçlanma Araçlarýnýn Ediniminden Nakit Çýkýþlarý (-)"
	descriptions(35) = "Maddi ve Maddi Olmayan Duran Varlýklarýn Satýþýndan Nakit Giriþleri"
	descriptions(36) = "Maddi ve Maddi Olmayan Duran Varlýk Alýmýndan Nakit Çýkýþlarý (-)"
	descriptions(37) = "Diðer Uzun Vadeli Varlýklarýn Saýþýndan Nakit Giriþleri "
	descriptions(38) = "Diðer Uzun Vadeli Varlýk Alýmlarýndan Nakit Çýkýþlarý (-)"
	descriptions(39) = "Verilen Nakit Avans ve Borçlar (-)"
	descriptions(40) = "Verilen Nakit Avans ve Borçlardan Geri Ödemeler"
	descriptions(41) = "Türev Araçlardan Nakit Giriþleri"
	descriptions(42) = "Türev Araçlardan Nakit Çýkýþlarý (-)"
	descriptions(43) = "Devlet Teþviklerinden Nakit Giriþleri"
	descriptions(44) = "Alýnan Kar Paylarý"
	descriptions(45) = "Ödenen Faiz (-)"
	descriptions(46) = "Alýnan Faiz"
	descriptions(47) = "Vergi Ýadeleri (Ödemeleri) (+/-)"
	descriptions(48) = "Diðer Nakit Giriþleri (Çýkýþlarý) (+/-)"
	descriptions(49) = "Yatýrým Faaliyetlerinden Net Nakit Akýþý (+/-)"
	descriptions(50) = "Finans Faaliyetlerinden Nakit Akýþlarý"
	descriptions(51) = "Baðlý Ortaklýklardaki Paylarýn Kontrol Kaybýna Neden Olmayacak Þekilde Elden Çýkarýlmasýndan Nakit Giriþleri"
	descriptions(52) = "Baðlý Ortaklýklarýn Ýlave Paylarýnýn Ediniminden Nakit Çýkýþlarý (-)"
	descriptions(53) = "Özkaynak Araçlarýnýn Ýhracýndan veya Sermaye Artýrýmýndan Nakit Giriþleri"
	descriptions(54) = "Ýþletmenin Kendi Paylarýný ve Diðer Özkaynak Araçlarýný Almasýyla veya Sermayenin Azaltýlmasýyla Ýlgili Nakit Çýkýþlarý (-)"
	descriptions(55) = "Borçlanmadan Kaynaklanan Nakit Giriþleri"
	descriptions(56) = "Borç Ödemelerinden Nakit Çýkýþlarý (-)"
	descriptions(57) = "Finansal Kiralama Borçlarýndan Nakit Çýkýþlarý (-)"
	descriptions(58) = "Devlet Teþviklerinden Nakit Giriþleri"
	descriptions(59) = "Ödenen Kar Paylarý (-)"
	descriptions(60) = "Ödenen Faiz (-)"
	descriptions(61) = "Vergi Ýadeleri (Ödemeleri) (+/-)"
	descriptions(62) = "Diðer Nakit Giriþleri (Çýkýþlarý) (+/-)"
	descriptions(63) = "Finansman Faaliyetlerinden Net Nakit Akýþý (+/-)"
	descriptions(64) = "Kur Farklarýnýn Etkisinden Önce Nakit ve Nakit Benzerlerindeki Safi Artýþ (Azalýþ) (+/-)"
	descriptions(65) = "Kur Farklarýnýn Nakit ve Nakit Benzerleri Üzerindeki Etkisi (+/-)"
	descriptions(66) = "Nakit ve Nakit Benzerlerindeki Safi Artýþ (Azalýþ) (+/-)"
	descriptions(67) = "Dönem Baþý Nakit ve Nakit Benzerleri"
	descriptions(68) = "Dönem Sonu Nakit ve Nakit Benzerleri"
	
	
	
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










































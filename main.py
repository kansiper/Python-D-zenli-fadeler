import re 
#örnek 1
>>> re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
<_sre.SRE_Match object; span=(12, 17), match='Sinan'>

#örnek 2 
>>> metin = "Merhaba ben Sinan, senin adın nedir?"
>>> metin[12:17]
'Sinan'
#örnek 3
>>> kontrol = re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
>>> kontrol.start()
12
#örnek 4
>>> kontrol = re.search("Sinan","Merhaba ben Sinan, senin adın nedir?")
>>> kontrol.end()
17
#örnek 5
>>> metin = "Merhaba ben Sinan, senin adın nedir?"
>>> kontrol = re.search("Sinan",metin)
>>> kontrol.endpos
36
>>> metin[:36]
'Merhaba ben Sinan, senin adın nedir?'
#örnek 6
>>> print(re.findall("zaman","Tam zamanında geldin, sensiz zaman geçmiyor"))
['zaman', 'zaman']
#örnek 7
>>> print(len(re.findall("zaman","Tam zamanında geldin, sensiz zaman geçmiyor")))
2
#örnek 8
>>> re.findall(".aman","O her zaman, saman altından su yürütürdü.")
['zaman', 'saman']
#örnek 9
>>> re.findall("@g*mail","E-posta adresimiz test@mail.com, test@gmail.com ve test@ggggggmail.com")
['@mail', '@gmail', '@ggggggmail']
#örnek 10
>>> re.findall("@g+mail","E-posta adresimiz test@mail.com, test@gmail.com ve test@ggggggmail.com")
['@gmail', '@ggggggmail']
#örnek 11
>>> re.findall("@g?mail","E-posta adresimiz test@mail.com, test@gmail.com ve test@ggggggmail.com")
['@mail', '@gmail']
#örnek 12
>>> re.findall("[HB]ilal","Hilal ve Bilal çok iyi arkadaştır.")
['Hilal', 'Bilal']
#örnek 13
>>> re.findall("s[ai]m[ei]t","Kardeşim samet, markete simit almaya gitti.")
['samet', 'simit']
#örnek 14
>>> re.findall("[A-Z]ilal","Hilal ve Bilal çok iyi arkadaştır.")
['Hilal', 'Bilal']
#örnek 15
>>> re.findall("[a-z]ilal","Hilal ve Bilal çok iyi arkadaştır.")
[]
#örnek 16
>>> re.findall("[a-z]*a{2}t","Bence saat tamir etmek zor zanaat.")
['saat', 'zanaat']
#örnek 17
>>> re.findall("^Oku","Oku oğul, sesli oku.")
['Oku']
>>> re.findall("^sesli","Oku oğul, sesli oku.")
[]
#örnek 18
metin = "Mustafa başkomiser ve yardımcısı Kemalettin, 34XY6699 plakalı arabanın peşinde."
liste = metin.split()
for i in liste:
  sonuc = re.findall("^[A-Z]+[a-z]+",i)
  if sonuc:
    print(sonuc)

['Mustafa']
['Kemalettin']
#örnek 19
for i in liste:
  sonuc = re.findall("[^A-Za-z-][0-9]+[A-Z]+[0-9]+",i)
  if sonuc:
    print(sonuc)

['34XY6699']
#örnek 20
metin = "Silikon vadisi, google.com ve apple.com arasındaki rekabeti tartışıyor."
liste = metin.split()
for i in liste:
  sonuc = re.search(".com$",i)
  if sonuc:
    print(sonuc.string)

google.com
apple.com

#örnek 21
metin = "Silikon vadisi, google.com ve apple.net arasındaki rekabeti tartışıyor."
liste = metin.split()
for i in liste:
  sonuc = re.search("(.com|.net)$",i)
  if sonuc:
    print(sonuc.string)
#örnek 22
>>> re.findall("(siyah|beyaz)","Beşiktaş, siyah ve beyaz renkleri ile anılır.")
['siyah', 'beyaz']
#örnek 23
>>> re.findall("[0-9]+$","Ekran kartı 150$, ses kartı ise 90$")
[]
>>> re.findall("[0-9]+\$","Ekran kartı 150$, ses kartı ise 90$")
['150$', '90$']
#örnek 24
>>> re.findall("\s","Bil bakalım kaç boşluk var.")
[' ', ' ', ' ', ' ']
>>> len(re.findall("\s","Bil bakalım kaç boşluk var."))
4
#örnek 25
>>> re.findall("\S+","Bil bakalım kaç boşluk var.")
['Bil', 'bakalım', 'kaç', 'boşluk', 'var.']
#örnek 26
>>> re.findall("\d+","Gelirken 1 kilo yoğurt ve 2 adet ekmek alırsın.")
['1', '2']
#örnek 27
>>> re.findall("\w+","Mail adresin sinan%erdinc@test.com mu?")
['Mail', 'adresin', 'sinan', 'erdinc', 'test', 'com', 'mu']
>>> re.findall("\W+","Mail adresin sinan%erdinc@test.com mu?")
[' ', ' ', '%', '@', '.', ' ', '?']


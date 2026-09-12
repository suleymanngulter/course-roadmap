#! Python yalın anlatım
#! Kaynak: aynı dizindeki Python.py notları
#! Bu dosya ders notudur. Çalışan örnekler # ile kapalıdır.
#! Bir bloğu denemek için o bloğun # işaretlerini kaldır.

#  NASIL OKUNUR
#
#  #!  başlık
#  #?  kural / tanım
#  #*  örnek ve alıştırma
#
#  Diyagramlar dosyanın içindedir. Dış görsel yok.


# ============================================================
#  İÇİNDEKİLER
# ============================================================
#
#   01  print, yorum, format, f-string
#   02  değişkenler
#   03  veri tipleri (int str float tuple list set dict)
#   04  operatörler ve tip dönüşümü
#   05  len, eval, input
#   06  string dilimleme ve metotlar
#   07  liste metotları
#   08  if / elif / else
#   09  and / or
#   10  datetime ve random
#   11  for, break, continue
#   12  dict
#   13  iç içe for ve "in"
#   14  while
#   15  try / except
#   16  dosya okuma yazma
#   17  matematik
#   18  fonksiyonlar
#   19  class
#   20  bitirme fikirleri (kısa)
#


# ============================================================
#! 01  PRINT, YORUM, FORMAT
# ============================================================
#? print = ekrana yazdır.
#? #    = tek satır yorum. Python bu satırı çalıştırmaz.
#? """  = birden fazla satır yorum veya çok satırlı metin.

#
#   senin kodun          Python ne yapar
#
#   print("merhaba")  →  ekran: merhaba
#   # print("gizli")  →  hiçbir şey (yorum)
#

# print("hello world")
# print("hello", "world")          #? virgül = ayrı değer, araya boşluk koyar
# print("hello" + "world")         #? + = metinleri yapıştırır (boşluk yok)
# print("hello    " + "world")     #? boşluk karakterdir, kaybolmaz

# print("""selam
#       ben yasin""")             #? üç tırnak alt satıra geçer

# mesaj = "selam python derslerine hoşgeldin!"
# print(mesaj)

# print("front-end", "backend", sep="--")   #? sep: değerlerin ARASINA ne koyayım
# print("selamlar burası", end=" cümle sonu")  #? end: satır sonunda ne olsun (varsayılan \n)


#? f-string: metnin içine değişken göm
#
#   isim = "yasin"
#          │
#          ▼
#   f"Selam {isim}"   →   Selam yasin
#            ^^^^
#            süslü parantez = buraya değişkeni yaz
#

# isim = "yasin"
# print(f"Selam {isim}, Hoşgeldin!")


#? format(): yer tutucu. {} boş kutu, format doldurur.

# print("Selam benim adım {ad}".format(ad="yasin"))

# marka = "BMW"
# print("Benim arabamın markası : {}".format(marka))

# meslek = "web dev."
# yil = 2016
# print("Benim mesleğim {}. Ben {} yılından beri yazılımla uğraşmaktayım".format(meslek, yil))

# isim = "yasin"
# soyisim = "coban"
# print("selamlar ben {1} ve soyadım {0}".format(isim, soyisim))
#? {0} birinci değer, {1} ikinci değer. Sıra numarasıyla yer değiştirirsin.

# print("{1} {3} {2} {0}".format("ben", "python", "öğrenmek", "istiyorum"))

# print("adım: {ad}. soyadım: {soyad}, yaş: {yas}".format(ad="yasin", soyad="coban", yas=23))


# ============================================================
#! 02  DEĞİŞKENLER
# ============================================================
#? Değişken = kutunun adı. İçine bir değer koyarsın, sonra o adla çağırırsın.

#
#   kutu adı          içindeki değer
#   --------          --------------
#   sayi       →      20
#   isim       →      "yasin"
#
#   print(sayi)  ekrana 20 basar, "sayi" yazısını değil.
#


#? KURALLAR
#
#   1sayi = 20              HATA  sayı ile başlama
#   girilen kullanici = ""  HATA  boşluk yok
#   degisken$adi = ""       HATA  özel karakter yok
#
#   girilenIsim = "yasin"   TAMAM  camelCase
#   girilen_yas = 23        TAMAM  snake_case
#

# girilenIsim = "yasin"
# print(girilenIsim)

# sayi = 20
# print(sayi)

# sayi = 20
# sayi = sayi + 1     #? eski 20'yi al, 1 ekle, tekrar sayi'ya koy → 21
# print(sayi)

#
#   KISA YAZIM (aynı kutu üzerinden işlem)
#
#   sayi += 10    aynı    sayi = sayi + 10
#   sayi -= 3     aynı    sayi = sayi - 3
#   sayi *= 2     aynı    sayi = sayi * 2
#   sayi /= 2     aynı    sayi = sayi / 2
#

# sayi = 5
# sayi += 10
# print(sayi)   # 15


#? Çoklu atama
#
#   x, y, z = 5, 10, 15
#      │  │  │     │   │   │
#      └──┴──┴─────┴───┴───┘
#      sırayla eşleşir
#
#   a = b = c = d = "kırmızı"
#   dördü de aynı değeri tutar
#

# x, y, z = 5, 10, 15
# print(z)

# sinav1, sinav2, sinav3 = 50, 70, 90
# print((sinav1 + sinav2 + sinav3) / 3)

# a = b = c = d = "kırmızı"
# print(a, b, c, d)


# ============================================================
#! 03  VERİ TİPLERİ
# ============================================================
#? type(x) = "bu kutu ne tür?" sorusunun cevabı.

#
#   tip        ne tutar              örnek                  değişir mi
#   ---------  --------------------  ---------------------  ----------
#   int        tam sayı              20                     -
#   float      ondalık               1.25                   -
#   str        yazı                  "selam"                yeni str üretir
#   tuple      sabit sıra            ("sarı","mavi")        hayır (immutable)
#   list       değişen sıra          ["a", 23, "x"]         evet
#   set        tekrarsız küme        {12, "python"}         eleman ekle/sil
#   dict       anahtar → değer       {"ad":"yasin"}         evet
#
#
#   list  [ 0 ] [ 1 ] [ 2 ]     sıra var, indeks ile girersin
#   tuple ( 0 ) ( 1 ) ( 2 )     aynı ama içeriği değiştiremezsin
#   set   { a, b, c }           sıra garanti değil, tekrar yok
#   dict  ad → yasin            isimle (key) ulaşırsın, sıra numarasıyla değil
#


# sayi = 20
# print(type(sayi))                 # <class 'int'>

# metin = "selam burada metin yazıyor"
# print(type(metin))                # <class 'str'>

# sayi = 1.25
# print(type(sayi))                 # <class 'float'>


#? tuple — virgülle ayrılmış, parantez opsiyonel
# renkler = "sarı", "mavi", "pembe", "yeşil", "turuncu"
# print(type(renkler))
# print(renkler[0])                 # sarı


#? list — köşeli parantez, karışık tip olabilir
# karisikList = ["a", "b", 23, 44, "x", "y", 76]
# print(type(karisikList))
# print(karisikList[0])             # a   (ilk eleman, indeks 0)


#? set — süslü parantez, key yok. Tek tek garanti sıra vermez → for ile gez.
# degerler = {"renkler", "arabalar", 23, 44, 55}
# print(type(degerler))
# for i in degerler:
#     print(i)


#? dict — "isimle çekmece"
#
#   calisanlar
#   ┌─────────┬────────┐
#   │  isim   │ yasin  │
#   │ soyisim │ coban  │
#   │  yas    │  23    │
#   └─────────┴────────┘
#              │
#              └── calisanlar["yas"]  →  23
#

# calisanlar = {
#     "isim": "yasin",
#     "soyisim": "coban",
#     "yas": 23
# }
# print(calisanlar["yas"])


#? list + dict iç içe: çalışanlar listesi
#
#   [0] { isim: yasin, yas: 23 }
#   [1] { isim: burak, yas: 25 }  ← calisanlar[1]["yas"] → 25
#

# calisanlar = [
#     {"isim": "yasin", "soyisim": "coban", "yas": 23},
#     {"isim": "burak", "soyisim": "yalcin", "yas": 25},
# ]
# print(calisanlar[1]["yas"])


# ============================================================
#! 04  OPERATÖRLER VE TİP DÖNÜŞÜMÜ
# ============================================================
#
#   +   topla          5 + 2   →  7      "ya"+"sin" → "yasin"
#   -   çıkar          5 - 2   →  3
#   *   çarp           5 * 2   →  10     "ab"*2     → "abab"
#   /   böl (float)    5 / 2   →  2.5
#   //  tam böl        5 // 2  →  2
#   %   kalan (mod)    5 % 2   →  1      tek/çift bulmada kullanılır
#   **  üs             10 ** 3 →  1000
#

# print(5 % 2)     # 1
# print(10 % 5)    # 0  tam bölünür

# sayi1 = 20
# sayi2 = 40
# print(sayi1 + sayi2)     # 60  sayı toplama

# sayi1 = "20"
# sayi2 = "40"
# print(sayi1 + sayi2)     # "2040"  yazı yapıştırma

# isim = "yasin"
# soyisim = "coban"
# print(isim + soyisim)    # yasincoban

# sayi1 = "20"
# sayi2 = 40
# print(sayi1 + sayi2)     # HATA  str ile int toplanmaz

# sayi = 10
# sayi = sayi ** 3
# print(sayi)              # 1000


#? Tip dönüşümü: kutunun türünü değiştir
#
#   "23"  --int()-->  23
#    23   --str()-->  "23"
#   45.65 --int()-->  45     (ondalık atılır, yuvarlanmaz)
#
#   int("yasin")  HATA  yazı sayı değildir
#

# sayi = int("23")
# sayi2 = int("24")
# print(sayi + sayi2)      # 47

# sayi = int(45.65)
# print(sayi)              # 45

# sayi = str(23)
# print(type(sayi))        # str

# sayi1 = str(10)
# sayi2 = str(20)
# print(sayi1 + sayi2)     # "1020"


# ============================================================
#! 05  LEN, EVAL, INPUT
# ============================================================
#? len = kaç eleman / kaç karakter / dict'te kaç anahtar

#
#   [1,2,3,4,5,6,7,8,9]     len → 9
#   "selam ben yasin"       len → 15  (boşluk da karakter)
#   {"ad":"..","soyad":".."} len → 2  (key sayısı)
#

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(len(myList))

# mesaj = "selam ben yasin"
# print(len(mesaj))

# person = {"ad": "yasin", "soyad": "coban"}
# print(len(person))


#? eval = string içindeki Python kodunu çalıştırır.
#? Ders için gösterilir. Kullanıcıdan gelen metni eval ile çalıştırma:
#? kötü niyetli kod da çalışır.

# x = "print(25)"
# eval(x)                      # ekrana 25 basar

# result = eval("2 + 3")
# print(result)                # 5

# result = eval("max(1, 2, 3)")
# print(result)                # 3


#? input = kullanıcıdan yazı alır. HER ZAMAN str döner.
#
#   input("Adınız: ")  →  kullanıcı yazar:  20
#                         Python görür:     "20"   (yazı)
#
#   toplama yapacaksan:   int(input("Sayı: "))
#

# isim = input("adınızı giriniz ")
# print("Hoşgeldin " + isim)

# kullaniciAdi = input("Kullanıcı Adiniz : ")
# sifreniz = input("Şifreniz : ")
# print("Hoşgeldin! Kullanıcı Adın : " + kullaniciAdi + " Şifren : " + sifreniz)

# x = int(input("bir sayi giriniz"))
# print(type(x))               # int

# HATALI — yazı + yazı
# sayi1 = input("Sayı girin")
# sayi2 = input("Sayı girin2")
# print(sayi1 + sayi2)         # "1020" gibi yapışır

# DOĞRU
# sayi1 = int(input("Sayı girin"))
# sayi2 = int(input("Sayı girin2"))
# print(sayi1 + sayi2)         # 30


#* input alıştırmaları (hepsi yorum — açınca çalışır)

# isim = input("adınızı giriniz : ")
# soyisim = input("soyadınızı giriniz : ")
# dogumTarihi = input("Doğum tarihinizi giriniz : ")
# print(isim, soyisim, dogumTarihi)

# sayi = input("bir sayı giriniz")
# print(int(sayi) * 3)                         # 3 katı

# girilenSayi = int(input("Bir sayi giriniz :"))
# print(girilenSayi ** 2)                      # kare

# s1 = int(input("1. Sınavı Giriniz : "))
# s2 = int(input("2. Sınavı Giriniz : "))
# s3 = int(input("3. Sınavı Giriniz : "))
# print("Ortalamanız : ", (s1 + s2 + s3) / 3)

# kenar = int(input("Kenar uzunluğunu giriniz : "))
# yukseklik = int(input("Yüksekliği Giriniz : "))
# print("Üçgenin Alanı : ", (kenar * yukseklik) / 2)

# kisa = int(input("Kısa Kenarı Giriniz : "))
# uzun = int(input("Uzun Kenarı Giriniz : "))
# print("Dikdörtgenin Çevresi : ", (kisa + uzun) * 2)

# vize = int(input("Vize notunuzu giriniz : "))
# final = int(input("Final notunuzu giriniz : "))
# print("Ortalamanız : ", int((vize * 0.4) + (final * 0.6)))

# print(len(input("Lütfen Kullanıcı Adınızı Giriniz : ")))

# boy = float(input("Lütfen Boyunuzu Giriniz (1.83) : "))
# kilo = int(input("Lütfen Kilonuzu Giriniz (78) : "))
# print(kilo / (boy * boy))                    # vücut kitle

# maas = int(input("Lütfen Maaşınızı Giriniz"))
# zam = int(input("Zam Oranını Giriniz : "))
# print(f"Zamlı Maaşınız {maas + (maas * zam / 100)}")

# d1 = input("1. Değeri Giriniz : ")
# d2 = input("2. Değeri Giriniz : ")
# d3 = input("3. Değeri Giriniz : ")
# print(d1, d2, d3, sep="**")                  # ahmet**yasin**rojin

# yaricap = int(input("Yarı çapı giriniz : "))
# print(f"Dairenin Alanı : {3 * yaricap * yaricap}\nDairenin cevresi : {2 * 3 * yaricap}")

# girilenIsim = input("Lütfen Adınızı Giriniz")
# print(f"{girilenIsim}\n" * 10)               # for yok, 10 satır

# bosArray = []
# meyveler = input("Meyveleri giriniz (virgülle) : ")
# meyveler = meyveler.split(",")
# print(meyveler)


# ============================================================
#! 06  STRING DİLİMLEME VE METOTLAR
# ============================================================
#? String = karakter dizisi. Her harfin bir index'i vardır. 0'dan başlar.

#
#   metin = "selam ben yasin"
#            0123456789......
#                          -3-2-1   (sondan da sayılır)
#
#   text[:5]    baştan 5 karakter          selam
#   text[:-3]   sondan 3 karakteri at      (geri kalan)
#   text[6:9]   6 dahil, 9 hariç           ben
#   text[-6:]   sondan 6 karakter
#   text[::3]   3'er atlayarak
#
#   [başlangıç : bitiş : adım]
#    dahil       hariç   varsayılan 1
#

# text = "selam ben yasin"
# print(text[:5])
# print(text[:-3])
# print(text[6:9])
# print(text[-6:])
# print(text[::3])


#? lower / casefold  →  hepsi küçük
#? upper             →  hepsi büyük
#? casefold, lower'dan daha agresif (özel harfler)

# text = "SELAM BEN yasin COBAN"
# print(text.lower())
# print(text.casefold())

# text = "selam ben yasin coban"
# print(text.upper())


#? strip  baştaki ve sondaki boşluğu (veya verdiğin karakterleri) siler
#
#   "     selam     "  --strip()-->  "selam"
#   ",,,**yasin**,,,"  --strip(",*")-->  "yasin"
#

# text = "     selam ben yasin coban       "
# print(text.strip())

# text = ",,,....**yasin COBAN,,,....**"
# print(text.strip(",.*"))

#? lstrip  sadece soldan siler
# text = "05453054354"
# print(text.lstrip("0"))          # 5453054354


#? istitle  her kelimenin baş harfi büyük mü? True / False

# print("selam ben yasin coban".istitle())   # False
# print("Selam Ben Yasin Coban".istitle())   # True

# girilenKullanici = input("Adınızı Giriniz (baş harfi büyük) : ")
# if girilenKullanici.istitle():
#     print("Teşekkürler", girilenKullanici)
# else:
#     print("Hatalı Kullanım! Tekrar dene")


#? count  kelime kaç kez geçiyor
# yazi = "Selam ben yazılım çok severim. Çünkü benim işim yazılım"
# print(yazi.count("yazılım"))               # 2
# print(yazi.count("yazılım", 19, 55))       # 19-55 arası ara


#? index  ilk bulunduğu yer. YOKSA HATA.
#? find   ilk bulunduğu yer. YOKSA -1.  (hata fırlatmaz)

#
#   "selam ben yasin"
#         find("ş")   →  -1     (yok)
#         index("k")  →  hata
#

# text = "selam ben yasin coban"
# print(text.index("m"))
# print(text.index("ben"))
# print(text.index("e", 5, 10))
# print(text.find("ş"))                      # -1


#? center  metni verilen genişlikte ortala, kenarları doldur
# print("Neos Yazılım".center(20))
# print("Neos Yazılım".center(50, "*"))

# girilenMetin = input("lütfen bir metin giriniz : ")
# girilenBosluk = int(input("Lütfen Boşluk Sayısını Giriniz : "))
# girilenKarakter = input("lütfen karakter giriniz : ")
# print(girilenMetin.center(girilenBosluk, girilenKarakter))


#? split  yazıyı parçala, liste yap
#
#   "selam ben yasin" .split()      →  ["selam","ben","yasin"]   (boşluktan)
#   "ocak,şubat,mart" .split(",")   →  ["ocak","şubat","mart"]
#

# print("selam ben yasin coban".split())
# aylar = "ocak,şubat,mart,nisan,mayıs,haziran,"
# print(aylar.split(",")[1])                 # şubat

# isimler = input("Ayları virgülle yazınız")
# for i in isimler.split(","):
#     print(i)


#? startswith / endswith  başı / sonu ne ile bitiyor? True/False
# print("selam, ben yasin coban!".endswith("."))     # False
# print("neos akademide yazılım dersleri alıyorum!".startswith("n"))  # True


#? replace(eski, yeni, kaç_kez)
# text = "selam ben yasin coban"
# print(text.replace("selam", "merhaba"))

# tel = input("telefon numaranızı giriniz!")
# if tel.startswith("0"):
#     tel = tel.replace("0", "", 1)          # sadece İLK 0
# print(tel)


#? isnumeric  sadece rakam mı?
# print("5538462904".isnumeric())            # True

# tel = input("telefon (bitişik) : ")
# if tel.isnumeric():
#     print("Teşekkürler")
# else:
#     print("Hatalı Giriş Yapıldı!")


# ============================================================
#! 07  LİSTE METOTLARI
# ============================================================
#? Liste değişir. Metotlar listenin kendisini günceller (çoğu return etmez).

#
#   arabalar:  [ audi ] [ bmw ] [ mercedes ]
#                    0      1         2
#
#   append("renault")     sona ekle
#   insert(1, "react")    1. indexe sok, diğerleri kayar
#   remove("html")        DEĞERE göre sil (ilk eşleşen)
#   del liste[0]          INDEX'e göre sil
#   pop(1)                o indexi sil ve geri ver. pop() = son eleman
#   extend(diger)         diğer listedeki her elemanı tek tek ekle
#   append(diger)         diğer listeyi TEK eleman olarak ekler (iç içe liste)
#

# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# print(list1 + list2)                       # yeni liste birleştirme


# arabalar = ["audi", "bmw", "mercedes"]
# arabalar.append("renault")
# print(arabalar)

# meyveler = ["elma", "armut", "kivi", "ananas"]
# meyveler.append(input("Sevdiğiniz Meyveler : "))
# print(meyveler)

# diller = ["html", "css", "js"]
# girilenDil = input("Yazılım Dillerini Sıralayınız : ").split()
# diller.append(girilenDil)                  # liste içinde liste olur
# print(diller)


# mylist = ["html", "css", "js", "python"]
# mylist.insert(1, "DJANGO")
# print(mylist)                              # html, DJANGO, css, js, python

# mylist = ["html", "css", "js", "python"]
# mylist.remove("html")
# print(mylist)

# myList = ["test1", "test2", "test3", "test4"]
# del myList[0]
# print(myList)

# mylist = ["html", "css", "js", "python", "html", "react", "html"]
# print(mylist.count("html"))                # 3

# mylist = ["html", "css", "js", "python"]
# mylist.reverse()
# print(mylist)

#
#   extend vs append
#
#   front = [html, css, js]
#   back  = [django, c#, php]
#
#   front.extend(back)  →  [html, css, js, django, c#, php]
#   front.append(back)  →  [html, css, js, [django, c#, php]]
#

# front = ["html", "css", "js"]
# back = ["django", "c#", "php"]
# front.extend(back)
# print(front)

# print(sum([1, 2, 3, 4, 5, 6]))            # 21  sadece sayılar

# mylist = ["html", "css", "js", "python"]
# mylist.clear()
# print(mylist)                              # []

# mylist = ["html", "css", "js", "python"]
# mylist.pop(1)                              # css gider
# print(mylist)
# mylist.pop()                               # son eleman gider

#? sort  yerinde sıralar (A-Z veya küçükten büyüğe)
#? sorted(liste, reverse=True)  yeni liste döner, orijinali bozmaz

# ["html", "css", "js", "python"].sort()    # örnek: önce kopya al
# mylist = ["html", "css", "js", "python"]
# mylist.sort()
# print(mylist)

# myList = [11, 99, 22, 42, 12, 67, 32, 78, 23, 1, 4, 77, 99]
# print(sorted(myList, reverse=True))

# sayisalDizi = [1, 20, 40, 23, 11, 190, 2334, 23, 54, 324, 123, 67]
# sayisalDizi.sort()
# sayisalDizi.reverse()
# print(sayisalDizi)


#* liste alıştırması
# list1 = []
# list1.append("muz")
# list1.append("kivi")
# list1.append("elma")
# list1.append("karpuz")
# list1.pop(3)
# list1.insert(3, "patates")
# print(list1)

# list2 = ["javascript", "c#", "java"]
# list2.append("python")
# list2.pop(2)
# print(list2)


# ============================================================
#! 08  IF / ELIF / ELSE
# ============================================================
#? Karşılaştırma True veya False üretir. if o cevaba bakıp yol seçer.

#
#   ==   eşit mi
#   !=   eşit değil mi
#   <    küçük mü
#   >    büyük mü
#   <=   küçük veya eşit
#   >=   büyük veya eşit
#
#   print(44 == 44)  →  True
#   print(44 != 44)  →  False
#
#
#              [ şart ]
#             /       \
#         True         False
#           │             │
#          if            else
#
#
#   birden fazla kapı:
#
#   if     şart1:   ...
#   elif   şart2:   ...     (else if = "değilse şunu dene")
#   elif   şart3:   ...
#   else:           ...     (hiçbiri değilse)
#
#   İlk True olan çalışır, gerisine bakılmaz.
#

# if 44 == 44:
#     print("Doğru")
# else:
#     print("Yanlış")


# yas = int(input("Yaşın kaç"))
# if yas >= 18:
#     print("Reşitsin")
# else:
#     print("Reşit Değilisin.")

# isim = input("Adınız : ")
# yas = int(input("yaşınızı giriniz : "))
# if yas >= 18:
#     print(f"Selam {isim},Reşitsiniz!")
# else:
#     print(f"Selam {isim},Reşit Değilsiniz!")

# sayi1 = int(input("1. Sayıyı Giriniz"))
# sayi2 = int(input("2. Sayıyı Giriniz"))
# if sayi1 == sayi2:
#     print("Girilen İki Sayı Eşit")
# else:
#     print("sayılar eşit değil")

# s1 = int(input("1.Sınav"))
# s2 = int(input("2.Sınav"))
# s3 = int(input("3.Sınav"))
# ortalama = (s1 + s2 + s3) / 3
# if ortalama >= 50:
#     print("Geçtiniz.")
# else:
#     print("Kaldın.")

# say1 = int(input("1. Sayıyı Giriniz : "))
# say2 = int(input("2. Sayıyı Giriniz : "))
# if say1 > say2:
#     print(f"{say1} sayısı {say2} sayısından büyüktür")
# else:
#     print(f"{say1} sayısı {say2} sayısından Küçüktür")

# girilenSayi = int(input("Lütfen Sayıyı Giriniz : "))
# if girilenSayi % 2 == 0:
#     print(f"{girilenSayi} sayısı çifttir")
# else:
#     print(f"{girilenSayi} sayısı tektir")

# alisverisFiyati = int(input("Lütfen alışveriş fiyatınızı giriniz! : "))
# if alisverisFiyati < 100:
#     alisverisFiyati += 15
#     print("Kargo Ücreti 15TL. Toplam Ödenecek Tutar : ", alisverisFiyati)
# else:
#     print("Kargo Ücretsiz! Ücretiniz : ", alisverisFiyati)

# vize = int(input("Vize Notunuzu Giriniz : "))
# final = int(input("Final Notunuzu Giriniz : "))
# ortalama = (vize * 0.4) + (final * 0.6)
# if ortalama >= 50:
#     print("Tebrikler Geçtiniz, Ortalamanız : ", ortalama)
# else:
#     print("Maalesef Kaldınız, Ortalamanız : ", ortalama)
#     but = int(input("Büt Notunuzu Giriniz : "))
#     ortalama = (vize * 0.4) + (but * 0.6)
#     if ortalama >= 50:
#         print("Tebrikler Geçtiniz! Ortalamanız : ", ortalama)
#     else:
#         print("Maalesef Kaldınız, Ortalamanız : ", ortalama)


#? elif örnekleri

# renk = "kırmızı"
# if renk == "mavi":
#     print("Girilen Renk Mavi")
# elif renk == "yeşil":
#     print("Girilen Renk Yeşil")
# elif renk == "kırmızı":
#     print("Girilen Renk Kırmızı")
# else:
#     print("Hatalı Giriş!")

# sayi1 = int(input("1. Sayıyı Giriniz : "))
# sayi2 = int(input("2. Sayıyı Giriniz : "))
# if sayi1 > sayi2:
#     print(f"{sayi1} sayısı {sayi2} sayısından büyüktür!")
# elif sayi2 > sayi1:
#     print(f"{sayi2} sayısı {sayi1} sayısından büyüktür!")
# else:
#     print(f"{sayi1} sayısı {sayi2} sayısına eşittir")

# sayi = int(input("Sayıyı Giriniz : "))
# if sayi < 10:
#     print("Sayı 1 Basamaklıdır")
# elif sayi < 100:
#     print("Sayı 2 Basamaklıdır")
# elif sayi < 1000:
#     print("Sayı 3 Basamaklıdır")
# elif sayi < 10000:
#     print("Sayı 4 Basamaklıdır")
# else:
#     print("Sayı Çok Basamaklıdır :)")
# # alternatif: print(len(str(sayi)))

# sinavNotu = int(input("Notunuzu Giriniz : "))
# if sinavNotu < 45:
#     print("Notunuz 1")
# elif sinavNotu < 55:
#     print("Notunuz 2")
# elif sinavNotu < 69:
#     print("Notunuz : 3")
# elif sinavNotu < 84:
#     print("Notunuz : 4")
# elif sinavNotu <= 100:
#     print("Notunuz : 5")
# else:
#     print("Hatalı Not!")

# sayi1 = int(input("1. Sayıyı Giriniz : "))
# sayi2 = int(input("2. Sayıyı Giriniz : "))
# print("""Toplama : T
# Çıkart : Ç
# Çarp : X
# Böl : B""")
# secilenislem = input("Yapacağınız İşlemin Baş Harfini Yazını : ")
# if secilenislem == "T":
#     print(f"Toplama İşleminin Sonucu : {sayi1 + sayi2}")
# elif secilenislem == "Ç":
#     print(f"Çıkartma İşleminin Sonucu : {sayi1 - sayi2}")
# elif secilenislem == "X":
#     print(f"Çarpma İşleminin Sonucu : {sayi1 * sayi2}")
# elif secilenislem == "B":
#     print(f"Bölme İşleminin Sonucu : {sayi1 / sayi2}")
# else:
#     print("Hatalı bir işlem yaptınız!")

# tiyatro, sinema = 100, 50
# secim = input("Sinema yada Tiyatro! Lütfen Seçiminizi Yapınız.. : ")
# if secim == "sinema":
#     ogrenci = input("Öğrencimisiniz : e/h ")
#     if ogrenci == "e":
#         print("Öğrenci İndirimi Uygulandı! Ödenecek Tutar : ", sinema * 0.5)
#     else:
#         print("Tam Bilet Fiyatı : ", sinema)
# elif secim == "tiyatro":
#     ogrenci = input("Öğrencimisiniz : e/h ")
#     if ogrenci == "e":
#         print("Öğrenci İndirimi Uygulandı! Ödenecek Tutar : ", tiyatro * 0.5)
#     else:
#         print("Tam Bilet Fiyatı : ", tiyatro)
# else:
#     print("HATALI SEÇİM!")


# ============================================================
#! 09  AND / OR
# ============================================================
#? and = VE   ikisi de True olmalı
#? or  = VEYA en az biri True olsa yeter

#
#   kadi=="yasin"  and  sifre=="1a2b3c"
#         │                    │
#       True                 True     →  kapı açılır
#       True                 False    →  kapı kapalı
#       False                True     →  kapı kapalı
#
#   A or B
#   True  or False  →  True
#   False or False  →  False
#

# kadi = "yasin"
# sifre = "1a2b3c"
# if kadi == "yasin" and sifre == "1a2b3c":
#     print("Sisteme Hoşgeldiniz!")
# else:
#     print("Hatalı Giriş Yaptınız!")

# if kadi == "yasin" and sifre == "1a2b3c":
#     print("Sisteme Hoşgeldiniz!")
# elif kadi != "yasin" or sifre != "1a2b3c":
#     print("Kullanıcı adı veya şifre yanlış!")

# say1 = int(input("1. Sayıyı Giriniz"))
# say2 = int(input("2. Sayıyı Giriniz"))
# say3 = int(input("3. Sayıyı Giriniz"))
# if say1 > say2 and say1 > say3:
#     print(say1, " En Büyüktür")
# elif say2 > say1 and say2 > say3:
#     print(say2, " En Büyüktür")
# else:
#     print(say3, " En Büyüktür")

# kadi = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# sifre = input("Lütfen Şifrenizi Giriniz : ")
# if len(kadi) < 8 or len(sifre) < 8:
#     print("8 Karakterden fazla bir kullanıcı adı veya şifre oluşturunuz")
# else:
#     print("Kayıdınız Başarı İle Oluşturuldu! ", kadi)

# fiyatTutar = int(input("Ne kadarlık alışveriş yaptınız : "))
# if fiyatTutar >= 100 and fiyatTutar < 200:
#     print("%10'luk bir indirim Kazandınız! Ödenecek Tutar : ", fiyatTutar - fiyatTutar * 0.10)
# elif fiyatTutar >= 200 and fiyatTutar < 300:
#     print("%15'lik bir indirim Kazandınız! Ödenecek Tutar : ", fiyatTutar - fiyatTutar * 0.15)
# elif fiyatTutar >= 300:
#     print("%20'lik bir indirim Kazandınız! Ödenecek Tutar : ", fiyatTutar - fiyatTutar * 0.20)
# else:
#     print("100 TL altı indirim yok / hatalı giriş")

# sifre = "123"
# bakiye = 2500
# girilenSifre = input("Zırt Bankasına Hoşgeldiniz! \nLütfen Şifrenizi Giriniz : ")
# if girilenSifre == sifre:
#     yapilacakIslem = input("Lütfen Yapmak İstediğiniz İşlemi Yazınız : ")
#     if yapilacakIslem == "para çek":
#         girilenTutar = int(input("Lütfen Bir Tutar Giriniz : "))
#         if girilenTutar < bakiye:
#             bakiye = bakiye - girilenTutar
#             print(f"Para Çekilme İşlemi Tamamlandı! Kalan Tutar {bakiye}")
#         else:
#             print("Yetersiz Bakiye")
#     elif yapilacakIslem == "para yatır":
#         girilenTutar = int(input("Lütfen Bir Tutar Giriniz : "))
#         bakiye = bakiye + girilenTutar
#         print(f"Para Yatırma İşlemi Tamamlandı! Toplam Tutar : {bakiye}")
# else:
#     print("Girilen Parola Hatalı")


# ============================================================
#! 10  DATETIME VE RANDOM
# ============================================================
#? Modül = hazır araç kutusu. import ile içeri alırsın.

#
#   import datetime
#   datetime.datetime.now()
#           │
#           ├── .year .month .day
#           └── .hour .minute .second
#
#   import random
#           ├── randrange(1,10)   1 dahil, 10 hariç rastgele int
#           ├── randint(1,50)     1 ve 50 DAHİL
#           ├── choice(liste)     listeden 1 eleman
#           └── choices(liste, k=3)  listeden 3 eleman (tekrar olabilir)
#

# import datetime
# zaman = datetime.datetime.now()
# print(zaman)
# print(zaman.year, zaman.month, zaman.day)
# print(zaman.hour, zaman.minute, zaman.second)

# import random
# print(random.randrange(1, 10))

# myList = ["elma", "armut", "karpuz", "kavun", "kivi"]
# print(random.choice(myList))

# renkler = ["kırmızı", "mavi", "sarı", "turuncu", "yeşil"]
# print(random.choices(renkler, k=3))

# rndSayi = random.randint(1, 50)
# girilenSayi = int(input("Lütfen Bir Sayı Giriniz : "))
# if girilenSayi == rndSayi:
#     print("Sayıyı Bildiniz!")
# else:
#     print("Bilemediniz!")

# havaDurumu = ["yağışlı", "karlı", "güneşli"]
# rndHavaDurumu = random.choice(havaDurumu)
# if rndHavaDurumu == "yağışlı":
#     print("Bugün Hava Yağışlı! Şemsiyenizi Alınız")
# elif rndHavaDurumu == "karlı":
#     print("Bugün Hava Kar Yağışlı! Lütfen Sıkı Giyininiz")
# elif rndHavaDurumu == "güneşli":
#     print("Bugün Hava Güneşli! Parkta çekirdek kola yapabilirsiniz")


#* çekiliş: kazanan + yedek, seçileni listeden çıkar ki tekrar çıkmasın
# kisiler = input("Kişilerin İsimlerini Giriniz (virgül) : ").split(",")
# kazananSayisi = int(input("Kazanan sayisini giriniz : "))
# yedekSayisi = int(input("Yedek sayisini giriniz : "))
# while len(kisiler) < (kazananSayisi + yedekSayisi):
#     kazananSayisi = int(input("Kazanan sayisini giriniz : "))
#     yedekSayisi = int(input("Yedek sayisini giriniz : "))
# kazananlar, yedekler = [], []
# for i in range(kazananSayisi):
#     rnd = random.choice(kisiler)
#     kazananlar.append(rnd)
#     kisiler.remove(rnd)
# for i in range(yedekSayisi):
#     rnd = random.choice(kisiler)
#     yedekler.append(rnd)
#     kisiler.remove(rnd)
# print(kazananlar)
# print(yedekler)


# ============================================================
#! 11  FOR, BREAK, CONTINUE
# ============================================================
#? for = "şu koleksiyonun her elemanı için bir tur dön"

#
#   range(10)        0,1,2,...,9          bitiş HARİÇ
#   range(5, 10)     5,6,7,8,9
#   range(0, 20, 2)  0,2,4,...,18         adım 2
#
#   for i in range(3):
#       print(i)
#
#   tur 1: i=0
#   tur 2: i=1
#   tur 3: i=2
#   bitti.
#
#
#   break     döngüyü ÖLDÜR, dışarı çık
#   continue  bu turu ATLA, sonraki elemana geç
#   else      döngü break OLMADAN biterse çalışır
#
#   [kırmızı] [mavi] [turuncu] [yeşil]
#      print     print   break!
#                           │
#                           └── yeşil ve sonrası yazılmaz
#
#   continue i==3:
#   0 1 2  (3 atlanır)  4 5 6 7 8 9
#

# for i in range(10):
#     print(i)

# for i in range(20):
#     print("yasin")

# for i in range(5, 10):
#     print(i)

# for i in range(0, 20, 2):
#     print(i)

# havaDurumu = ["yağışlı", "karlı", "güneşli"]
# for i in havaDurumu:
#     print(i)

# myList = [1, 2, 3, 4, 5, 6]
# text = ""
# for i in myList:
#     text += str(i)
# print(text)                                # 123456

# renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "gri", "siyah"]
# for i in renkler:
#     if i == "turuncu":
#         print(i)
#         break

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print("Sayımlar Bitti!")


#* for alıştırmaları
# for i in range(1, 100, 2):
#     print(i)                               # tekler

# for i in range(0, 100, 2):
#     print(i)                               # çiftler

# for i in range(0, 101):
#     if i % 5 == 0:
#         print(i)

# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i)

# tekSayilar, ciftSayilar = [], []
# for i in range(0, 101):
#     if i % 2 == 0:
#         ciftSayilar.append(i)
#     else:
#         tekSayilar.append(i)
# print(f"Tek Sayılar : {tekSayilar}")
# print(f"Çift Sayılar : {ciftSayilar}")

# meyveler = ["elma", "armut", "kavun", "kivi"]
# for i in meyveler:
#     if i == "elma":
#         print(f"{i} 10 TL")
#     elif i == "kivi":
#         print(f"{i} 20 TL")
#     elif i == "kavun":
#         print(f"{i} 30 TL")
#     elif i == "armut":
#         print(f"{i} 40 TL")

# renkler = ["kırmızı", "mavi", "turuncu", "yeşil", "gri", "siyah"]
# for i in renkler:
#     if i == "yeşil":
#         break
#     print(i)

# for i in renkler:
#     if i == "mavi":
#         continue
#     print(i)


#* sayısal loto fikri: 3 rastgele, 3 tahmin, kaç eşleşme
# import random
# tutulansayilar = [random.randint(1, 10) for _ in range(3)]
# girilenBakiye = int(input("Ne Kadarlık Oynamak İstersin!"))
# say1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
# say2 = int(input("Lütfen 2. Sayıyı Giriniz : "))
# say3 = int(input("Lütfen 3. Sayıyı Giriniz : "))
# sayac = 0
# for i in tutulansayilar:
#     if say1 == i or say2 == i or say3 == i:
#         sayac += 1
# if sayac == 3:
#     print(f"Tebrikler! {sayac} adet rakam bildiniz! Kazancınız : {girilenBakiye * 3}")
# elif sayac == 2:
#     print(f"Tebrikler! {sayac} adet rakam bildiniz! Kazancınız : {girilenBakiye * 2}")
# elif sayac == 1:
#     print(f"Amorti! Kazancınız : {girilenBakiye}")
# else:
#     print("Kasa Kazandı :)")


#* 5 haklı sayı tahmini
# import random
# rndSayi = random.randint(1, 50)
# bilinmeSayısı = 1
# for i in range(5):
#     girilenSayi = int(input("Sayıyı Tahmin Ediniz : "))
#     if girilenSayi == rndSayi:
#         print(f"Tebrikler {bilinmeSayısı}. defada Bildiniz!")
#         break
#     else:
#         bilinmeSayısı += 1
#         if i == 4:
#             print("Hakkınız Doldu!")
#         else:
#             print("Bilemedin")


#* 3 haklı şifre
# sifre = "123"
# hak = 3
# for i in range(3):
#     girilenSifre = input("Lütfen şifre giriniz : ")
#     if girilenSifre == sifre:
#         print("Hoşgeldiniz!")
#         break
#     else:
#         hak -= 1
#         if hak == 0:
#             print("Hakkınız Bitti!")
#             break
#         print(f"Hatalı Şifre! Kalan Hakkınız : {hak}")


#* N kullanıcı ekle (liste içinde dict)
# kullanicilar = []
# girilenKullaniciSayisi = int(input("Kaç Adet Kullanıcı Eklemek İsteriniz ?"))
# for i in range(girilenKullaniciSayisi):
#     girilenKullaniciAdi = input("Kullanıcı Adı Giriniz : ")
#     girilenSifre = input("Şifre Giriniz : ")
#     kullanicilar.append({"kadi": girilenKullaniciAdi, "sifre": girilenSifre})
# print(kullanicilar)


#* listedeki kullanıcılardan giriş
# kullanicilar = [
#     {"kadi": "yasin", "sifre": "1234"},
#     {"kadi": "rojin", "sifre": "4567"},
# ]
# girilenKullanici = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Lütfen Şifrenizi Giriniz : ")
# kontrol = False
# for i in range(len(kullanicilar)):
#     if girilenKullanici == kullanicilar[i]["kadi"] and girilenSifre == kullanicilar[i]["sifre"]:
#         kontrol = True
#         break
# if kontrol:
#     print("hg")
# else:
#     print("yanlış şifre")


#* sezar: her harfin ASCII koduna +3, sonra tekrar karaktere çevir
#
#   "a" --ord--> 97  +3 → 100 --chr--> "d"
#

# plainText = "omer yasin"
# mytest = ""
# for i in range(len(plainText)):
#     test = int(ord(plainText[i])) + 3
#     mytest += chr(test)
# print(mytest)


#* yıldız üçgeni
# for i in range(10):
#     print(i * "*")


#* 0'dan N'e toplam
# girilenSayi = int(input("Bir Sayı Giriniz : "))
# toplam = 0
# if girilenSayi > 0:
#     for i in range(girilenSayi + 1):
#         toplam = toplam + i
#     print(toplam)
# else:
#     print("0'dan büyük bir sayı giriniz!")

# tekToplam = 0
# ciftToplam = 0
# girilenSayi = int(input("Bir Sayı Giriniz : "))
# for i in range(girilenSayi + 1):
#     if i % 2 == 0:
#         ciftToplam += i
#     else:
#         tekToplam += i
# print(f"Tek Sayıların Toplamı : {tekToplam} \n Çift Sayıların Toplamı : {ciftToplam}")


# ============================================================
#! 12  DICT
# ============================================================
#? dict = anahtar ile değer. Liste gibi 0,1,2 değil; isimle çekersin.

#
#   kullanici["isim"]          oku
#   kullanici["isim"] = "x"    değiştir (yoksa ekler)
#   kullanici.update({"yas":30})  ekle / güncelle
#   kullanici.pop("isim")      o key'i sil
#   kullanici.popitem()        SON eklenen çifti sil
#
#   .keys()    sadece anahtarlar     isim, soyisim, yas
#   .values()  sadece değerler       yasin, coban, 23
#   .items()   ikisi birden          (isim, yasin), ...
#
#   for k, v in kullanici.items():
#       print(k, v)
#

# kullanici = {
#     "isim": "yasin",
#     "soyisim": "coban",
#     "yas": 23,
#     "numara": 34535
# }
# print(kullanici["isim"])

# kullanici["isim"] = "rojin"
# print(kullanici)

# kullanici.update({"yas": 30})
# print(kullanici)

# kullanici["maas"] = 12345
# print(kullanici)

# kullanici.pop("isim")
# print(kullanici)

# kullanici.popitem()
# print(kullanici)

# kullanici = {
#     "kadi": "yasin",
#     "sifre": "1234",
#     "yas": 23,
#     "meslek": "web dev."
# }
# girilenKullaniciAdi = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Lütfen Şifrenizi Giriniz : ")
# if girilenKullaniciAdi == kullanici["kadi"] and girilenSifre == kullanici["sifre"]:
#     print(f"Hoşgeldin! {kullanici['kadi']}\nYaşın : {kullanici['yas']}\nMeslek : {kullanici['meslek']}")
# else:
#     print("Bilgiler Hatalı")

# kullanici = {"isim": "yasin", "soyisim": "coban", "yas": 23, "numara": 34535}
# for i in kullanici.keys():
#     print(i)
# for i in kullanici.values():
#     print(i)
# for k, v in kullanici.items():
#     print(k, v)

# urunler = {"çikolata": 3, "ekmek": 5, "cips": 4, "meyvesuyu": 2}
# urunFiyatlari = []
# for k, v in urunler.items():
#     urunFiyatlari.append(v)
# print(f"Toplam Ürün Fiyatı : {sum(urunFiyatlari)}")


# ============================================================
#! 13  İÇ İÇE FOR VE "IN"
# ============================================================
#
#   dış for i in range(5):          i = 0
#       iç for j in range(2):         j = 0, j = 1
#                                     (i hâlâ 0)
#                                   i = 1
#                                     j = 0, j = 1
#                                   ...
#
#   "in" = içinde var mı?
#   "a" in ["a","b"]     True
#   "dünya" in "Merhaba dünya!"   True
#   "ad" in kullanicilar          True  (key bakışı)
#

# for i in range(5):
#     for j in range(2):
#         print(i)

# for i in range(11):
#     for j in range(3):
#         print(i)

# for i in range(11):
#     if i == 5:
#         continue
#     for j in range(3):
#         print(i)

# for i in range(11):
#     if i == 3 or i == 7:
#         continue
#     for j in range(2):
#         print(i)

# for i in range(5):
#     print(i * "*")
#     if i == 4:
#         for j in range(5, 0, -1):
#             print(j * "*")

# mylist = ["a", "b", "c", "d", "e", "f"]
# if "a" in mylist:
#     print("Bu liste içerisinde a elementi bulunuyor")
# else:
#     print("bu liste içerisinde bu element yok")

# text = "Merhaba dünya!"
# word = "dünya"
# if word in text:
#     print("Kelime metin içerisinde bulundu.")
# else:
#     print("Kelime metin içerisinde bulunamadı.")

# meyveler = ["elma", "armut", "karpuz", "kivi"]
# renkler = ["kırmızı", "mavi", "yeşil", "turuncu"]
# if "elma" in meyveler and "yeşil" in renkler:
#     print("Her iki arraydede değerler mevcut")
# else:
#     print("değerler bulunmuyor!")

# b = input("Bir harf giriniz: ")
# if b in "aeiouAEIOU":
#     print("Girdiğiniz harf bir sesli harftir.")
# else:
#     print("Girdiğiniz harf bir sessiz harftir.")

# kullanicilar = {"ad": "yasin", "soyad": "coban", "yas": 23}
# if "ad" in kullanicilar:
#     print(kullanicilar["ad"])


# ============================================================
#! 14  WHILE
# ============================================================
#? for: "şu kadar tur / şu listenin her elemanı"
#? while: "şart True olduğu sürece dön"  (sonsuz döngü burada doğar)

#
#   i = 1
#   while i <= 5:
#       print(i)
#       i += 1          ← bunu unutursan sonsuz döngü
#
#   1 → 2 → 3 → 4 → 5 → i=6 şart bozulur, çıkar
#
#   while True:         kasıtlı sonsuz
#       if bitti:
#           break       tek çıkış kapısı
#

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# i = 0
# while i <= 10:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 0
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("Sona erdi")

# i = 0
# while True:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         print(f"{i} Sayısı Çifttir")
#     else:
#         print(f"{i} Sayısı Tektir")
#     i += 1

# i = 1
# toplam = 0
# while i <= 100:
#     if i % 2 == 1:
#         toplam = i + toplam
#     i += 1
# print(toplam)

# kadi = "yasin"
# while True:
#     girilenKadi = input("Kullanıcı Adınızı Giriniz!")
#     if girilenKadi == kadi:
#         print("Hoşgeldiniz!")
#         break

# myList = ["a", "b", 3, 4, 5, 6, 7, 8, 9, 0]
# i = 0
# while i < len(myList):
#     print(myList[i])
#     i += 1

# baslangic = int(input("Başlangıç Değerini Giriniz : "))
# bitis = int(input("Bitiş Değerini Giriniz : "))
# artis = int(input("Artış Değeri Giriniz : "))
# i = baslangic
# while i <= bitis:
#     print(i)
#     i += artis

# girilenDeger = input("Lütfen Değer Giriniz")
# i = 0
# while i < len(girilenDeger):
#     print(girilenDeger[i])
#     i += 1

# baslangic = int(input("Başlangıç Değerini Giriniz : "))
# bitis = int(input("Bitiş Değerini Giriniz : "))
# i = baslangic
# while i <= bitis:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1

# i = 100
# while i > 1:
#     print(i)
#     i -= 1

# i = 0
# dizi = []
# while i < 5:
#     dizi.append(int(input("Deger giriniz:  ")))
#     i += 1
# print(f"Küçükten Büyüğe : {sorted(dizi)}")
# print(f"Büyükten Küçüğe : {sorted(dizi, reverse=True)}")

# urunler = []
# urunMiktari = int(input("Kaç Adet Ürün Eklemek isteriniz : "))
# i = 1
# while i <= urunMiktari:
#     urunIsim = input("Ürün İsimi : ")
#     urunFiyatı = int(input("Ürün Fiyatı : "))
#     urunler.append({"isim": urunIsim, "fiyat": urunFiyatı})
#     i += 1
# for i in urunler:
#     print(f"Ürün İsimleri : {i['isim']} Ürün Fiyatları : {i['fiyat']}")


# ============================================================
#! 15  TRY / EXCEPT
# ============================================================
#? Hata gelince program ölmesin, sen yakala.

#
#   try:
#       tehlikeli iş          (olmayan değişken, olmayan dosya...)
#   except NameError:
#       bu özel hata
#   except:
#       diğer her hata
#   else:
#       hiç hata YOKSA burası
#
#   [ try ] --hata--> [ except ]
#           --tamam--> [ else ]
#

# try:
#     print(x)
# except:
#     print("Böyle Bir Değer Yok!")

# try:
#     print(x)
# except NameError:
#     print("NameError Verdi! x değişkenini göremiyorum")
# except:
#     print("Birşeyler Ters Gitti")

# try:
#     print("selam!")
# except:
#     print("hatalı bir işlem!")
# else:
#     print("Hata Yok Devam Et")

# try:
#     dosya = open("test.txt", "r")
# except:
#     print("Böyle bir dosya yoktur")


# ============================================================
#! 16  DOSYA OKUMA / YAZMA
# ============================================================
#
#   open("test.txt", mod)
#
#   r  oku. dosya yoksa HATA
#   w  yaz. yoksa oluştur, varsa İÇİNİ SİL
#   a  ekle. yoksa oluştur, varsa SONA yaz
#
#   .read()        tüm metin
#   .readline()    bir satır
#   .readlines()   satır listesi (sonlarında \n kalır)
#   .read().splitlines()  satır listesi, \n temiz
#   .write("...")  yaz
#   .close()       kapat (kilidi bırak)
#
#   disk
#    │
#    ├── r ──────────►  bellek  ──► print
#    └── a/w ◄──────── bellek  ◄── senin string'in
#

# dosya = open("test.txt", "r")
# print(dosya.read())

# dosya = open("test.txt", "r")
# print(dosya.readline())                    # sadece ilk satır

# dosya = open("test.txt", "r")
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())

# dosya = open("test.txt", "r")
# for satir in dosya:
#     print(satir)

# dosya = open("test.txt", "r")
# print(dosya.readlines())

# dosya = open("test.txt", "r")
# print(dosya.read().splitlines())

# dosya = open("test.txt", "a")
# dosya.write("selam naber?")
# dosya.close()

# dosya = open("test.txt", "a")
# dosya.write("selam naber")
# dosya.close()
# dosya = open("test.txt", "r")
# print(dosya.read())

# kullanicilar = input("Kullanıcıları Giriniz : ").split(",")
# dosya = open("test.txt", "a")
# for x in kullanicilar:
#     dosya.write(x + "\n")
# dosya.close()
# dosya = open("test.txt", "r")
# print(dosya.read())


# ============================================================
#! 17  MATEMATİK
# ============================================================
#? Hazır fonksiyonlar (import gerekmez): min max abs pow round
#? Daha fazlası: import math   →  sqrt ceil floor

#
#   min(1,2,3)        en küçük     1
#   max(10,20,30)     en büyük     30
#   abs(-20)          mutlak       20
#   pow(2,3)          2 üssü 3     8     ( ** ile aynı iş)
#   round(2.8)        en yakın     3
#   math.sqrt(16)     karekök      4.0
#   math.ceil(2.2)    YUKARI        3
#   math.floor(2.8)   AŞAĞI         2
#

# print(min(1, 2, 3, 4, 5))
# print(max(10, 20, 30, 40, 50))

# girilenDegerKat = int(input("Kaç Adet Değer Gireceksin ? "))
# test = []
# for i in range(girilenDegerKat):
#     test.append(int(input("Lütfen Deger Giriniz : ")))
# print(max(test))

# print(abs(-20))
# print(abs(50 - 60))

# print(pow(2, 3))
# altDeger = int(input("Alt Değeri Giriniz : "))
# ussuDeger = int(input("Üssü Değeri Giriniz : "))
# print(pow(altDeger, ussuDeger))

# print(round(2.8))

# import math
# print(math.sqrt(16))
# print(math.ceil(2.2))
# print(math.floor(2.8))


# ============================================================
#! 18  FONKSİYONLAR
# ============================================================
#? def = "bu işi bir kere yaz, adıyla çağır"

#
#   def toplam(say1, say2):     parametre = dışarıdan gelen kutu
#       sonuc = say1 + say2
#       return sonuc            return = çağıran yere değer gönder
#
#   print(toplam(5, 10))        5 ve 10 argüman
#                 │
#                 ▼
#              15 döner
#
#   return yoksa fonksiyon None döner, sadece içeride print yapar.
#

# def yazdir():
#     print("selamlar ben yasin")
# yazdir()

# def isim():
#     name = input("lütfen adınızı giriniz : ")
#     if name == "yasin":
#         print("TRUE")
#     else:
#         print("FALSE")
# isim()

# def toplam(say1, say2):
#     sonuc = say1 + say2
#     return sonuc
# print(toplam(5, 10))

# def carpma(say1, say2, say3):
#     return say1 * say2 * say3
# print(carpma(1, 1, 1))

# def uzunlukHesapla(sonuc):
#     return len(sonuc)
# print(uzunlukHesapla(input("Lütfen Bir Değer Giriniz : ")))

# def ortalama(say1, say2, say3):
#     return (say1 + say2 + say3) / 3
# print(ortalama(50, 50, 50))

# def ortalama():
#     sin1 = int(input("1. Sınavı Giriniz : "))
#     sin2 = int(input("2. Sınavı Giriniz : "))
#     sin3 = int(input("3. Sınavı Giriniz : "))
#     print(f"Ortalamanız : {(sin1 + sin2 + sin3) / 3}")
# ortalama()

# def ortalama(say1, say2):
#     return (say1 + say2) / 2
# print(ortalama(int(input("1.Sınavı Giriniz : ")), int(input("2.Sınavı Giriniz : "))))


# import random
# def colorPalette():
#     colorHex = "0123456789ABCDEF"
#     newColor = "#"
#     for i in range(6):
#         newColor += random.choice(colorHex)
#     print(newColor)
# if input("Random olarak Color Oluşturmak İster Misiniz?") == "e":
#     colorPalette()
# else:
#     print("Color Oluşmadı")


# def islem(tutar):
#     bakiye = 1000
#     return bakiye - tutar
# if input("Lütfen Şifre Giriniz : ") == "1234":
#     print(islem(int(input("Lütfen Tutar Giriniz : "))))
# else:
#     print("hatalı sifre")


#? fonksiyon başka fonksiyonu çağırabilir
# def carpma(say1, say2):
#     return say1 * say2
# def cikartma():
#     return carpma(2, 2) - carpma(3, 3)
# print(cikartma())


# import random
# yemek = ["pilav", "çorba", "köfte", "bulgur", "patates"]
# def rndYemek():
#     return random.choice(yemek)
# while True:
#     soru = input("Rastgele Yemek Seçmek İçin 1, çıkmak için 2: ")
#     if soru == "1":
#         print(rndYemek())
#         if input("beğendin mi?") == "evet":
#             break
#     elif soru == "2":
#         break


# ============================================================
#! 19  CLASS
# ============================================================
#? class = kalıp. nesne (object) = o kalıptan basılmış ürün.
#? __init__ = nesne doğunca ilk çalışan kurucu. self = "bu nesnenin kendisi"

#
#   class Kisi:                         KALIP
#       def __init__(self, isim, yas):
#           self.isim = isim            bu nesnenin isim rafı
#           self.yas = yas
#       def yazdir(self):
#           print(self.isim, self.yas)
#
#   p1 = Kisi("yasin", 23)              NESNE
#   p1.yazdir()
#
#   class ─────────►  p1 { isim: yasin, yas: 23 }
#          basınca    p2 { isim: burak, yas: 25 }
#

# class ClassOlustur:
#     x = 5
# test = ClassOlustur()
# print(test.x)

# class Kullanici:
#     def __init__(self, isim, sifre):
#         self.isim = isim
#         self.sifre = sifre
# elemanYaz = Kullanici("yasin", "123")
# print(elemanYaz.isim)

# class Kisi:
#     def __init__(self, isim, yas):
#         self.isim = isim
#         self.yas = yas
# k1 = Kisi("yasin", 23)
# print(k1.yas)

# class Kisi:
#     def __init__(self, isim, yas):
#         self.isim = isim
#         self.yas = yas
#     def yazdir(self):
#         print("Selamlar! Adım : ", self.isim, "yaşım", self.yas)
# p1 = Kisi("yasin", 23)
# p1.yazdir()


# ============================================================
#! 20  BİTİRME FİKİRLERİ (orijinal ödevlerin iskeleti)
# ============================================================
#? Aşağıdakiler Python.py'deki bitirme sorularının yalın hali.
#? Tam çözüm orijinal dosyada. Burada "ne isteniyor" net.

#* 1) Rakip sayı tutsun, sen e/h de, hak bitsin.
#* 2) Market: ürün dict'i, while ile ürün seç, hayır deyince toplam.
#* 3) Şifre kırma denemesi: rastgele string üret, eşleşene kadar while.
#* 4) API örneği: urllib + json ile rastgele kullanıcı çek (ileri konu).

#
#   TEK CÜMLELİK HARİTA
#
#   yazdır / oku     print  input
#   kutula           değişken, tip, int() str()
#   metin            dilimleme, split, replace
#   koleksiyon       list  dict
#   karar            if elif else  and or
#   tekrar           for  while  break continue
#   hata             try except
#   disk             open r/w/a
#   paketle          def  class
#


print("Python-Yalin-Anlatim.py not dosyası yüklendi. Örnekler yorumda; bir bloğu açıp dene.")

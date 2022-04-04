#VERİ YAPILARI

#Python'da kullanılan birden fazla veri yapısı var.
#1.LİSTELER
#2.TUPLE
#3.SETLER
#4.SÖZLÜK



#LİSTELER
#değiştirilebilir,kapsayıcı,sıralı.
#liste 2 ayrı yolla oluşturulabilir.
#list()
#[]

notlar = [90,80,45,17]
type(notlar)
liste= ["a",19.52,935,10.5]
liste_cok= ["a",19.52,935,10.5,notlar]
len(liste_cok)

type(liste_cok[0]) #0.indeksteki elemanın tipini gösterir.
type(liste_cok[2])
type(liste_cok[1])
liste_cok[4] #liste_cok un 4.indeksini gösterir.
#del komutu ile liste silinebilir.

#Listeler-Eleman İsimleri

listem = [10,20,30,40,50]
listem[1] #listemin 1.elemanı
listem[9]
listem[0:2] #0'dan 2'ye kadar,2 dahil değil.
listem[:2] #baştan 2ye kadar
listem[1:] #1den en sona kadar

yeniliste = ["a",10,[20,30,40,50]]
yeniliste[2]
yeniliste[2][3]


#LİSTELER ELEMAN DEĞİŞTİRME

liste=["nar","elma" ,"portakal","muz","mandalina"]
liste

#Portakalı Antalya Portakalı olarak değiştirmek istediğimizde
liste[2]
liste[2]="Antalya Portakalı"
liste

liste[2]="portakal"
liste

liste[:4]
liste[:4]="a","b","c","d"

#Listeye yeni bir eleman eklemek istersek

liste=["nar","elma" ,"portakal","muz","mandalina"]
liste

liste + ["kiraz"]
liste
#Kalıcı eklenmedi listemize.Atama işlemi gerçekleştirmemiz lazım.
liste = liste + ["kiraz"]
liste
#Liste içinden eleman silme
del liste[0]
liste


#LİSTE METODLARI
liste_yeni=["ali","ahmet","lamba"]
liste_yeni
dir(liste_yeni)
liste_yeni

#append (eleman eklemek),remove (eleman silmek)

liste_yeni.append("kalem")
liste_yeni

liste_yeni.remove("ahmet")
liste_yeni



liste.insert(0,"aa")
#insert indekse göre eleman eklemek için kullanılır.
liste.insert(len(liste),"ss")

#pop eleman silme metodudur.
liste.pop(0)
liste.pop(4)

#Count sayma metodu
liste=["ali","veli","ayse","ali","ayse","veli","elli"]
liste
liste.count("ali")
liste.count("elli")

#copy metodu (yedeklemek)
liste_yedek = liste.copy()

#extend (iki listeyi kalıcı birleştirmek)
liste.extend (["a","cb","kevser",10])
liste


#index metodu (bir eleman hangi indekste)
liste.index("veli")
liste.index("elli")

#reverse metodu (elemanları terse çevirme)
liste.reverse()
liste

#Sort metodu (sıralama yapmak için kullanılır)
liste = [10,20,35,39,88,95,93,65,72,89,100]
liste.sort()
liste

#clear metodu (liste temizleme)
liste.clear()
liste









































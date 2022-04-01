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

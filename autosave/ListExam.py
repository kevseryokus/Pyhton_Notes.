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

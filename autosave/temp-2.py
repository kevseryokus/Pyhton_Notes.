#VERÄ° YAPILARI

#Python'da kullanÄ±lan birden fazla veri yapÄ±sÄ± var.
#1.LÄ°STELER
#2.TUPLE
#3.SETLER
#4.SÃZLÃK



#LÄ°STELER
#deÄiÅtirilebilir,kapsayÄ±cÄ±,sÄ±ralÄ±.
#liste 2 ayrÄ± yolla oluÅturulabilir.
#list()
#[]

notlar = [90,80,45,17]
type(notlar)
liste= ["a",19.52,935,10.5]
liste_cok= ["a",19.52,935,10.5,notlar]
len(liste_cok)

type(liste_cok[0]) #0.indeksteki elemanÄ±n tipini gÃ¶sterir.
type(liste_cok[2])
type(liste_cok[1])
liste_cok[4] #liste_cok un 4.indeksini gÃ¶sterir.
#del komutu ile liste silinebilir.



#Listeler-Eleman Ä°simleri

listem = [10,20,30,40,50]
listem[1] #listemin 1.elemanÄ±
listem[9]
listem[0:2] #0'dan 2'ye kadar,2 dahil deÄil.
listem[:2] #baÅtan 2ye kadar
listem[1:] #1den en sona kadar 

yeniliste = ["a",10,[20,30,40,50]]
yeniliste[2]
yeniliste[2][3]



#LÄ°STELER ELEMAN DEÄÄ°ÅTÄ°RME

liste=["nar","elma" ,"portakal","muz","mandalina"]
liste

#PortakalÄ± Antalya PortakalÄ± olarak deÄiÅtirmek istediÄimizde
liste[2]
liste[2]="Antalya PortakalÄ±"
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
#KalÄ±cÄ± eklenmedi listemize.Atama iÅlemi gerÃ§ekleÅtirmemiz lazÄ±m.
liste = liste + ["kiraz"]
liste
#Liste iÃ§inden eleman silme
del liste[0]
liste


#LÄ°STE METODLARI
liste_yeni=["ali","ahmet","lamba"]
liste_yeni
dir(liste_yeni)
liste_yeni

#append (eleman eklemek),remove (eleman silmek)

liste_yeni.append("kalem")
liste_yeni

liste_yeni.remove("ahmet")
liste_yeni


#insert ve pop komutları
#indekse göre eleman eklemek için kullanılır.

list=["kahve","nescafe","tchibo","jacobs"]
list


list.insert(0,"1")


list=["kahve","nescafe","tchibo","jacobs"]
list

list[0]="ıce"
list

list.insert(8,"ss")
list

len(list)

list.insert(len(list),"aa")
list

list.pop(4)
list.pop(2)






































































































































































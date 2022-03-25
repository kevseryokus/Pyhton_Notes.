sayi1 = input('1. Sayı : ')
sayi2 = input('1. Sayı : ')
ortalama = (int(sayi1) + int(sayi2)) / 2
print("Ortalama :{0} ".format(ortalama))

vize = input('Vize Notunuz : ')
final = input('Final Notunuz : ')
ortalama = (float(vize) * 0.3) + (float(final) * 0.7)
print("Ortalama :{0} ".format(ortalama))

kisa = input('Kısa Kenar : ');
uzun = input('Uzun Kenar : ');
alan = int(kisa) * int(uzun);
cevre = 2 * (int(kisa) + int(uzun));
print("Alan : {0}".format(alan));
print("Çevre : {0}".format(cevre));

isim = input("Adınızı Girin ");
sayac = 0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
else:
    print("Adının harflerini listeledim.")




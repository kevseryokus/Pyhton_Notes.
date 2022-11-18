#başlangıc seviye,yeniden hatırlamaya yonelik giris notlarım
x = "Kevser"
y = 15
z = "15"

print(x)
print(y)
print(z)

print(x,y,z)
print("jkedwjlwsvwkl",z,y,"kev",2,2.5)

print("T","B","M","M",sep = ".")
print("T","B","M","M")
print("T","B","M","M",sep = "88888....")

print("T","B","M","M",sep = "")
print("K","N","M","L",sep = " ")
print("T","B","M","M",sep=" ",end = "\n")
print("kevser","yokuş")

print("T","B","M","M",sep=" ",end = "")
print("kevser","yokuş")

print("T","B","M","M",sep=" ",end = " ")
print("kevser","yokuş")

print("T","B","M","M",sep=" ",end = "-----")
print("kevser","yokuş")

print("T","B","M","M",sep=" ",end = "-----")

print("T","B","M","M",sep="**")
#sep aralara tırnak içinde yazılanı koyar.En sona koymaz. En sona da end ile koydururuz.
print("T","B","M","M",sep="**",end="**")

print("kivi","portakal")
print("elma","armut")
print("\n" *12)












# IF / ELSE BLOCKS

x = input("enter number:")
x = int(x)

if x==5:
    print("You entered the correct value!")

else:
    print("You entered the wrong value!")
print("----------------------")

x = input("enter number:")
x = int(x)

if x==3:
    print("3 entered!")
else:
    print("3 not entered")

#BOOL ' LA KULLANMA DURUMU
x = input("enter number:")

if bool(x):
    print("full")
else:
    print("empty")

# 3 tırnak koyup alt satırlara da yazı yazabiliyoruz.
#control mechanisms
print("""
[1] addition
[2] extraction
   """)

Login = input("Your choice: ")
if Login =="1":
    print("Toplama sonucu =",5+3)
else:
    print("Cıkarma Sonucu =",5-3)

























































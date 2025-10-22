import sys

#import debug <- import debug.py

#sys.exit() <- run code until this line

print("Hello", "world!", sep=" ", end="\n")

me = "William Allonsius" #string (str)
you = "Yves"
test = "Wesley"

een = 1  #integer
tweeeneenhalf = 2.5  #float
toto = 2,5  #tuple

print(type(me)) #type = opvragen wat de variable is
print(type(een))
print(type(tweeeneenhalf))
print(isinstance(me, str)) #waar of niet waar teruggeven

a = 1
b = 2
c = a + b
d = 2.5
e = c + d
print(e)
print(type(e))

print(2 + 2.0) #optellen
print(1 - 2) #aftrekken
print(2 * 7) #vermenigvuldigen
print(2 / 3) #delen
print(4 // 3) #gehele deling naar beneden
print(7 % 2) #wat er overschiet dus 7/2=3, overschot is 1
print(7 ^ 2) #binaire or 101 = '1'*'2'*'2+1'=5, 100 = 1x2X2 = 4
print(6 >> 1)
print(5 ** 2) # 5 tot de 2de macht = 25

a = 1
#a = "Yves" #eerst "a" gaat overschreven worden door tweede "a"
b = "Toto"
#print(a + b) #a en b samenvoegen
print(" " * 30) #30 spaties printen

x = 1
y = "toto"
#print(x + y) gaat niet = int en str kan niet worden samengevoegd

punten = 80
totaal = 100
resultaat = punten / totaal * 100
print("U behaalde " + str(resultaat) + " punten") #resultaat moet je aanpassen naar een string
print("U behaalde", resultaat, "punten")
print(f"U behaalde {resultaat} punten") #format functie, liefst altijd dit gebruiken ipv bovenstaande 2

i = input("Geef een getal: ")
print("U behaalde", str(int(i) / 100) + " percent") #i is geen int dus je moet er een int van maken maar dan moet je er een str van maken

print(len("Yves")) #aantal characters

# "CTRL" + "/" = alles in commentaar zetten

"""
Dit is één grote lange tekst
Blablabla
Hahaha
"""
print(a) #tekst tussen 3 """ is één grote lange tekst

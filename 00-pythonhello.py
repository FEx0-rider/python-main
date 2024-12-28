#kanál conax

"string je třeba toto:""vnfjls43*-/žýš"
"toto je integer:" 
from os import nice


46248566
-4584
0 #jakákoliv čísla !!celá čísla
"float je necelé číslo"
-15.7   
14.999874
0.0
True 
1
False 
0
"boolean"
print ("ahoj jak se dnes máš já dobře")
# příkaz který řekne ahoj.... !!!!!!! musí obsahovat apostrofi
a = 5
b= 7
c = 8
d = 1
hodně_slov = 0
#více slovné promněnné se píší s podtržítkem místo mezery
print(a + b)
#a plus b
""" toto je poznámka na více řádků
(končí se stejně jako začíná(třemi apostrofi))
"""
print (a < 8)
#a je menší než 8
print (a < d)
#a je menší než d
print (a <= 5)
#a je menší nebo rovno pěti
print (a >= a)
#a je větší nebo rovno než a
print ( a == d)
#a je rovno d 
print(a != 5)
#a se nerovná pěti
print(True and True)
#!!!!!!pozor u True a False vždy velké počáteční 
print(True or False)
print(not not False)
print(not False)
"""
!!! 1 = True
!!! 0 = False
AND:
1 a 1 => 1
1 a 0 => 0
0 a 0 => 0
OR:
1 a 1 => 1
1 a 0 => 1
0 a 0 => 0
NOT:
1 => 0
0 => 1

přednost má not (před and a or)
přednost má and (před or)
or nemá přednost
!!!!# závorky a vše v nich má přednost před: not, and, or
"""

""" >, <, ="""

x = 1
y = 2
z = 3 
if x < y:
    print("program s if funguje jen, když")
    print("podmínka if je splněna")
#podmínka if se vykoná pouze, když je pravdivá (True), 
# když ale není pravidivá není vykonána a přeskočí se tak její příkaz 

if True:
    print("podmínka if se vykonná, protože se rovnou dosadí True")

if x > z or False:
    print("příkaz se nevykonná protože nevýjde True (pravda)")
elif x < z:
    print("příkaz se vykonná protože výjde True (pravda)")


"""elfi musí být vždy po if protože pokud if není pravda (tím pádem se nevypíše)
program pokračuje na elif a pokud elif je pravda tak se vypíše,
ale pokud se if vypíše (protože je pravda) tak program přeskočí elif a tím pádem nemá šanci se vypsat 
"""
if x > z or False:
    print("x je větší než z")
elif z < y:
    print("z je menší než y")
else:
    print("tak nic nevyšlo")

#else se píše na konec a bez podmínek př.(z < y) a tím pádem se vypíše vždy když nevýjde if a následně ani elif


############################################################
#                """TRY, EXCEPT, FINALLY"""               #
############################################################


try:
    vstup1 = int(input("Zdejte číslo 1: "))
except:
    print("zadejde platné číslo.")
    exit()
#try zkusí provést příkaz a pokud to nejde spustí se except a provede kód pod ním
#!!!!! exit() dříve ukončí program // break předčasně ukončí blok ale pouze u ciklů
try:
    vstup2 = int(input("Zdejte číslo 2: "))
except:
    print("zadejde platné číslo.")
    exit()
print("Součet čísel: " +str(vstup1 + vstup2))

try:
    print (a + nic)
except NameError:
    print("chyba")
#except NameError znamená, že except se vykonná pouze když bude NameError(chyba jména) v try

try:
    čísla = int(input("Zdejte číslo: "))
except:
    print("zadejde platné číslo!!.")
finally:
    print("právě skončil blok 1")
# finally vykonná příkaz když skončí buď try nebo except

#while dokud
dokud = 3
while dokud > 0:
    print("dokud je větší než 0 ")
    dokud = dokud - 1  # taky bychom mohyl napsat dokud-= 1 neboli dokud - 1
print("dokud se rovná nebo je menší než nula")
# u while nikdy nedělat cikly

"""IF, ELIF, ELSE"""

a = 0 
x = 0
y = int(input("zadejte číslo: "))
W = int(input("zadejte 1. číslo rozsahu: "))
z = int(input("zadejte 2. číslo rozsahu: "))
if x == 0:
    if y in range(W, z):
        print("číslo je v rozsahu")
    elif x == 0:
        print("číslo není v rozsahu")
    elif a == 1:
        exit()
    else:
        print("chcete ukončit program?")
"""
když je x = 0 tak y je v rozmezí w a z

"""
"""LISTY"""

pozdravy = ["ahoj", "dobrý den", "zdravím", "nazdar"]
hodnoty = ["jablko", 5, True, "červená", 9.1, ["python", 83, "zmrzlina"]]
#toto jsou listy, list je datový typ
print(pozdravy) #vypíše se ["ahoj", "dobrý den", "zdravím", "nazdar"]
print(pozdravy[2]) #vypíše se "zdravím" protože početní řada začíná na nule
"""
"ahoj", "dobrý den", "zdravím", "nazdar"
###########################################
  0       1             2          3
  -4      -3            -2         -1
  """



print(int(9.999) + 7)
# phyton vždy zaohrouhluje dolů

for i in range(0, 5):
    print(i) 
#písmeno i si na sebe vezme dočasnou hodnotu
#tento blok kódu vypíše čísla 0 - 4
"""
SLOVNÍKY
"""

slovnik = {"hodnota1": 4, "hodnota2": 71.2, True: "ahoj"}
#toto je slovník má 3 hodnoty a to: 4, 71.2, "ahoj"
#tyto hodnoty vždy mají nějaké klíče v tomto případě pro hodnotu 4 je klíč: "hodnota1"
print(slovnik["hodnota2"]) #vypíše se hodnota 71.2 která je schovná pod klíčem "hodnota2"

#když chceme přepsat hodnotu uděláme to takto
slovnik["hodnota1"] = "hodnota z 4 se změnila na tento text"  
print(slovnik)

#když chceme přidat hodnotu tak napíšeme neexistující klíč a k tomu hodnotu
slovnik["python"] = "nová hodnota"

print("ahoj mám se dobře", True, 9.33, sep="+", end="\n\n")
print("o dva\n řádky dolů")
#vypíše: ahoj mám se dobře+True+9.33, když necháme prázdné vypíše se bez mezery
# end="\n\n" znamená že příkaz vynechá dva řádky

print(type(12))
# program nám vypíše 'int' (integer)

print(type(print))
# program nám vypíše 'builtin_function_or_method' (vestavěná funkce nebo metoda)

print(len("Toto je len"))
# výsedek bude 11 jako 11 znaků (nepočítají se uvozovky)

print(abs(-61))
# vypíše se 61 (abs jako absolutní hodnota(tedy vzdálenost čísla od nuly))

print(round(9.5))
# zaokrouhlý na číslo 10

print(min(["a", "b", "c"]))
# terminál napíše a jako nejmenší hodnotu

print(max(["a", "b", "c"]))
# terminál napíše c jako největší hodnotu

print(sorted(["c", "a", "b"]))
# python seřadí hodnoty (a, b, c)

print(sorted(["c", "a", "b"], reverse=True))
# python seřadí hodnoty (c, b, a)

print(sum([9, 2, 17]))
# čísla se sečdou dohromady vznikne 28

#conax #12 začátek


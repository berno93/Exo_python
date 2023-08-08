from time import sleep

print("Bienvenue dans notre logiciel de conversion de température Celsius en Fahrenheit")
sleep(1.5)
print("Entrez une température en Celcius °C")
tp= float(input())

def Conversion_tp (tp):
    return (tp*1.8)+32

tp_convertit = Conversion_tp (tp)

print("Vous entrez une température de",tp, "°C")
sleep(0.5)
print("Conversion en cours")
sleep(0.5)
print("Conversion en cours.")
sleep(0.5)
print("Conversion en cours..")
sleep(0.5)
print("Conversion en cours...")
sleep(0.5)
print("Votre température de",tp,"° C est égale à",tp_convertit,"°F")


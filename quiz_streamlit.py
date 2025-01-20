print("Welcome quizzer!")

playing = input("Do you want to play? ")   #inside is the PROMPT

if playing.lower() != "yes":    #!= means: NOT
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Qual è la data della prima mostra impressionista? ")
if answer.lower() == "1884" or "15 aprile 1884":
    print("correct!")
    score += 1
else:
    print("Why the fuck didnt u study?")
    score -= 1

answer = input("I Macchiaioli usavano la linea di contorno? ")
if answer.lower() == "yes" or "no" or "si":
    print("Boh credo di sì, la prof e il libro dicono due cose diverse...")
    score += 1

answer = input("Qual è la sostanza chimica presente nella lastra di feltro di Nièpce? ")
if answer.lower() == "bitume di giude":
    print("Che conoscenza inutile che ora hai aggiunto al tuo bagaglio culturale!")
    score += 1
else:
    print("vabbè potevi non sapere di peggio")
    score -= 1     

answer = input("Quanti dipinti ha fatto Monet della cattedrale di Rouen? ")
if answer.lower() == "50":
    print("Madonna non c'aveva veramente niente da fare")
    score += 1
else:
    print("Bro...")
    score -= 1

answer = input("Chi è il coglione che ha preso un'insufficienza e non ci ha fatto fare una gita in più? ")
if answer.lower() == "scimmia" or "gabriele" or "civale" or "cicala":
    print("Madonna se è scemo...")
    score += 1
else:
    print("No ok questo devi saperlo")
    score -= 1

answer = input("La vitina va al poligono a sparare per divertimento? ")
if answer.lower() == "si":
    print("Si. è decisamente psicopatica")
    score += 1
else:
    print("Non te l'aspettavi? Mi dispiace")
    score -= 1

answer = input("Degas è un impressionista? ")
if answer.lower() == "si":
    print("Se un cane sta sempre con un gruppo di gatti può essere considerato un gatto?")
    score += 1
else:
    print("Si sono d'accordo (probabilmente anche lui)")
    score -= 1

answer = input("La Morisot s'è messa con il fratello di Manet o Monet? ")
if answer.lower() == "manet":
    print("Ehhhhhh fa tipo Olympia lei... wink wink")
    score += 1
else:
    print("Tu le cose importanti non le studi vedo, GOSSIP!!!!!!!!!!")
    score -= 1

answer = input("Quanti peli di cavallo contavano i capelli della bambina di Degas? ")
if answer.lower() == "troppi" or "che schifo":
    print("Le prenotiamo un parrucchiere?")
    score += 1
else:
    print("Non puoi cadermi in questo common knowledge però")
    score -= 1

answer = input("Le spigolatrici si chiamano così perchè mangiano le spigole? ")
if answer.lower() == "no":
    print("Te la do buona ma secondo me dovrebbe essere un sì")
    score += 1
else:
    print("sono d'accordo ma la società ci è avversa")
    score -= 1

print("Hai fatto "+ str(score)+" punti!")
print("Ecco il commento:")

if score<0:
    print("Gabri?")
if 0<score<2:
    print("Sono molto deluso dal tuo rendimento scolastico: devi studiare decisamente di più, era un test facilissimo")
if score< 3:
    print("Vabbè dai poteva andare peggio, forse è anche un buon punteggio rispetto agli altri")
if 4<score<5:
    print("Non male, hai risposto bene a molte domande")
if 6<score<7:
    print("Si no ok tu hai decisamente barato")
if score>8:
    print("ti prego puoi fare te lezione invece che la Vitina?")

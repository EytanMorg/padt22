import socket
import pickle
import time
import chapters


HOST = '127.0.0.1'
PORT = 6000        # Port to listen on (non-privileged ports are > 1023)

#maak een tcp socket aan en bind deze aan de host en poort
s = socket.socket()
s.bind((HOST, PORT))

chapter = chapters.entry() #begin bij het hoofdstuk genaamd "entry"
next = "asciiModt" #binnen dat hoofdtuk beginnen met het dialoog "acsciiModt"

name = "" #variabele wordt in eerste hoofdstuk gezet

#functie om multipleChoice af te handelen (mc.... in chapters.py)
def multipleChoice(chapter, next, name):
    list = []
    #maak een lijst met de vragen
    for item in getattr(chapter, next):
        list.append(item[0])
    #pickle(serialize) dit en stuur naar de frontend
    conn.sendall(pickle.dumps(list))
    #ontvang de index(het nummer) van het antwoord en unpickle(deserialize) dit
    antwoord = pickle.loads(conn.recv(1024))
    #kijk wat de vervolgactie is die bij dit antwoord hoort
    next = getattr(chapter, next)[antwoord][1]
    return next

#functie om de input van de gebruiker te verwerken. word nu alleen gebruik voor de naam van de gebruiken.
def userInput(chapter, next, name):
    #haal de vraag uit het hoofdstuk/dialoog
    input = getattr(chapter, next)[0][0]
    #zet er "input>" voor zodat de frontend weet dat hier een getypt antwoord op moet komen, en vervang _name_ met de naam van de gebruiker
    input = "input> " + input.replace("_name_", name)
    #pickle(serialize) dit en stuur naar de frontend
    conn.sendall(pickle.dumps(input))
    #kijk welke variable het antwoord toegeven krijgt
    target = getattr(chapter, next)[0][1]
    #ontvang het antwoord en unpickle(deserialize) dit
    result = pickle.loads(conn.recv(1024))
    #maak een string van de variable en het antwoord
    var = "{} = '{}'".format(target, result)
    #kijk wat de vervolgactie is
    next = getattr(chapter, next)[0][2]
    #return de vervolgactie en de string van de variable en het antwoord
    return next, var

#functie om simpel dialoog te printen
def showUser(chapter, next, name, num=0):
    while True:
        #kijk wat het dialoog is en zet de naam erin(als dat nodig is)
        dialog = getattr(chapter, next)[num][0]
        dialog = dialog.replace("_name_", name)

        #pickle(serialize) dit en stuur naar de frontend
        conn.sendall(pickle.dumps(dialog))
        #krijg een bevestiging terug
        conn.recv(1024)

        #als de vervolgactie 0 is print dan de volgende regel in de dialoog lijst
        if getattr(chapter, next)[num][1] == 0:
            num += 1

        #zo niet stop dan de loop en return de vervolgactie
        else:
            next = getattr(chapter, next)[num][1]
            num = 0
            break
    return next

#functie om de vlag te controleren, zelfde als de input functie maar dan met een juist/fout antwoord
def checkFlag(chapter,next, name):
    input = getattr(chapter, next)[0][0]
    input = "input> " + input.replace("_name_", name)
    conn.sendall(pickle.dumps(input))
    result = pickle.loads(conn.recv(1024))
    #Einde overeenkomst input()
    #Als het antwoord juist is set dan de vervolgactie uit de flag variable uit het hoofdstuk
    if result == getattr(chapter, next)[0][1]:
        next = getattr(chapter, next)[0][2]
    #Zo niet maak de vervolgactie "wrongFlag"
    else:
        next = "wrongFlag"

    return next



while True:
    #maak varable aan en zorg dat het het type bytes is
    from_client = bytes()
    try:
        #Luister op de socket
        s.listen()
        #Als er een inkomende verbinding is, accepteer deze dan. Dit is blocking: hij blijft wachten op een client, gaat nooit verder zonder
        conn, addr = s.accept()

        with conn:
            while True:
                print(next)

                #besluit wat er moet gebeuren aan de hand van de naam van de vervolgactie
                if next[:2] == "mc": next = multipleChoice(chapter, next, name)
                elif next[:5] == "input":
                    next, var = userInput(chapter, next, name)
                    #maak van de string van userInput() een python actie en voer deze uit
                    exec(var)
                elif next == "flag":
                    next = checkFlag(chapter,next,name)
                elif next[:7] == "chapter":
                    chapter = eval("chapters.{}()".format(next))
                    next = "dialog1"
                else: next = showUser(chapter, next, name)
                #als de vervolgatie back is moet hij dit pas laten zien als de gebruiker de interface weer opent, verbreek de verbinding dus
                if next == "back": raise ValueError('end')
    except Exception as e: print(e)

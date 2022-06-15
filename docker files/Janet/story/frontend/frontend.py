#!/usr/bin/python3
import socket
import pickle
import time
import sys
import signal
import atexit
import termios

#disable keyboard interrupt
signal.signal(signal.SIGINT,signal.SIG_IGN)

HOST = '127.0.0.1'  # The backend's hostname or IP address
PORT = 6000        # The port used by the backend

#enige functie die niet zelf geschreven is, komt van stackoverflow. Het zorgt ervoor dat de gebruiker niks kan typen (of juist weer wel)
def enable_echo(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO

    termios.tcsetattr(fd, termios.TCSANOW, new)

atexit.register(enable_echo, True)
enable_echo(False)

#afhandelen van multiple choice vragen
def vraag_opties(opties):
    num = 1

    #print alle opties
    for optie in opties:
        print("[{}] {}".format(num, optie))
        num += 1

    errors = 0
    del_errors = 0
    while True:
        try:
            #laat de gebruiker weer typen
            enable_echo(True)
            termios.tcflush(sys.stdin, termios.TCIFLUSH)
            #vraag om de keuze
            choice = int(input("Choose a number: "))
            #laat de gebruiker niet meer typen
            enable_echo(False)
            #onthoud de tekst van de keuze
            text = opties[choice - 1]

            #verwijder error regels
            while errors != del_errors:
                print("\033[1A \033[2K \033[1A")
                print("\033[1A \033[2K \033[1A")
                del_errors += 1
            break
        except:
            #als ze een verkeerd nummer geven, of iets anders dan een nummer geef een error en noteer het
            print("Please choose a number")
            errors += 1

    #verwijder keuze regels
    print("\033[1A \033[2K \033[1A")
    for optie in opties:
          print("\033[1A \033[2K \033[1A")

    #print keuze als dialoog
    print_dialog("You> {}".format(text))

    #return de index van de optie lijst
    return choice - 1

#functie om te printen met vertraging tussen letters. text is de teks die pegrint moet worden, nl bepaald on en een nieuwe regel na komt(standaard wel)
def print_dialog(text, nl = True):
    #behandel elke letter in text als individu
    for character in text:
        #print de letter
        sys.stdout.write(character)
        sys.stdout.flush()
        #wacht 0.03 seconden
        time.sleep(0.03)
    #als een nieuweregel geprint meot worden doe dit dan
    if nl: sys.stdout.write("\n")
    #wacht een halve seconde
    time.sleep(0.5)

#maak een tcp socket om met de backend te verbinden
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #verbind met de backend
    s.connect((HOST, PORT))
    #loop om frontend levend te houden
    while True:
        data = None
        #ontvang data van backend
        data = s.recv(1024)
        #als er data is ontvangen behandel het
        if data:
            #unpickle(deserialize) de data
            result = pickle.loads(data)
            #als de data eeen lijst is weten we dat het multiple choice is
            if isinstance(result, list):
                #Verwerk de multipleChoice vragen, pickle(serialize) het antwoord en stuur dit naar de backend
                s.sendall(pickle.dumps(vraag_opties(result)))
            elif isinstance(result, str):
                #als de data "end" is moet de frontend gesloten worden
                if result == "end":
                    #Stuur bevestiging
                    s.sendall(pickle.dumps("ok"))
                    #breek de loop wat het programa beeindigd
                    break
                #als de data begint met "input> " dan moeten we de gebruker vragen te typen
                elif result[:7] == "input> ":
                    #print de ontvangen vraag zonder "input> "
                    print_dialog(result[7:])
                    #print "You> " waar de gebruiker achter kan typen
                    print_dialog("You> ", False)
                    #laat de gebruiker typen
                    enable_echo(True)
                    termios.tcflush(sys.stdin, termios.TCIFLUSH)
                    response = input("")
                    #laat de gebruiker niet meer typen
                    enable_echo(False)
                    #pickle(serialize) het antwoord en stuur dit naar de backend
                    s.sendall(pickle.dumps(response))
                else:
                    #in de data geen lijst, "end" of "input> " dan printen we het als dialoog
                    print_dialog(result)
                    #Stuur een bevestiging
                    s.sendall(pickle.dumps("ok"))

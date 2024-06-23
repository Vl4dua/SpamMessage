import pyautogui
import time

limite = input("Inserisci il numero di volte che desideri inviare il messaggio: ")

# Controlla se l'input non è vuoto
if limite.strip() == "":
    print("Per favore inserisci un numero valido.")
    exit()

try:
    limite = int(limite)
except ValueError:
    print("Per favore inserisci un numero valido.")
    exit()

messaggio = input("Inserisci il tuo messaggio: ")

print("Posiziona il cursore dove desideri inviare il messaggio...")

# Attendi 5 secondi per permettere all'utente di posizionare il cursore
time.sleep(5)

i = 0
while i < limite:
    pyautogui.typewrite(messaggio)
    pyautogui.press('enter') 
    time.sleep(0.5)  
    i += 1

print("Spam completato!")

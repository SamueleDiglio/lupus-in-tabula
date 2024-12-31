# Import delle classi dal file ruoli
from ruoli import Villico, Veggente, Lupo, Indemoniato, Protettore, Medium, giocatori_vivi
# Import di diverse librerie utili per il funzionamento del gioco
import time
import random
import os


# Inizio del programma, output di benvenuto e comunicazione delle regole
print("Benvenuto a Lupus In Tabula!")

# Visualizzazione delle regole generali del gioco
regole = input("Vuoi leggere le regole del gioco? [si/no]: ").strip().lower()	# Vengono usati i metodi .strip() e .lower() per rendere in minuscolo l'input inserito dall'utente e per scartare i possibili spazi inseriti
if regole == "si":
	os.system('cls' if os.name == 'nt' else 'clear')
	input("I villici devono collaborare tra loro per scoprire chi nel villaggio è un impostore." + 
			"\n" + "Durante la notte, oguno è chiamato a svolgere il proprio ruolo, mentre durante il giorno i giocatori devono identificare uno tra di loro da eliminare in base ai sospetti accumulati." + 
			"\n" + "La partita termina quando tutti i lupi vengono scoperti (vittoria dei buoni) oppure quando tutti i buoni vengono eliminati (vittoria dei cattivi)" + 
			"\n" + "Premi invio per chiudere ")
	os.system('cls' if os.name == 'nt' else 'clear')

# Visualizzazione delle informazioni sui ruoli
regole_ruoli = input("Vuoi leggere la descrizione dei ruoli? [si/no]: ").strip().lower()
if regole_ruoli == "si":
	os.system('cls' if os.name == 'nt' else 'clear')
	input("Villico: nessun potere (buoni)" + 
			"\n" + "Lupo: sceglie un giocatore da eliminare durante la notte (cattivi)" + 
			"\n" + "Veggente: scopre se uno tra i vivi è un lupo o meno (buoni)" + 
			"\n" + "Medium: scopre la fazione del linciato dell'ultima giornata (buoni)" + 
			"\n" + "Protettore: ad ogni notte protegge un vivo dai lupi (buoni)" + 
			"\n" + "Indemoniato: nessun potere (cattivi)" + 
			"\n" + "Premi invio per chiudere")
	os.system('cls' if os.name == 'nt' else 'clear')
else:
	os.system('cls' if os.name == 'nt' else 'clear')


# Numero e nomi dei giocatori
nomi_giocatori = []

def numero_giocatori(nomi_giocatori):
	numero_giocatori = int(input("Inserisci il numero di giocatori (da 9 a 11): "))
	while numero_giocatori < 9 or numero_giocatori > 11:	# Controllo numero massimo e minimo dei giocatori
		numero_giocatori = int(input("Inserisci un numero di giocatori valido: "))
	for i in range(numero_giocatori):
		nome = input("Inserisci un nome: ")
		while nome in nomi_giocatori:	# Controllo per impedire giocatori doppi
			nome = input("Un' altro giocatore usa questo nome, inseriscine un altro: ")
		nomi_giocatori.append(nome)


# Estrazione ed assegnazione dei ruoli
def estrazione_ruoli(nomi_giocatori):
	lista_ruoli = []

	if len(nomi_giocatori) == 9:
		lista_ruoli = [Villico(),Villico(),Villico(),Villico(),Lupo(),Lupo(),Veggente(),Medium(),Protettore()]
	elif len(nomi_giocatori) == 10:
		lista_ruoli = [Villico(),Villico(),Villico(),Villico(),Lupo(),Lupo(),Veggente(),Medium(),Protettore(),Indemoniato()]
	else:
		lista_ruoli = [Villico(),Villico(),Villico(),Villico(),Villico(),Lupo(),Lupo(),Veggente(),Medium(),Protettore(),Indemoniato()]

	random.shuffle(lista_ruoli)	# Randomizzazione dell'ordine dei ruoli per l'assegnamento ai giocatori

	diz_giocatori = {}

	for i in range(len(nomi_giocatori)): # Creazione di un dizionario giocatore : ruolo
		diz_giocatori[nomi_giocatori[i]] = lista_ruoli[i]
	return diz_giocatori


# Chiamata delle funzioni numero_giocatori e estrazione_ruoli
numero_giocatori(nomi_giocatori)
giocatori = estrazione_ruoli(nomi_giocatori)
print(giocatori)


# Comunicazione dei ruoli ai giocatori
def comunicazione_ruoli(giocatori):

    os.system('cls' if os.name == 'nt' else 'clear')
    for nome in giocatori.keys():
        input("Venga al pc " + nome + " e prema invio.")
        input("Sei " + str(giocatori[nome]) + ". Premi invio per cancellare. ")
        os.system('cls' if os.name == 'nt' else 'clear') # Cancellazione del messaggio per evitare di comunicare agli altri giocatori il ruolo di quello precedente

# Chiamata della funzione comunicazione_ruoli
comunicazione_ruoli(giocatori)


# Funzione notte
nome_linciato = "Nessuno"
nome_protetto = "Nessuno"

def notte(nome_protetto):
    
    global nome_mangiato
    nome_mangiato = "Nessuno"
    nome_protetto = "Nessuno"

    print("La notte giunge sul villaggio, tutti dormono...")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

    g_vivi = giocatori_vivi(giocatori)
    random.shuffle(g_vivi)	# Shuffle dei giocatori vivi per chiamarli a giocare in ordine randomico

    for nome in g_vivi:
        input("Venga al pc " + nome + " e prema invio")
        personaggio_corrente = giocatori[nome]

        if personaggio_corrente.ruolo == "Lupo":
            nome_mangiato = personaggio_corrente.potere_notturno(giocatori, nome_mangiato) # Chiamata del metodo del potere notturno del lupo
            os.system('cls' if os.name == 'nt' else 'clear')
        elif personaggio_corrente.ruolo == "Villico":
            personaggio_corrente.potere_notturno(giocatori) # Chiamata del metodo del potere notturno del villico
            os.system('cls' if os.name == 'nt' else 'clear')
        elif personaggio_corrente.ruolo == "Veggente":
            personaggio_corrente.potere_notturno(giocatori) # Chiamata del metodo del potere notturno del veggente
            os.system('cls' if os.name == 'nt' else 'clear') 
        elif personaggio_corrente.ruolo == "Indemoniato":
            personaggio_corrente.potere_notturno(giocatori) # Chiamata del metodo del potere notturno dell'indemoniato
            os.system('cls' if os.name == 'nt' else 'clear')
        elif personaggio_corrente.ruolo == "Protettore":
            nome_protetto = personaggio_corrente.potere_notturno(giocatori, nome_protetto) # Chiamata del metodo del potere notturno del protettore
            giocatori[nome_protetto].vivo = True
            os.system('cls' if os.name == 'nt' else 'clear')
        elif personaggio_corrente.ruolo == "Medium":
            personaggio_corrente.potere_notturno(giocatori, nome_linciato) # Chiamata del metodo del potere notturno del medium
            os.system('cls' if os.name == 'nt' else 'clear')
	# Verifica dell'uccisione del giocatore scelto dai lupi
    if giocatori[nome_protetto] is not giocatori[nome_mangiato]:	# Se il nome scelto dai lupi non coincide con quello del scelto dal protettore, il giocatore viene mangiato
      giocatori[nome_mangiato].vivo = False
    else:
       giocatori[nome_mangiato].vivo = True	# Se il nome coincide, il giocatore non viene mangiato
       nome_mangiato = "nessuno"
            


# Funzione giorno
def giorno(nome_mangiato):
    
	global nome_linciato
	nome_linciato = "Nessuno"
	timer = 120
		
	print("Arriva il giorno. Tutto il villaggio si risveglia.")
	time.sleep(5)
	os.system('cls' if os.name == 'nt' else 'clear')

	print("Questa notte è stato mangiato " + nome_mangiato + "\n")	# Comunicazione del nome del giocatore che è stato mangiato
	print("Giunge il momento delle discussione: avete 2 minuti per esporre i vostri sospetti e decidere chi linciare")
	time.sleep(5)
	# Countodown del tempo rimanente per la decisione del giocatore da linciare
	while timer > 0:
		print(timer)
		timer -= 1
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')  
		
	print(giocatori_vivi(giocatori))	# comunicazione dei giocatori ancora in vita
	nome_linciato = input("Chi avete scelto di linciare oggi?: ")
	giocatori[nome_linciato].vivo = False
    
# Controllo del vincitore \per continuare o interrompere il gioco
def controlla_vincitore():
	numero_non_lupi_vivi = 0
	numero_lupi_vivi = 0
	for nome in giocatori.keys():
		if giocatori[nome].vivo and giocatori[nome].ruolo == "Lupo":
			numero_lupi_vivi += 1
		elif giocatori[nome].vivo:
			numero_non_lupi_vivi +=1

	if numero_lupi_vivi >= numero_non_lupi_vivi:
		return "cattivi"
	elif numero_lupi_vivi == 0: 
		return "buoni"
	else:
		return "Nessuno"


# Ciclo giorno/notte e incoronamento della classe vincitrice
vincitore = 'Nessuno'

while vincitore == 'Nessuno':
	notte(nome_protetto)   # Chiamata della funzione notte
	vincitore = controlla_vincitore()	# Controllo di un possibile vincitore
	if vincitore == 'Nessuno':
		giorno(nome_mangiato)    # Chiamata della funzione giorno
		vincitore = controlla_vincitore()	# Controllo di un possibile vincitore

# Comunicazione del vincitore
print("Hanno vinto i " + vincitore + "!")	
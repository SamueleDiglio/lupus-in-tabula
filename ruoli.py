import os

# Creazione della lista contenente i giocatori vivi
def giocatori_vivi(giocatori):
	g_vivi = []
	for nome in giocatori.keys():
		if giocatori[nome].vivo == True:
			g_vivi.append(nome)
	return g_vivi


class Personaggio:
	def __init__(self,ruolo,fazione):
		self.ruolo = ruolo
		self.fazione = fazione
		self.vivo = True
	
	def __str__(self):
		return self.ruolo

	def __repr__(self):
		return self.ruolo

# Classe del ruolo Villico
class Villico(Personaggio):
	def __init__(self):
		super().__init__('Villico', 'buoni')

	# Il villico non ha un potere notturno, ma gli viene richiesto ugualmente di inserire un nome per non far capire agli altri giocatori il suo ruolo
	def potere_notturno(self,giocatori):
		nome = input("Ciao Villico. Purtroppo la natura non è stata molto grata con te: non hai nessun potere. Per non far capire che sei un inutile villico, scrivi il nome di un giocatore vivo: ")
		while (nome not in giocatori_vivi(giocatori)):	# Controllo che il giocatore scelto sia vivo
			nome = input("Non sei stato in grado di scrivere nemmeno il nome di un giocatore. Per favore riprova scrivendo il nome di un vivo. " + "\n" + "I vivi sono :" + str(giocatori_vivi(giocatori)) + ": ")
		input("Bravo, sei stato molto utile. Premi invio per cancellare.")
		os.system('cls' if os.name == 'nt' else 'clear')

# Classe del ruolo Veggente
class Veggente(Personaggio):
	def __init__(self):
		super().__init__('Veggente', 'buoni')

	# Al veggente viene chiesto di inserire il nome di un giocatore in vita per scoprire se si tratta o meno di un lupo
	def potere_notturno(self, giocatori):
		nome = input("Ciao Veggente. Con te il fato è stato clemente e hai la possibilità di scoprire chi tra i giocatori è un infame. Inserisci il nome di uno dei tuoi compagni di viaggio vivi per scoprire se è un lupo oppure no: ")
		while (nome not in giocatori_vivi(giocatori)):	# Controllo che il giocatore scelto sia vivo
			nome = input("Il fato ti avrà pur dato molti doni, ma l'intelligenza non è sicuramente uno tra quelli. Devi inserire il nome di un giocatore vivo. " + "\n" + "I vivi sono :" + str(giocatori_vivi(giocatori)) + ": ")
		if giocatori[nome].ruolo == "Lupo":
			print("Ottima scelta, il giocatore che hai esaminato è un lupo, fai in modo che venga eliminato")
		else:
			print("Poteva andare meglio, il giocatore esaminato non è un lupo, ma non scoraggiarti: FORSE puoi fidarti di lui")
		input("Per questa notte il tuo lavoro qui è finito, premi invio per cancellare.")
		os.system('cls' if os.name == 'nt' else 'clear')

# Classe del ruolo Indemoniato
class Indemoniato(Personaggio):
	def __init__(self):
		super().__init__('Indemoniato', 'cattivi')

	# L'indemoniato non ha un potere notturno, ma gli viene richiesto ugualmente di inserire un nome per non far capire agli altri giocatori il suo ruolo
	def potere_notturno(self, giocatori):
		nome = input("Ciao Indemoniato. Come sai, il tuo potere è non avere un potere. Un po' inutile, non credi? Ma non è il caso di farlo sapere agli altri, quindi scrivi il nome di un giocatore vivo per non farti scopirire: ")
		while (nome not in giocatori_vivi(giocatori)): # Controllo che il giocatore scelto sia vivo
			nome = input("Oltre ad essere inutile sei anche stupido. Per favore, inserisci il nome di un giocatore vivo: ")
		input("Ora puoi tornare ad essere inutile, ma al tuo posto. Premi invio per canecellare.")
		os.system('cls' if os.name == 'nt' else 'clear')
     

# Classe del ruolo Lupo
class Lupo(Personaggio):
	def __init__(self):
		super().__init__('Lupo', 'cattivi')

	# Al lupo viene chiesto di inserire il nome di un giocatore da mangiare. Quando ci sono due lupi in gioco, il giocatore che viene mangiato sarà quello scelto dal secondo lupo a essere chiamato a giocare
	def potere_notturno(self, giocatori, nome_mangiato):
		print("Ciao Lupo, è arrivato il momento di scegliere chi tra i buoni sarà il tuo pasto di questa notte. Per evitare di commettere un cannibalismo e mangiare un tuo simile, ecco chi sono i lupi: ")
		for nome in giocatori:
			if giocatori[nome].ruolo == "Lupo":
				print(nome)
		nome_mangiato = input("Quindi, chi tra i giocatori vivi decidi di fare fuori questa notte?: ")
		while nome_mangiato not in giocatori_vivi(giocatori):	# Controllo che il giocatore scelto sia vivo
			nome_mangiato = ("Vuoi mangiare delle ossa? Devi inserire il nome di un giocatore vivo: ")
		input("Un pasto delizioso. Ora premi invio per cancellare e ricorda, non farti scoprire.")
		os.system('cls' if os.name == 'nt' else 'clear')
		return nome_mangiato


# Classe del ruolo Medium
class Medium(Personaggio):
	def __init__(self):
		super().__init__('Medium', 'Buoni')


	# Al medium viene comunicato la fazione del giocatore linciato durante l'ultima giornata. Gli viene poi chiesto di inserire un nome per non far capire agli altri giocatori il suo ruolo
	def potere_notturno(self, giocatori, nome_linciato):
		print("Ciao medium, hai il pregio di poter comunicare con i giocatori dei quali non si è fidato il villaggio (I morti per intenderci, un po' macabro vero?)")
		if nome_linciato == "Nessuno":
			print("Durante l'ultima giornata nessuno è stato linciato. Mi spiace, ma per questa notte sei inutile quanto un villico")
		elif giocatori[nome_linciato].ruolo == "Lupo" or giocatori[nome_linciato].ruolo == "Indemoniato":
			print("Il giocatore che è stato linciato la scorsa notte era dei cattivi. Sei hai dei sospetti in base a questo nome fatti valere, altrimenti non depistare le indagini altrui: saresti meno utile di un villico.")
		else:
			print("Il giocatore che è stato linciato la scorsa notte era dei buoni. Usa questa informazione a tuo piacimento, ma mi raccomando, sii più utile di un villico.")
		nome = input("Per non rivelare agli altri il tuo importante ruolo, fingi di scrivere il nome di un giocatore vivo: ")
		while (nome not in giocatori_vivi(giocatori)):
			nome = input("Devi inserire il nome di un vivo: ")	# Controllo che il giocatore scelto sia vivo
		input("Torna domani per scoprire la fazione del nuovo linciato. Ora, premi invio per cancellare.")
		os.system('cls' if os.name == 'nt' else 'clear')


# Classe del ruolo Protettore
class Protettore(Personaggio):
	def __init__(self):
		super().__init__('Protettore', 'buoni')

	# Al protettore viene chiesto di inserire il nome di un giocatore da proteggere, il quale non potrà essere eliminato durante questa notte
	def potere_notturno(self, giocatori, nome_protetto):
		nome_protetto = input("Ciao Protettore. Il tuo ruolo è fondamentale: hai la possibilità di sottrarre qualcuno da una sorte terribile. Tra i vivi, chi decidi di proteggere questa notte?: ")
		while (nome_protetto not in giocatori_vivi(giocatori)):	# Controllo che il giocatore scelto sia vivo
			nome_protetto = input("Come pensi di proteggere un morto? Spetterebbe a te essere mangiato... Devi inserire il nome di un giocatore vivo: ")
		input("Bene, ora qualcuno potrà stare tranquillo, ma tu invece? Potresti aver appena protetto un lupo. Nel dubbio, premi invio per cancellare.")
		os.system('cls' if os.name == 'nt' else 'clear')
		return nome_protetto
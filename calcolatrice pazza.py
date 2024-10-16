import random
frasi_scherzose = [
    "Hmm, la tua matematica mi sta confondendo!",
    "Non sono sicuro, ma il risultato è questo... forse é:",
    "Risultato incerto, ma prova a fidarti di me! il numero che dovrebbe uscire è:",
    "Aspetta, devo chiamare un matematico... ok, ecco il risultato!",
    "Calcolatrice stanca, risultato è approssimativo me te lo do lo stesso!",
    "Questo numero sembra sospetto, ma te lo do comunque:",
    "Sei sicuro di voler sapere la risposta? Eccola:",
    "Risultato generato con un pizzico di follia! eccolo brutto scemo di merda: ",
    "Sto improvvisando... il risultato potrebbe essere giusto ma nache sbagliato. nel caso lo voglia sapere è: ",
    "Mmm, sì, potrebbe essere corretto... forse, per me è: ",
    "Faccio finta di sapere cosa sto facendo. Ecco il numero: ",
    "Il risultato è così grande che anche Einstein si confonderebbe! il risualtato è: ",
    "Questo numero mi sembra giusto... oppure no? forse è: ",
    "Non mi fido di questo risultato, ma eccolo comunque: ",
    "La matematica non è il mio forte oggi! ma ci provo lo stesso, mi è uscito: ",
    "Non chiedermi come ci sono arrivato. Ecco il risultato: ",
    "Risultato calcolato sotto pressione... sii clemente, cazzo! Il risultato è:",
    "Ho fatto del mio meglio, ma potrebbe essere sbagliato. Il reisultato è: ",
    "Spero tu non stia facendo affidamento su questo risultato! Il risultato ovviamente è: ",
    "Penso che questo sia giusto, ma il dubbio è grande! Per me è: "
]
frasi_errore_numero = [
    "Ehm... mi sa che ti sei dimenticato un numero!",
    "Non so fare magie senza numeri!",
    "Aspetto il numero... prima o poi arriverà?",
    "Sembra che tu abbia dimenticato il pezzo più importante: il numero!",
    "Niente numeri, niente matematica! Dai, inseriscine uno.",
    "Calcolatrice in sciopero finché non vedo un numero!",
    "Ho bisogno di numeri, non aria fritta!",
    "Non sono un indovino, inserisci un numero!",
    "Mi dispiace, ma senza numeri è difficile fare calcoli!",
    "Il numero dove l'hai nascosto? Dai, non farmi lavorare troppo!",
    "Il numero è sparito! Non posso calcolare senza di lui.",
    "Senza numeri mi sento un po' inutile!",
    "Inserire un numero sarebbe un'idea geniale, sai?",
    "Sto ancora aspettando un numero... non essere timido!",
    "Puoi riprovare? Magari con un numero stavolta!",
    "Non posso calcolare il nulla! Inserisci qualcosa.",
    "Calcolatrice in pausa fino a quando non vedo un numero!",
    "Sicuro che non ti sei dimenticato di qualcosa? Tipo un numero?",
    "Ho bisogno di input numerici per fare il mio lavoro... non idee astratte!",
    "Sei creativo, ma la matematica ha bisogno di numeri!"
]
sino=["no","si"]
operazioniLista=["somma","differenza","divisione", "moltiplicazione"]
def operazioni(numero1, numero2, operazione):
    if operazione == "somma":
        return numero1 + numero2 #finisci qua 
try:
    numeroUtente1=int(input("inserisci un numero "))
    numeroUtente2=int(input("inserisci un numero "))
    operazioni=input("che operazione vuoi fare")
    while operazioni not in operazioniLista:
        print("che cazzo hai messo, ti eìsempbra una operazione? Tranquillo ti do un'altra possibilità")
        operazioni=input("che operazione vuoi fare")
    fraseSiNo=random.sample(sino,1)
    if fraseSiNo[0] == "si":
        frase=random.sample(frasi_scherzose,1)   
        print(frase[0], numeroUtente) 
    elif fraseSiNo[0]=="no":
        print("il risualtato è: ", numeroUtente)

#aggingi arriabitao, triste, felice  
except ValueError:
    errore=random.sample(frasi_errore_numero,1)
    print(errore[0])





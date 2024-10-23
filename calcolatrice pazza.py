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

frasiArrabiato = [
    "Davvero avevi bisogno di aiuto per fare questa operazione? Che operazione di merda che mi hai fatto fare! Era così semplice che non te lo dovrei dire, ma il risultato è ",
    "Non riesci a risolvere nemmeno questo? Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "Questo era un problema per te? Sul serio? Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "Hai chiesto aiuto per questa banalità? Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "Ma ti rendi conto di quanto fosse facile? Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "Non ci credo che hai avuto bisogno di aiuto per questo. Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "Hai davvero avuto bisogno di aiuto per questo? Povero me. Che operazione di merda che mi hai fatto fare! Il risultato è ",
    "E pensavi che fosse difficile? Ma per favore. Che operazione di merda che mi hai fatto fare! Il risultato è "
]

frasiCalme = [
    "Oh, tranquillo, non tutti riescono a farlo al primo tentativo. Il risultato comunque è ",
    "Non preoccuparti, capita di sbagliare cose semplici. Il risultato è ",
    "Sì, direi che potevi farcela da solo... Ma visto che ci sono, il risultato è ",
    "Non era proprio una sfida difficile, ma ecco il risultato: ",
    "Nessun problema, ci siamo passati tutti. Il risultato è ",
    "Beh, la prossima volta ci riuscirai da solo, sono sicuro. Il risultato è ",
    "Va bene, te lo dico lo stesso. Il risultato è ",
    "Non c'era fretta, è normale chiedere aiuto. Il risultato è "
]

frasiPaura = [
    "Oh no, spero di non sbagliare... il risultato è... oh mamma... è ",
    "Sono un po' nervoso a dirtelo... ma ecco il risultato... spero che vada bene: ",
    "Non sono sicuro di volerlo dire... ma il risultato è... ",
    "Mi tremano le mani mentre te lo dico... il risultato è ",
    "Questo è davvero inquietante... ma ok, il risultato è... ",
    "Ti prego, non arrabbiarti... ma il risultato è ",
    "Non so se voglio vedere cosa succede dopo... il risultato è ",
    "Sto sudando freddo, ma... ecco il risultato: "
]


sino=["no","si"]
operazioniLista=["somma","differenza","divisione", "moltiplicazione"]
def operazioni(numero1, numero2, operazione):
    if operazione == "somma":
        return numero1 + numero2 
    elif operazione =="differenza":
        return numero1-numero2
    elif operazione =="divisione":
        sn=input("vuoi avere un risultato con o senza virgola ")
        while (sn != "con la virgola" or sn != "senza la virgola"):
            sn=input("vuoi avere un risultato con o senza virgola ")
        if (sn=="con la virgola"):
            return numero1/numero2
        elif (sn == "senza la virgola"):
            return numero1//numero2
    elif operazione == "moltiplicazione":
        return numero1*numero2



def emozioni(risultato):
        if(risultato>0 and risultato<30):
            return random.choice(frasiArrabiato)
        elif(risultato>30 and risultato<1000):
            return random.choice(frasiCalme)
        elif(risultato>1000 or risultato<0):
            return random.choice(frasiPaura)


try:
    numeroUtente1=int(input("inserisci un numero "))
    numeroUtente2=int(input("inserisci un numero "))
    operazionis=input("che operazione vuoi fare")
    while operazionis not in operazioniLista:
        print("che cazzo hai messo, ti eìsempbra una operazione? Tranquillo ti do un'altra possibilità")
        operazionis=input("che operazione vuoi fare")
    numeroUtente=operazioni(numeroUtente1,numeroUtente2,operazionis)

    frase=emozioni(numeroUtente)
    print(frase, numeroUtente) 

except ValueError:
    errore=random.sample(frasi_errore_numero,1)
    print(errore[0])


        




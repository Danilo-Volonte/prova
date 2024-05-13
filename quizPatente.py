import random
"""
1 --> il  rimo numero indica la categoria 
2 --> nel secondo numero 
3 --> s550 è l'immagine (la libreria del imagini la darà il professore qunado ci sarà il test )
3 --> 
1) leggere il file
2( estrarre 10 domande DIVERSE)
3) mostro domande e immagini se serve e confornto risposte
4) stampo punteggio
"""
def leggiFile():
     domande=[]
     f=open("quiz.txt")
     "laggo file e lo trasferisxo in memoria in questo caso ci metto delle tuple dove abbbiamo la domanda e la risposta giusta"
     """
      tutto quello dentro prima è in una funzione
     """
     riga = f.readline()
     while riga != "":
          for linea in f:
               categoria, bo, immagine, bo2, testo, risposta = linea.strip().split(";")
               risposte=(immagine,testo,risposta)
               domande.append(risposte)
               riga=f.readline()
     rispondi(domande)
     f.close()
def rispondi(lista):
     giuste=0
     sbagliate=0
     for i in range(10):
          domandePrese=random.sample(len(lista),10)
          risposta = input(lista[domandePrese][1]).append()
          while risposta != "V" or risposta != "V":
            if lista[domandePrese][3] == risposta:
             print("giusta") 
             giuste+=1
          else:
             print("sbagliato")
             sbagliate+=1
leggiFile()

          

     

leggiFile()
"impiccato"
import random
def fareLista():
    parole=[]
    f=open("parole.txt")
    riga=f.readline()
    while riga !="":
        riga=f.readline().strip()
        parole.append(riga)
    f.close()
    parole.pop(-1)
    print(parole)
    indovina(parole)

def indovina(lista):
   numero=random.randint(1,(len(lista)-1))
   parola=lista[numero]
   prendereLettere=input("vuoi acquistare qualche lettera")
   for i in parola:
      lettere = []
      if i not in lettere:
         lettere.append(i)
   print(lettere)    
   acquisto=[]
   if prendereLettere == "sì":
      numeroLettere=random.randint(1,len(lettere))
      acquisto.append(lettere[numeroLettere])
   else:
      parolaIndovinare=""
      for i in parola:
         if i in acquisto:
            parolaIndovinare+=i
         else:
            parolaIndovinare+="#"
            
fareLista()
   
   

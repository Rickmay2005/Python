diz={}

import pprint
pp=pprint.PrettyPrinter(indent=4)

def leggiDati():
  global cod,fila,num,prezzo,data,nGiorni,opzione
  cod=input("Inserisci il codice =")
  fila=input("Inserisci la fila =")
  while len(fila)==0:
    fila=input("Inserisci la fila =")
  num=input("Inserisci il numero =")
  while len(num)==0:
    num=input("Inserisci il numero =")
  prezzo=input("Inserisci il prezzo =")
  data=input("Inserisci la data =")
  nGiorni=input("Inserisci il numero di giorni")
  opzione=input("Inserisci l'opzione")
  diz[cod]=[fila,num,prezzo,data,nGiorni,opzione]
 
def leggiChiave():
  cod = 0
  cod+1

def cerca():
  leggiChiave()
  if((cod) in diz):
    print(diz(cod))
  else:
    print("Ombrellone non esistente")

def tutti():
  print(diz)

def leggiPrezzoValido():
  prezzo=input("Inserisci prezzo: ")
  while len(prezzo)!=0:
    prezzo=input("Inserisci prezzo:  ")

def leggiDataValido():
  data=input("Inserisci la data:  ")
  while len(data)==0:
    data=input("Inserisci la data: ")
  return data

def leggiNGiorniValido():
  nGiorni=input("Inserisci il numero di giorni  ")
  while len(nGiorni)==0:
    nGiorni=input("Inserisci il numero di giorni ")
  return nGiorni

def leggiDatiValido():
  return [leggiPrezzoValido(), leggiDataValido(), leggiNGiorniValido()]

def modifica():
  chiave = leggiChiave()
  if(chiave in diz):
    diz[chiave] = leggiDataValido()
  else:
    print("L'ombrellone non è presente")

def totMese():
  tot = 0
  mese=input("Inserire il mese")
  while len(mese)==0:
    mese=input("Inserisci il mese ")
  tot=prezzo+opzione
  return tot

def VisPre():
  opz = 0
  while (opz!=0):
    mese=input("Inserire il mese")
  opz+=mese
print(diz[cod])

def MesMin():
  min=0
for i in range(len(diz[cod])):
  if(min<diz[cod][i][2]):
    min=diz[cod][i][2]
print(min)



scelta=1
while (scelta!=0):
  print('0) Esci')
  print('1) Popola')
  print('2) Mostra le prenotazioni di un ombrellone')
  print('3) Mostra tutte le prenotazioni')
  print('4) Riduzione prezzo percentuale')
  print('5) Calcolo incasso totale di un mese')
  print('6) Visualizza le prenotazioni di n mesi')
  scelta=int(input('Scegli :'))
  if scelta==1:#Spinarelli 09:58
    n=(int(input("Inserisci n persone da aggiungere")))
    for i in range(n):
      leggiDati()
  elif scelta==2:
    cerca()
  elif scelta==3:
    tutti()
  elif scelta==4:
    modifica()
  elif scelta==5:
    totMese()
  elif scelta==6:
    VisPre()
  elif scelta==7:
    MesMin()

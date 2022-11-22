#1
#Creazione dizionario
diz={"Giuseppe Gullo" : [("Corsa campestre",(40,21,0),"Allievi"),("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
     "Antonia Barbera":[("Corsa campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
     "Nicola Esposito":[("Corsa campestre",(0,43,22),"Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19),"Juniores mas")]}

#2
#Aggiunta al dizionario
diz["Riccardo Maggioni"]=[("Corsa campestre",(20,11,0),"Allievi"),("Corsa 100mt",(10,42,0),"Juniores mas"),("Corsa 200mt",(0,15,19),"Juniores mas")]

#3 #9:37 Gornati
#tramite un ciclo for e una serie di if aggiungo in ciascuna chiave la disciplina
for chiave in diz:
  if (chiave=="Giuseppe Gullo"):
    diz["Giuseppe Gullo"].append(("Corsa ad ostacoli 400mt",(0,40,34),"Allievo")) #.append aggiunge un'elemento alla fine del vettore
  if (chiave=="Antonia Barbera"):
    diz["Antonia Barbera"].append(("Corsa ad ostacoli 400mt",(0,39,10),"Allieva")) 
  if (chiave=="Nicola Esposito"):
    diz["Nicola Esposito"].append(("Corsa ad ostacoli 400mt",(0,40,26),"Allievo")) 
  if (chiave=="Riccardo Maggioni"):
    diz["Riccardo Maggioni"].append(("Corsa ad ostacoli 400mt",(0,40,26),"Allievo")) 

#4 #9:30 Gornati
#Mostro le informazioni sulla disciplina "Campestre" dell'atleta Giuseppe Gullo
print(diz["Giuseppe Gullo"][0])

#5 #9:30 Gornati
#Informazione sulla corsa 200mt dell'atleta Nicola Esposito
print(diz["Nicola Esposito"][2])

#6 #10:46 Gornati
#Stampo i valori del tempo di Antonia Barbera nella corsa 100mt
print(diz["Antonia Barbera"][1][1])

#7 #10:26 Gornati
#Prendo le tre chiavi nel dizionario e in seguito prendo i valori della corsa 100mt. In seguito stampo il minimo
min=0
minx=0
mino=0
for i in diz:
  if(i=="Giuseppe Gullo"):
    min=diz["Giuseppe Gullo"][1][1]
for i in diz:
  if(i=="Nicola Esposito"):
    minx=diz["Nicola Esposito"][1][1]
for i in diz:
  if(i=="Riccardo Maggioni"):
    mino=diz["Riccardo Maggioni"][1][1]
if(min<minx and mino):
  print(min)
elif(minx<min and mino):
  print(minx)
else:
  print(mino)
 
#8 #10:45 Gornati
#Prendo le tre chiavi nel dizionario e in seguito prendo i valori della corsa 200mt. In seguito stampo il massimo
max=0
maxx=0
mas=0
for i in diz:
  if(i=="Giuseppe Gullo"):
    max=diz["Giuseppe Gullo"][2][1]
for i in diz:
  if(i=="Nicola Esposito"):
    maxx=diz["Nicola Esposito"][2][1]
for i in diz:
  if(i=="Riccardo Maggioni"):
    mas=diz["Riccardo Maggioni"][2][1]
if(max>maxx and mas):
  print(mas)
elif(maxx>max and mas):
  print(maxx)
else:
  print(mas)
 
#9
#Prendo le tre chiavi nel dizionario e in seguito prendo i valori della corsa campestre. In seguito stampo la media
med=0
medi=0
me=0
for i in diz:
  if(i=="Giuseppe Gullo"):
    med=diz["Giuseppe Gullo"][0][1]
for i in diz:
  if(i=="Nicola Esposito"):
    medi=diz["Nicola Esposito"][0][1]
for i in diz:
  if(i=="Riccardo Maggioni"):
    me=diz["Riccardo Maggioni"][0][1]
tmed=int(med+medi+me)/3 
print(tmed)

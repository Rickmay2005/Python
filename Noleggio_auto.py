#1
diz={"AA123BB":[("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],#creazione dizionario
     "AB345CD":[("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
     "CD456FF":[("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}
#2
diz["ZZ999MR"]=[("Giugno",10,15000),("Luglio",10,15000),("Agosto",10,15000),("Settembre",10,15000)]#aggiunta al dizionario
#3
print(diz["AA123BB"][1])#posizione 1 s'intende il mese ovvero luglio
#4
print(diz["AA123BB"][1][1])#con il primo uno si entra nel mese mentre nel secondo 1 entro nel numero di noleggio
#5
cont=0
for i in range(len(diz["AB345CD"])):#lunghezza dizionario
  cont+=diz["AB345CD"][i][2]#cont+= alla chiave del dizionario con i che parte dalla posizione 1 (giugno) e prende la posizione 2 (km)
print(cont)
#6
cont=0
for i in range(len(diz["AA123BB"])):#lunghezza dizionario
  cont+=diz["AA123BB"][i][2]+diz["AB345CD"][i][2]+diz["CD456FF"][i][2]+diz["ZZ999MR"][i][2]#somma di tutti i km delle varie macchine
print(cont)
#7
max=0
for i in range(len(diz["CD456FF"])):
  if(max<diz["CD456FF"][i][2]):#ogni volta che max è < del numero di km prende quel numero come valore
    max=diz["CD456FF"][i][2]
print(max)

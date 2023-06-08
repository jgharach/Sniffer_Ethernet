 #Importation des librairies 
import struct
import mysql.connector
import json
#Importation des fonctions locales
from decodage_udp import decodage_udp
from decodage_arp import decodage_arp
from fonction_decodage import extraction

fic_binaire = "Vt_DEMO_power_on/ethernet.result_data" # Fichier binaire comportant les trames à décoder 
fic_rep = "Vt_DEMO_power_on/Vt_DEMO_power_on.rep" # Fichier comportant la configuration du test
id_test = 1 # Identification du test nécéssaire pour l'importation des trames dans la base
 
f = open("Decodage_trame/fonction_transfert.json", "r") # Ouverture du fichier fonction transfert 
FT = json.load(f) # Déserialisation des données
f.close() # Fermeture du fichier fonction transfert 

f = open(fic_binaire, "rb") # Ouverture du fichier binaire comportant les trames
trames = [] # Création d'une liste vide pour stocker les trames
try:
	while True: # Lecture de toutes les trames du fichier binaire
		data = f.read(28) # Lecture des 28 premiers octets 
		date1, date2, bench_3, bench_4_5_6, framesize = struct.unpack('>ddIII', data) # Décommutation des 28 premiers octets en big endian
		mask = 0b00000000000011110000000000000000  # Masque de 4 bits pour récupérer sélectionner les 4 bits du bench_5 parmi 4 octets 
		bench_5 = (bench_4_5_6 & mask) >> 16 # Décalage vers la droite de 16 bits pour obtenir les bits de poids fort
		trame = f.read(framesize) # Taille de la trame stocké dans une variable 
		field_1 = struct.unpack_from('>H', trame, 12) # Décommutation du field 1
		field_1 = hex(field_1[0]) # Conversion en hexadécimal
   		# Condition déterminant si c'est une trame udp ou arp
		if field_1 == "0x800": 
			# Appel d'une fonction decodage_udp et ajoute les données de la trame udp dans la liste trames
			trames.append(decodage_udp(date2, bench_3, bench_5, framesize, trame, FT))
		elif field_1 == "0x806":
			 # Appel d'une fonction decodage_arp et ajoute les données de la trame arp dans la liste trames
			trames.append(decodage_arp(date2, bench_3, bench_5, framesize, trame, FT))
		else:
			break # Casse la boucle True si les 2 premières conditions ne sont plus satisfaites
	f.close() # Fermeture du fichier binaire
except struct.error: # Capture l'exception struct.error
    None 

donnees_test = extraction(fic_rep, "r") # Appel d'une fonction extraction venant récupérer les données de la configuration du test 
 
for trame in trames: # Boucle affichant toutes les trames
    print(trame) 

print(donnees_test) # Affiche les données de la configuration du test

# Connexion à la base de données
 
db = mysql.connector.connect(
    host="localhost", 
    user="gj200498",  
    password = "gj2004987503", 
    database = "gj200498"
)

cursor = db.cursor() # Créer l'objet curseur

# Insére le nom et la date d'exécution du test dans la table test
sql = "INSERT INTO test (id_test, nom_test, date_execution) VALUES (%s, %s, %s)" 
val = (id_test, donnees_test[4], donnees_test[3]) 
cursor.execute(sql, val)

# Insére les trames dans la table trame
for trame in trames:		
	if trame[7] == "0x800":
		req_udp = """ INSERT INTO trame (framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, 
  		field_1, field_2, field_3, field_4, field_5, field_6, field_7, src_ip, dest_ip, field_9, field_10, field_11, 
   		field_14, field_16, field_17, field_18, field_20, field_21, field_23, field_25, field_26, field_28, field_29, 
    	field_30, field_32, packet_date, num_test) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
     	%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s,%s)"""
		val_udp = trame + (id_test,) # Ajout d'un numéro pour identifier le test 
		cursor.execute(req_udp, val_udp)
	elif trame[6] == "0x806":
		req_arp = """INSERT INTO trame (framedate, bench_3, bench_5, framesize, mac_dest, mac_src, 
  		field_1, field_2, field_3 , field_4, field_5 , field_6, mac_sender,sender_ip ,mac_target,target_ip, num_test) 
  		VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		val_arp = trame + (id_test,)  # Ajout d'un numéro pour identifier le test 
		cursor.execute(req_arp, val_arp) 
  
#db.commit() # Confirme la transaction à ne faire qu'une seule fois pour ne pas avoir de trames doubles
# Ferme le curseur et la connexion à la base 
cursor.close()
db.close()
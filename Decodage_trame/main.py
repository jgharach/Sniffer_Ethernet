# Importation des fonctions pour le décodage des trames et l'importation des données dans la base de données 
import mysql.connector
from fonction_decodage import extraction
from decodage import decodage

fic_binaire = "Vt-DEMO_mem_observability/ethernet.result_data" # Fichier binaire comportant les trames à décoder 
fic_rep = "Vt-DEMO_mem_observability/Vt_DEMO_mem_observability.rep" # Fichier comportant la configuration du test
id_test = 3 # Identification du test de manière unique nécéssaire pour l'importation des trames dans la base de donnnées

trames = decodage(fic_binaire)
donnees_test = extraction(fic_rep) # Appel d'une fonction extraction venant récupérer les données de la configuration du test 

for trame in trames:
	print(trame) # Affichage des trames
print(donnees_test) # Affichage de la configuration du test 

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
     	%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s,%s)""" # Requête SQL qui va importer les données des champs d'une trame UDP
		val_udp = trame + (id_test,) # Ajout d'un numéro pour identifier le test de manière unique 
		cursor.execute(req_udp, val_udp) # Exécute la requête SQL
	elif trame[6] == "0x806":
		req_arp = """INSERT INTO trame (framedate, bench_3, bench_5, framesize, mac_dest, mac_src, 
  		field_1, field_2, field_3 , field_4, field_5 , field_6, mac_sender,sender_ip ,mac_target,target_ip, num_test) 
  		VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" # Requête SQL qui va importer les données des champs d'une trame ARP
		val_arp = trame + (id_test,)  # Ajout d'un numéro pour identifier le test de manière unique
		cursor.execute(req_arp, val_arp) # Exécute la requête SQL
  
#db.commit() # Confirme la transaction à ne faire qu'une seule fois pour ne pas avoir de trames doubles
# Ferme le curseur et la connexion à la base 
cursor.close()
db.close()

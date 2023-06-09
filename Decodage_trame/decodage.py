#Importation des librairies 
import struct
import json
#Importation des fonctions nécessaire pour le decodage du fichier binaire
from decodage_udp import decodage_udp
from decodage_arp import decodage_arp 

def decodage(fic_binaire):
	"La fonction decodage prend en entrée le fichier binaire à décoder et retourne en résultat une liste contenant les trames décodées"
	f = open("Decodage_trame/fonction_transfert.json", "r") # Ouverture du fichier fonction transfert 
	FT = json.load(f)# Déserialisation des fonctions transfert 
	f.close() # Fermeture du fichier fonction transfert 

	f = open(fic_binaire, "rb") # Ouverture du fichier binaire comportant les trames
	trames = [] # Création d'une liste vide pour stocker les trames
	try:
		while True: # Lecture de toutes les trames du fichier binaire
			data = f.read(28) # Lecture des 28 premiers octets 
			date1, date2, bench_3, bench_4_5_6, framesize = struct.unpack('>ddIII', data) # Décommutation des 28 premiers octets en big endian
			mask = 0b00000000000011110000000000000000  # Masque de 4 bits pour récupérer sélectionner les 4 bits du bench_5 parmi 4 octets 
			bench_5 = (bench_4_5_6 & mask) >> 16 # Décalage vers la droite de 16 bits pour obtenir les bits de poids fort
			trame = f.read(framesize) # Taille de la trame lu dans le fichier stocké dans une variable 
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
				break # Interrompte la boucle True si les 2 premières conditions ne sont plus satisfaites
		f.close() # Fermeture du fichier binaire
	except struct.error: # Capture l'exception struct.error
		None 
	return trames
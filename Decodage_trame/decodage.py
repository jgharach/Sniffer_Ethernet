import struct
import mysql.connector
import time
import json
from decodage_udp import decodage_udp
from decodage_arp import decodage_arp

start_time = time.time()
f = open("Decodage_trame/fonction_transfert.json", "r")
FT = json.load(f)
f.close()
f = open("Vt_DEMO_power_on/ethernet.result_data", "rb")
trames = []
try:
	while True:
		data = f.read(28)
		date1, date2, bench_3, bench_4_5_6, framesize = struct.unpack('>ddIII', data)
		mask = 0b00000000000011110000000000000000  
		bench_5 = (bench_4_5_6 & mask) >> 16
		trame = f.read(framesize)
		field_1 = struct.unpack_from('>H', trame, 12)
		field_1 = hex(field_1[0])
		if field_1 == "0x800":
			trames.append(decodage_udp(date2, bench_3, bench_5, framesize, trame, FT))
		elif field_1 == "0x806":
			trames.append(decodage_arp(date2, bench_3, bench_5, framesize, trame, FT)) 
		else:
			break
except struct.error:
    None
 
for trame in trames:
    print(trame)
    
end_time = time.time()
temps_execution = end_time - start_time
print("Temps d'execution", temps_execution)

db = mysql.connector.connect(
    host="localhost", 
    user="",  
    password = "", 
    database = ""
)
cursor = db.cursor()

sql = "INSERT INTO test (nom_test, date_execution) VALUES (%s, %s)"
val = [
  	("Vt_DEMO_mem_observability", "22-09-01 17-14-48"),
  	("Vt_DEMO_power_on", "22-09-06 09-46-53")
]	
cursor.executemany(sql, val)
for trame in trames:		
	if trame[7] == "0x800":
		req_udp = "INSERT INTO trame (framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3, field_4, field_5, field_6, field_7, src_ip, dest_ip, field_9, field_10, field_11, field_14, field_16, field_17, field_18, field_20, field_21, field_23, field_25, field_26, field_28, field_29, field_30, field_32, packet_date, num_test) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s,%s)"
		val_udp = trame + (1,)
		cursor.execute(req_udp, val_udp)
	elif trame[6] == "0x806":
		req_arp = "INSERT INTO trame (framedate, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3 , field_4, field_5 , field_6, mac_sender,sender_ip ,mac_target,target_ip, num_test) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val_arp = trame + (1,)
		cursor.execute(req_arp, val_arp) 

for trame in trames:		
	if trame[7] == "0x800":
		req_udp = "INSERT INTO trame (framedate, MID, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3, field_4, field_5, field_6, field_7, src_ip, dest_ip, field_9, field_10, field_11, field_14, field_16, field_17, field_18, field_20, field_21, field_23, field_25, field_26, field_28, field_29, field_30, field_32, packet_date, num_test) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s,%s)"
		val_udp = trame + (2,)
		cursor.execute(req_udp, val_udp)
	elif trame[6] == "0x806":
		req_arp = "INSERT INTO trame (framedate, bench_3, bench_5, framesize, mac_dest, mac_src, field_1, field_2, field_3 , field_4, field_5 , field_6, mac_sender,sender_ip ,mac_target,target_ip, num_test) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val_arp = trame + (2,)
		cursor.execute(req_arp, val_arp)
#db.commit()
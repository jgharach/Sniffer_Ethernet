import struct
from decodage_udp import*
from decodage_arp import*
from fonction_decodage import*
f = open("Vt-DEMO_mem_observability/ethernet.result_data", "rb")
while True:
	data = f.read(28)
	date1, date2, bench_3, bench_4_5_6, framesize = struct.unpack('>ddIII', data)
	mask = 0b00000000000011110000000000000000  
	bench_5 = (bench_4_5_6 & mask) >> 16  
	trame = f.read(framesize)
	field_1 = struct.unpack_from('>H', trame, 12)
	field_1 = hex(field_1[0])
	if field_1 == "0x800":
		print(decodage_udp(date2, bench_3, bench_5, framesize, trame))
	else:
		print(decodage_arp(date2, bench_3, bench_5, framesize, trame))

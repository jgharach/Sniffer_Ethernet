import struct
import datetime
from datetime import timedelta
from fonction_decodage import*
def decodage_udp(date2, bench_3, bench_5, framesize, trame):
	trame_udp = struct.unpack_from('>12B5H2BH8B7H2BH2BI2H', trame)
	macd1 = trame_udp[0]
	macd2 = trame_udp[1]
	macd3 = trame_udp[2]
	macd4 = trame_udp[3]
	macd5 = trame_udp[4]
	macd6 = trame_udp[5]	
	macs1 = trame_udp[6]
	macs2 = trame_udp[7]	
	macs3 = trame_udp[8]
	macs4 = trame_udp[9] 
	macs5 = trame_udp[10]
	macs6 = trame_udp[11]
	field_1 = trame_udp[12]	
	field_2 = trame_udp[13]	
	field_3 = trame_udp[14]
	field_4 = trame_udp[15]
	field_5 = trame_udp[16] 
	field_6 = trame_udp[17]
	field_7 = trame_udp[18]
	field_8 = trame_udp[19]
	src_ip1 = trame_udp[20]
	src_ip2 = trame_udp[21]
	src_ip3 = trame_udp[22]
	src_ip4 = trame_udp[23] 
	dest_ip1 = trame_udp[24]
	dest_ip2 = trame_udp[25]
	dest_ip3 = trame_udp[26] 
	dest_ip4 = trame_udp[27]
	field_9 = trame_udp[28] 
	field_10 = trame_udp[29]
	field_11 = trame_udp[30]
	field_12 = trame_udp[31]
	field_13_14_15_16_17_18 = trame_udp[32]
	field_19_20 = trame_udp[33]
	field_21 = trame_udp[34] 
	field_22_23_24_25_26 = trame_udp[35] 
	field_27_28 = trame_udp[36]
	field_29_30 = trame_udp[37]
	field_31 = trame_udp[38]
	field_32 = trame_udp[39]
	field_33_34 = trame_udp[40]
	field_35 = trame_udp[41]
	field_36 = trame_udp[42]

	macdest = adr_mac(macd1, macd2, macd3, macd4, macd5, macd6)
	macsrc = adr_mac(macs1, macs2, macs3, macs4, macs5, macs6)
	src_ip = adr_ip(src_ip1, src_ip2, src_ip3, src_ip4)
	dest_ip = adr_ip(dest_ip1, dest_ip2, dest_ip3, dest_ip4)
	
	mask_field_14 = 0b0001000000000000
	mask_field_16 = 0b0000011100000000
	mask_field_17 = 0b0000000011100000
	mask_field_18 = 0b0000000000011111
	mask_field_20 = 0b0011111111111111
	mask_field_23 = 0b00001000
	mask_field_25 = 0b00000010
	mask_field_26 = 0b00000001
	mask_field_28 = 0b00111111
	mask_field_29 = 0b1111110000000000
	mask_field_30 = 0b0000001111111111

	field_14 = (field_13_14_15_16_17_18 & mask_field_14) >> 12
	field_16 = (field_13_14_15_16_17_18 & mask_field_16) >> 8
	field_17 = (field_13_14_15_16_17_18 & mask_field_17) >> 5
	field_18 = field_13_14_15_16_17_18 & mask_field_18
	field_20 = field_19_20 & mask_field_20
	field_23 = (field_22_23_24_25_26 & mask_field_23) >> 3
	field_25 = (field_22_23_24_25_26 & mask_field_25) >> 1
	field_26 = field_22_23_24_25_26 & mask_field_26
	field_28 = field_27_28 & mask_field_28
	field_29 = (field_29_30 & mask_field_29) >> 10
	field_30 = field_29_30 & mask_field_30
	
	masque_MID_field_14 = 0b1000000000000000000000000000
	masque_MID_field_18 = 0b0111110000000000000000000000
	masque_MID_field_28 = 0b0000001111110000000000000000	
	masque_MID_field_29 = 0b0000000000001111110000000000
	masque_MID_field_30 = 0b0000000000000000001111111111

	MID_field_14 = (field_14 & masque_MID_field_14) >> 27
	MID_field_18 = (field_18 & masque_MID_field_18) >> 22 
	MID_field_28 = (field_28 & masque_MID_field_28) >> 16 
	MID_field_29 = (field_29 & masque_MID_field_29) >> 10  
	MID_field_30 = field_30 & masque_MID_field_30 
	MID = PMID(MID_field_14, MID_field_18, MID_field_28, MID_field_29, MID_field_30)

	field_35 = field_35*(1/2**16)
	field_33_34_35 = field_33_34 + field_35 	

	FT_bench_5 = FT_0(bench_5)
	FT_macdest = FT_MAC(macdest)
	FT_macsrc = FT_MAC(macsrc)
	FT_src_ip = FT_IP(src_ip)
	FT_dest_ip = FT_IP(dest_ip)
	FT_field_14 = FT_7(field_14)
	FT_field_17 = FT_5(field_17)
	FT_field_18 = FT_2(field_18)
	FT_field_28 = FT_3(field_28)
	FT_field_29 = FT_4(field_29)
	FT_field_32 = FT_1(field_32)
	FT_MID = FT_6(MID)

	trame_udp = date2, MID, bench_3, FT_bench_5, framesize, FT_macdest, FT_macsrc, hex(field_1), field_2, field_3, field_4, field_5, field_6, field_7, FT_src_ip, FT_dest_ip, field_8, field_9, field_10, field_11, FT_field_14, field_16, FT_field_17, FT_field_18, field_20, field_21, hex(field_23), hex(field_25), field_26, FT_field_28, FT_field_29, field_30, FT_field_32, field_33_34_35
	return trame_udp




import struct
import datetime
import json
from fonction_decodage import*

def decodage_udp(date2, bench_3, bench_5, framesize, trame, FT):
    
	(macd1, macd2, macd3, macd4, macd5, macd6,
    macs1, macs2, macs3, macs4, macs5, macs6,
    field_1, field_2, field_3, field_4, field_5, field_6, field_7, field_8,
    src_ip1, src_ip2, src_ip3, src_ip4,
    dest_ip1, dest_ip2, dest_ip3, dest_ip4,
    field_9, field_10, field_11, field_12,
    field_13_14_15_16_17_18, field_19_20,
    field_21, field_22_23_24_25_26,
    field_27_28, field_29_30, field_31, field_32,
    field_33_34, field_35, field_36) = struct.unpack_from('>12B5H2BH8B7H2BH2BI2H', trame)

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
	field_23 = hex((field_22_23_24_25_26 & mask_field_23) >> 3)
	field_25 = hex((field_22_23_24_25_26 & mask_field_25) >> 1)
	field_26 = field_22_23_24_25_26 & mask_field_26
	field_28 = field_27_28 & mask_field_28
	field_29 = (field_29_30 & mask_field_29) >> 10
	field_30 = field_29_30 & mask_field_30

	field_35 = field_35*(1/2**16)
	field_33_34_35 = field_33_34 + field_35 	

	date_init_framedate = datetime.datetime(1970, 1, 1, 0, 0, 0)
	framedate = date_init_framedate + datetime.timedelta(0, date2)
	framedate = framedate.strftime("%Y-%m-%d %H:%M:%S")
	date_init_packetdate = datetime.datetime(2000, 1, 1, 12, 0, 0)
	packet_date = date_init_packetdate + datetime.timedelta(0, field_33_34_35)
	packet_date = packet_date.strftime("%Y-%m-%d %H:%M:%S") 
	
	MID_field_14 = format(field_14, '01b')   
	MID_field_18 = format(field_18, '05b')  
	MID_field_28 = format(field_28, '06b')
	MID_field_29 = format(field_29, '06b')
	MID_field_30 = format(field_30, '010b')
	MID = MID_field_14 + MID_field_18 + MID_field_28 + MID_field_29 + MID_field_30    
	PMID = hex(int(MID, 2))    
    
	field_14 = hex(field_14)
	field_18 = hex(field_18)
	field_28 = hex(field_28)
	field_29 = hex(field_29)

	for keys, value in FT['FT_6'].items():
		if PMID == keys:
			PMID = value
   
	for keys, value in FT['FT_0'].items():
		if bench_5 == keys:
			bench_5 = value

	for keys, value in FT['FT_MAC'].items():
		if macdest == keys:
			macdest = value
   
	for keys, value in FT['FT_MAC'].items():
		if macsrc == keys:
			macsrc = value
	
	for keys, value in FT['FT_IP'].items():
		if src_ip == keys:
			src_ip = value
   
	for keys, value in FT['FT_IP'].items():
		if dest_ip == keys:
			dest_ip = value
	
	for keys, value in FT['FT_7'].items():
		if field_14 == keys:
			field_14 = value
    
	for keys, value in FT['FT_5'].items():
		if str(field_17) == keys:
			field_17 = value
           
	for keys, value in FT['FT_2'].items():
		if field_18 == keys:
			field_18 = value
	
	for keys, value in FT['FT_3'].items():
		if field_28 == keys:
			field_28 = value
	
	for keys, value in FT['FT_4'].items():
		if field_29 == keys:
			field_29 = value
   
	for keys, value in FT['FT_1'].items():
		if str(field_32) == keys:
			field_32 = value
   
	return (framedate, PMID, bench_3, bench_5, framesize, macdest, macsrc, 
         field_1, field_2, field_3, field_4, field_5, field_6, field_7, src_ip, 
         dest_ip, field_9, field_10, field_11, field_14, field_16, field_17, field_18, 
         field_20, field_21, field_23, field_25, field_26, field_28, field_29, field_30, 
         field_32, packet_date) 
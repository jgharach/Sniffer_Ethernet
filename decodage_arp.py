import struct
from fonction_decodage import*
def decodage_arp(date2, bench_3, bench_5, framesize, trame):

	macd1, macd2, macd3, macd4, macd5, macd6, macs1, macs2, macs3, macs4, macs5, macs6, field_1, field_2, field_3, field_4, field_5, field_6, mac_sender1, mac_sender2, mac_sender3, mac_sender4, mac_sender5, mac_sender6, sender_ip1, sender_ip2, sender_ip3, sender_ip4, mac_target1, mac_target2, mac_target3, mac_target4, mac_target5, mac_target6, target_ip1, target_ip2, target_ip3, target_ip4 = struct.unpack_from('>BBBBBBBBBBBBHHHBBHBBBBBBBBBBBBBBBBBBBB', trame) 

	macdest = adr_mac(macd1, macd2, macd3, macd4, macd5, macd6)
	macsrc = adr_mac(macs1, macs2, macs3, macs4, macs5, macs6)
	mac_sender = adr_mac(mac_sender1, mac_sender2, mac_sender3, mac_sender4, mac_sender5, mac_sender6)
	sender_ip = adr_ip(sender_ip1, sender_ip2, sender_ip3, sender_ip4)
	mac_target = adr_mac(mac_target1, mac_target2, mac_target3, mac_target4, mac_target5, mac_target6)
	target_ip = adr_ip(target_ip1, target_ip2, target_ip3, target_ip4)

	bench_5 = FT_0(bench_5)
	macdest = FT_MAC(macdest)
	macsrc = FT_MAC(macsrc)
	mac_sender = FT_MAC(mac_sender)
	sender_ip = FT_IP(sender_ip)
	mac_target = FT_MAC(mac_target)
	target_ip = FT_IP(target_ip)

	trame_arp = date2, bench_3, bench_5, framesize, macdest, macsrc, hex(field_1), field_2, field_3, field_4, field_5, field_6, mac_sender, sender_ip, mac_target, target_ip
	return trame_arp

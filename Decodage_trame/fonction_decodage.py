def adr_mac(mac1, mac2, mac3, mac4, mac5, mac6):
        mac1 = hex(mac1)[2:]
        mac2 = hex(mac2)[2:]
        mac3 = hex(mac3)[2:]
        mac4 = hex(mac4)[2:]
        mac5 = hex(mac5)[2:]
        mac6 = hex(mac6)[2:]
        mac = [mac1, mac2, mac3, mac4, mac5, mac6]
        mac = ':'.join(mac)
        return mac

def adr_ip(ip1, ip2, ip3, ip4):
        ip = [str(ip1), str(ip2), str(ip3), str(ip4)]
        ip = '.'.join(ip)
        return ip	
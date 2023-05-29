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

def FTr_0(val, FT):
        for keys, value in FT['FT_0'].items():
                if val == keys:
                        val = value
        return val
        
def FTr_MAC(val, FT):
        for keys, value in FT['FT_MAC'].items():
                if val == keys:
                        val = value
        return val
                        
def FTr_IP(val,FT):
        for keys, value in FT['FT_IP'].items():
                if val == keys:
                        val = value
        return val

                        
def FTr_1(val,FT):
        for keys, value in FT['FT_1'].items():
                if val == keys:
                        val = value
        return val

def FTr_2(val,FT):
        for keys, value in FT['FT_2'].items():
                if val == keys:
                        val = value
        return val


def FTr_3(val,FT):
        for keys, value in FT['FT_3'].items():
                if val == keys:
                        val = value
        return val

def FTr_4(val,FT):
        for keys, value in FT['FT_4'].items():
                if val == keys:
                        val = value
        return val

def FTr_5(val,FT):
        for keys, value in FT['FT_5'].items():
                if val == keys:
                        val = value
        return val

def FTr_6(val,FT):
        for keys, value in FT['FT_6'].items():
                if val == keys:
                       val = value
        return val

def FTr_7(val,FT):
        for keys, value in FT['FT_7'].items():
                if val == keys:
                        val = value
        return val
def adr_mac(mac1, mac2, mac3, mac4, mac5, mac6):
        """La fonction adr_mac prend en entrée 6 entiers et 
        les renvoie sous la forme d'une adresse MAC"""
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
        """ La fonction adr_ip prend en entrée 4 entiers et 
        les renvoie sous la forme d'une adresse IP"""
        ip = [str(ip1), str(ip2), str(ip3), str(ip4)]
        ip = '.'.join(ip)
        return ip

def FTr_0(val, FT):
        """La fonction FTr_0 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 0 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_0'].items():
                if val == keys:
                        val = value
        return val
        
def FTr_MAC(val, FT):
        """La fonction FTr_MAC prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert MAC sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_MAC'].items():
                if val == keys:
                        val = value
        return val
                        
def FTr_IP(val,FT):
        """La fonction FTr_IP prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert IP sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_IP'].items():
                if val == keys:
                        val = value
        return val

                        
def FTr_1(val,FT):
        """La fonction FTr_1 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 1 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_1'].items():
                if val == keys:
                        val = value
        return val

def FTr_2(val,FT):
        """La fonction FTr_2 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 2 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_2'].items():
                if val == keys:
                        val = value
        return val


def FTr_3(val,FT):
        """La fonction FTr_3 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 3 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_3'].items():
                if val == keys:
                        val = value
        return val

def FTr_4(val,FT):
        """La fonction FTr_4 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 4 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_4'].items():
                if val == keys:
                        val = value
        return val

def FTr_5(val,FT):
        """La fonction FTr_5 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 5 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_5'].items():
                if val == keys:
                        val = value
        return val

def FTr_6(val,FT):
        """La fonction FTr_6 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 6 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_6'].items():
                if val == keys:
                       val = value
        return val

def FTr_7(val,FT):
        """La fonction FTr_7 prend en entrée une valeur, un dictionnaire comportant les fonctions transfert
        puis applique la fonction transfert 7 sur cette valeur et renvoie cette valeur transformée"""
        for keys, value in FT['FT_7'].items():
                if val == keys:
                        val = value
        return val

def extraction(fic):
        """La fonction extraction prend en entrée le fichier de configuration du test en extrayant 
        les informations nécéssaires du test qui permet son identification et renvoie l'obsw, la version du bds,
        le type et version moyen, la date d'exécution et le nom du test"""
        f = open(fic, "r")       
        infos_extrait = f.readlines()
        obsw = infos_extrait[7].rstrip().split(':')[1]
        version_obsw = infos_extrait[8].rstrip().split(':')[1]
        obsw = obsw + "" + version_obsw
        version_bds = infos_extrait[9].rstrip().split(':')[1]
        type_et_ver_moyen = infos_extrait[10].rstrip().split(':')[1]
        date_execution = eval(infos_extrait[14].rstrip().split(':')[1])
        nom_test = infos_extrait[27].rstrip().split(':')[1]
        f.close()
        return obsw, version_bds, type_et_ver_moyen, date_execution, nom_test
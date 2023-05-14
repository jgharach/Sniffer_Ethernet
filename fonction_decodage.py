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

def PMID(MID_14, MID_18, MID_28, MID_29, MID_30):
        MID = [hex(MID_14), hex(MID_18)[2:], hex(MID_28)[2:], hex(MID_29)[2:], hex(MID_30)[2:]]
        MID = ''.join(MID)
        return MID

def FT_0(bench_5):
	if hex(bench_5) == "0x0":
		return 'FT_0_label_0'
	elif hex(bench_5) == "0x1": 
		return 'FT_0_label_1'
	else:
		return bench_5

def FT_MAC(mac):
	if mac == '0:10:ec:01:e5:41':
		return 'ordi_1'
	elif mac == '0:10:ec:1:e5:43':
		return 'ordi_2'
	elif mac == '0:10:ec:01:e5:44':
		return 'ordi_3'
	elif mac == '0:1f:29:57:94:f2':
		return 'ordi_4'
	elif mac == '0:1f:29:57:94:f3':
		return 'ordi_5'
	elif mac == 'b4:7a:f1:e3:41:6b':
		return 'ordi_6'
	else:
		return mac

def FT_IP(ip):
	if ip == '169.254.173.5':
		return 'ordi_1'
	elif ip == '169.254.173.224':
		return 'ordi_2'
	elif ip == '169.254.174.5':
		return 'ordi_3'
	elif ip == '169.254.174.223':
		return 'ordi_4'
	elif ip == '169.254.175.5':
		return 'ordi_5'
	elif ip == '169.254.175.222':
		return 'ordi_6'
	else:
		return ip

def FT_1(field_32):
	if field_32 == 1:
		return 'FT_1_label_1'
	elif field_32 == 2:
		return 'FT_1_label_2'
	elif field_32 == 3:
		return 'FT_1_label_3'
	elif field_32 == 17:
		return 'FT_1_label_17'
	elif field_32 == 192:        
		return 'FT_1_label_192'
	elif field_32 == 208:
		return 'FT_1_label_208'
	else:
		return field_32

def FT_2(field_18):
	if hex(field_18) == '0x0':
		return 'FT_2_label_1'
	elif hex(field_18) == '0x1':
		return 'FT_2_label_2'
	else:
		return field_18

def FT_3(field_28):
	if hex(field_28) == '0x0':
		return 'FT_3_label_1'
	elif hex(field_28) == '0x1':
		return 'FT_3_label_2'
	elif hex(field_28) == '0x2':
		return 'FT_3_label_3'
	elif hex(field_28) == '0x3':
		return 'FT_3_label_4'
	elif hex(field_28) == '0x4': 
		return 'FT_3_label_5'
	else:
		return field_28

def FT_4(field_29):
	if hex(field_29) == '0x0':
                return 'FT_4_label_1'
	elif hex(field_29) == '0x1':
                return 'FT_4_label_2'
	elif hex(field_29) == '0x2':
                return 'FT_4_label_3'
	elif hex(field_29) == '0x3':
                return 'FT_4_label_4'
	elif hex(field_29) == '0x4':
                return 'FT_4_label_5'
	elif hex(field_29) == '0x5':
                return 'FT_4_label_6'
	elif hex(field_29) == '0x6':
                return 'FT_4_label_7'
	elif hex(field_29) == '0x7':
                return 'FT_4_label_8'
	elif hex(field_29) == '0x8':
                return 'FT_4_label_9'
	elif hex(field_29) == '0x9':
		return 'FT_4_label_10'
	elif hex(field_29) == '0xa':
                return 'FT_4_label_11'
	elif hex(field_29) == '0xb':
                return 'FT_4_label_12'
	elif hex(field_29) == '0xc':
                return 'FT_4_label_13'
	elif hex(field_29) == '0xd':
                return 'FT_4_label_14'
	elif hex(field_29) == '0xe':
                return 'FT_4_label_15'
	elif hex(field_29) == '0xf':
		return 'FT_4_label_16'
	else:
		return field_29
	
def FT_5(field_17):
	if field_17 == 0:
		return 'FT_5_label_1'	
	elif field_17 == 1:
                return 'FT_5_label_2'
	elif field_17 == 2:
                return 'FT_5_label_3'
	elif field_17 == 3:
                return 'FT_5_label_4'
	elif field_17 == 4:
                return 'FT_5_label_5'
	elif field_17 == 5:
                return 'FT_5_label_6'
	elif field_17 == 6:
                return 'FT_5_label_7'
	elif field_17 == 7:
                return 'FT_5_label_8'
	else:
		return field_17

def FT_7(field_14):
        if hex(field_14) == '0x0':
                return 'FT_7_label_1'
       	elif hex(field_14) == '0x1':
                return 'FT_7_label_2'
        else:
	        return field_14

def FT_6(MID):
	if MID == '0x33c01':
		return 'FT_6_MID_1'
	elif MID == '0x33c02':
                return 'FT_6_MID_2'
	elif MID == '0x33c03':
                return 'FT_6_MID_3'
	elif MID == '0x33c04':
                return 'FT_6_MID_4'
	elif MID == '0x33c05':
                return 'FT_6_MID_5'
	elif MID == '0x33c06':
                return 'FT_6_MID_6'
	elif MID == '0xc33C07':
                return 'FT_6_MID_7'
	elif MID == '0x33c08':
                return 'FT_6_MID_8'
	elif MID == '0x33c09':
                return 'FT_6_MID_9'
	elif MID == '0x33c0a':
                return 'FT_6_MID_10'
	elif MID == '0x33c0b':
                return 'FT_6_MID_11'
	elif MID == '0x33c0c':
                return 'FT_6_MID_12'
	elif MID == '0x33c0d':
                return 'FT_6_MID_13'
	elif MID == '0x33c0e':
                return 'FT_6_MID_14'
	elif MID == '0x33cf':
                return 'FT_6_MID_15'
	elif MID == '0x33c10':
                return 'FT_6_MID_16'
	elif MID == '0x33c11':
                return 'FT_6_MID_17'
	elif MID == '0x33c12':
                return 'FT_6_MID_18'
	elif MID == '0x33c13':
                return 'FT_6_MID_19'
	elif MID == '0x33c14':
                return 'FT_6_MID_20'
	elif MID == '0x33c15':
                return 'FT_6_MID_21'
	elif MID == '0x33c16':
                return 'FT_6_MID_22'
	elif MID == '0x33c17':
                return 'FT_6_MID_23'
	elif MID == '0x33c18':
                return 'FT_6_MID_24'
	elif MID == '0x33c19':
                return 'FT_6_MID_25'
	elif MID == '0x33c1a':
                return 'FT_6_MID_26'
	elif MID == '0x33c1b':
                return 'FT_6_MID_27'
	elif MID == '0x33c1c':
                return 'FT_6_MID_28'
	elif MID == '0x33c1d':
                return 'FT_6_MID_29'
	elif MID == '0x33c1e':
                return 'FT_6_MID_30'
	elif MID == '0x33c1f':
                return 'FT_6_MID_31'
	elif MID == '0x33c20':
                return 'FT_6_MID_32'
	elif MID == '0x33c21':
                return 'FT_6_MID_33'
	elif MID == '0x33c22':
                return 'FT_6_MID_34'
	elif MID == '0x33c23':
                return 'FT_6_MID_35'
	elif MID == '0x33c24':
                return 'FT_6_MID_36'
	elif MID == '0x33c25':
                return 'FT_6_MID_37'
	elif MID == '0x33c26':
                return 'FT_6_MID_38'
	elif MID == '0x33c27':
                return 'FT_6_MID_39'
	elif MID == '0x33c28':
                return 'FT_6_MID_40'
	elif MID == '0x33c29':
                return 'FT_6_MID_41'
	elif MID == '0x33c2a':
                return 'FT_6_MID_42'
	elif MID == '0x33c2b':
                return 'FT_6_MID_43'
	elif MID == '0x33c41':
                return 'FT_6_MID_44'
	elif MID == '0x33c42':
                return 'FT_6_MID_45'
	elif MID == '0x33c43':
                return 'FT_6_MID_46'
	elif MID == '0x33c44':
                return 'FT_6_MID_47'
	elif MID == '0x33c45':
                return 'FT_6_MID_48'
	elif MID == '0x33c46':
                return 'FT_6_MID_49'
	elif MID == '0x33c47':
                return 'FT_6_MID_50'
	elif MID == '0x33c61':
                return 'FT_6_MID_51'
	elif MID == '0x33c62':
                return 'FT_6_MID_52'
	elif MID == '0x33c63':
                return 'FT_6_MID_53'
	elif MID == '0x33c64':
                return 'FT_6_MID_54'
	elif MID == '0x33c65':
                return 'FT_6_MID_55'
	elif MID == '0x33c66':
                return 'FT_6_MID_56'
	elif MID == '0x33c67':
                return 'FT_6_MID_57'
	elif MID == '0x33c68':
                return 'FT_6_MID_58'
	elif MID == '0x33c69':
                return 'FT_6_MID_59'
	elif MID == '0x33d08':
                return 'FT_6_MID_60'
	elif MID == '0x33d10':
                return 'FT_6_MID_61'
	elif MID == '0x33d11':
                return 'FT_6_MID_62'
	elif MID == '0x33d18':
                return 'FT_6_MID_63'
	elif MID == '0x33d60':
                return 'FT_6_MID_64'
	elif MID == '0x33dc0':
                return 'FT_6_MID_65'
	elif MID == '0x33dc8':
                return 'FT_6_MID_66'
	elif MID == '0x33dc9':
                return 'FT_6_MID_67'
	elif MID == '0x34c01':
                return 'FT_6_MID_68'
	elif MID == '0x34c02':
                return 'FT_6_MID_69'
	elif MID == '0x34c03':
                return 'FT_6_MID_70'
	elif MID == '0x34c04':
                return 'FT_6_MID_71'
	elif MID == '0x34c05':
                return 'FT_6_MID_72'
	elif MID == '0x34c06':
                return 'FT_6_MID_73'
	elif MID == '0x34c07':
                return 'FT_6_MID_74'
	elif MID == '0x34c08':
                return 'FT_6_MID_75'
	elif MID == '0x34c09':
                return 'FT_6_MID_76'
	elif MID == '0x34c0a':
                return 'FT_6_MID_77'
	elif MID == '0x34c0b':
                return 'FT_6_MID_78'
	elif MID == '0x34c0c':
                return 'FT_6_MID_79'
	elif MID == '0x34c0d':
                return 'FT_6_MID_80'
	elif MID == '0x34c0e':
                return 'FT_6_MID_81'
	elif MID == '0x34C0F':
                return 'FT_6_MID_82'
	elif MID == '0x34c10':
                return 'FT_6_MID_83'
	elif MID == '0x34c11':
                return 'FT_6_MID_84'
	elif MID == '0x34c12':
                return 'FT_6_MID_85'
	elif MID == '0x34c13':
                return 'FT_6_MID_86'
	elif MID == '0x34c14':
                return 'FT_6_MID_87'
	elif MID == '0x34c15':
                return 'FT_6_MID_88'
	elif MID == '0x34c16':
                return 'FT_6_MID_89'
	elif MID == '0x34c17':
                return 'FT_6_MID_90'
	elif MID == '0x34c18':
                return 'FT_6_MID_91'
	elif MID == '0x34c19':
                return 'FT_6_MID_92'
	elif MID == '0x34c1a':
                return 'FT_6_MID_93'
	elif MID == '0x34c1b':
                return 'FT_6_MID_94'
	elif MID == '0x34c1c':
                return 'FT_6_MID_95'
	elif MID == '0x34c1d':
                return 'FT_6_MID_96'
	elif MID == '0x34c1e':
                return 'FT_6_MID_97'
	elif MID == '0x34c1f':
                return 'FT_6_MID_98'
	elif MID == '0x34c21':
		return 'FT_6_MID_99'
	elif MID == '0x34c22':
                return 'FT_6_MID_100'
	elif MID == '0x34c23':
                return 'FT_6_MID_101'
	elif MID == '0x34c24':
                return 'FT_6_MID_102'
	elif MID == '0x34c25':
                return 'FT_6_MID_103'
	elif MID == '0x34c26':
                return 'FT_6_MID_104'
	elif MID == '0x34c27':
                return 'FT_6_MID_105'
	elif MID == '0x34c28':
                return 'FT_6_MID_106'
	elif MID == '0x34c29':
                return 'FT_6_MID_107'
	elif MID == '0x34c2A':
                return 'FT_6_MID_108'
	elif MID == '0x34c41':
                return 'FT_6_MID_109'
	elif MID == '0x34c43':
                return 'FT_6_MID_110'
	elif MID == '0x34c44':
                return 'FT_6_MID_111'
	elif MID == '0x34c45':
                return 'FT_6_MID_112'
	elif MID == '0x34c46':
                return 'FT_6_MID_113'
	elif MID == '0x34c47':
                return 'FT_6_MID_114'
	elif MID == '0x34c61':
                return 'FT_6_MID_115'
	elif MID == '0x34c62':
                return 'FT_6_MID_116'
	elif MID == '0x34c63':
                return 'FT_6_MID_117'
	elif MID == '0x34c64':
                return 'FT_6_MID_118'
	elif MID == '0x34c65':
                return 'FT_6_MID_119'
	elif MID == '0x34c66':
                return 'FT_6_MID_120'
	elif MID == '0x34c67':
                return 'FT_6_MID_121'
	elif MID == '0x34c68':
                return 'FT_6_MID_122'
	elif MID == '0x34c69':
                return 'FT_6_MID_123'
	elif MID == '0x34d08':
                return 'FT_6_MID_124'
	elif MID == '0x34d18':
                return 'FT_6_MID_125'
	elif MID == '0x34d60':
                return 'FT_6_MID_126'
	elif MID == '0x34dc0':
                return 'FT_6_MID_127'
	elif MID == '0x8033c01':
                return 'FT_6_MID_128'
	elif MID == '0x8033c02':
                return 'FT_6_MID_129'
	elif MID == '0x8033c03':
                return 'FT_6_MID_130'
	elif MID == '0x8033c04':
                return 'FT_6_MID_131'
	elif MID == '0x8033c05':
                return 'FT_6_MID_132'
	elif MID == '0x8033c06':
                return 'FT_6_MID_133'
	elif MID == '0x8033c07':
                return 'FT_6_MID_134'
	elif MID == '0x8033c08':
                return 'FT_6_MID_135'
	elif MID == '0x8033c09':
                return 'FT_6_MID_136'
	elif MID == '0x8033c0a':
                return 'FT_6_MID_137'
	elif MID == '0x8033c0b':
                return 'FT_6_MID_138'
	elif MID == '0x8033c0c':
                return 'FT_6_MID_139'
	elif MID == '0x8033c0d':
                return 'FT_6_MID_140'
	elif MID == '0x8033c0e':
                return 'FT_6_MID_141'
	elif MID == '0x8033c0f':
                return 'FT_6_MID_142'
	elif MID == '0x8033c10':
                return 'FT_6_MID_143'
	elif MID == '0x8033c11':
                return 'FT_6_MID_144'
	elif MID == '0x8033c12':
                return 'FT_6_MID_145'
	elif MID == '0x8033c13':
                return 'FT_6_MID_146'
	elif MID == '0x8033c14':
                return 'FT_6_MID_147'
	elif MID == '0x8033c15':
                return 'FT_6_MID_148'
	elif MID == '0x8033c16':
                return 'FT_6_MID_149'
	elif MID == '0x8033c17':
                return 'FT_6_MID_150'
	elif MID == '0x8033c18':
                return 'FT_6_MID_151'
	elif MID == '0x8033c19':
                return 'FT_6_MID_152'
	elif MID == '0x8033c1a':
                return 'FT_6_MID_153'
	elif MID == '0x8033c1b':
                return 'FT_6_MID_154'
	elif MID == '0x8033c1c':
                return 'FT_6_MID_155'
	elif MID == '0x8033c1d':
                return 'FT_6_MID_156'
	elif MID == '0x8033c1e':
                return 'FT_6_MID_157'
	elif MID == '0x8033c21':
                return 'FT_6_MID_158'
	elif MID == '0x8033c22':
                return 'FT_6_MID_159'
	elif MID == '0x8033c23':
                return 'FT_6_MID_160'
	elif MID == '0x8033c24':
                return 'FT_6_MID_161'
	elif MID == '0x8033c25':
                return 'FT_6_MID_162'
	elif MID == '0x8033c26':
                return 'FT_6_MID_163'
	elif MID == '0x8033c27':
                return 'FT_6_MID_164'
	elif MID == '0x8033c28':
                return 'FT_6_MID_165'
	elif MID == '0x8033c29':
                return 'FT_6_MID_166'
	elif MID == '0x8033c2A':
                return 'FT_6_MID_167'
	elif MID == '0x8033c2B':
                return 'FT_6_MID_168'
	elif MID == '0x8033c2c':
                return 'FT_6_MID_169'
	elif MID == '0x8033c2d':
                return 'FT_6_MID_170'
	elif MID == '0x8033c2e':
                return 'FT_6_MID_171'
	elif MID == '0x8033c2f':
                return 'FT_6_MID_172'
	elif MID == '0x8033c41':
                return 'FT_6_MID_173'
	elif MID == '0x8033c42':
                return 'FT_6_MID_174'
	elif MID == '0x8033c43':
                return 'FT_6_MID_175'
	elif MID == '0x8033c46':
                return 'FT_6_MID_176'
	elif MID == '0x8033c47':
                return 'FT_6_MID_177'
	elif MID == '0x8033c48':
                return 'FT_6_MID_178'
	elif MID == '0x8033c49':
                return 'FT_6_MID_179'
	elif MID == '0x8033c4a':
                return 'FT_6_MID_180'
	elif MID == '0x8033c61':
                return 'FT_6_MID_181'
	elif MID == '0x8033c62':
                return 'FT_6_MID_182'
	elif MID == '0x8033c63':
                return 'FT_6_MID_183'
	elif MID == '0x8033c64':
                return 'FT_6_MID_184'
	elif MID == '0x8033c65':
                return 'FT_6_MID_185'
	elif MID == '0x8033c66':
                return 'FT_6_MID_186'
	elif MID == '0x8033d08':
                return 'FT_6_MID_187'
	elif MID == '0x8033d09':
                return 'FT_6_MID_188'
	elif MID == '0x8033d18':
                return 'FT_6_MID_189'
	elif MID == '0x8033d19':
                return 'FT_6_MID_190'
	elif MID == '0x8033d60':
                return 'FT_6_MID_191'
	elif MID == '0x8033d61':
                return 'FT_6_MID_192'
	elif MID == '0x8033d62':
                return 'FT_6_MID_193'
	elif MID == '0x8033dc0':
                return 'FT_6_MID_194'
	elif MID == '0x8033dc1':
                return 'FT_6_MID_195'
	elif MID == '0x8033dc8':
                return 'FT_6_MID_196'
	elif MID == '0x8034c01':
		return 'FT_6_MID_197'
	elif MID == '0x8034c02':
                return 'FT_6_MID_198'
	elif MID == '0x8034c03':
                return 'FT_6_MID_199'
	elif MID == '0x8034c04':
                return 'FT_6_MID_200'
	elif MID == '0x8034c05':
                return 'FT_6_MID_201'
	elif MID == '0x8034c06':
                return 'FT_6_MID_202'
	elif MID == '0x8034c07':
                return 'FT_6_MID_203'
	elif MID == '0x8034c08':
                return 'FT_6_MID_204'
	elif MID == '0x8034c09':
                return 'FT_6_MID_205'
	elif MID == '0x8034c0a':
                return 'FT_6_MID_206'
	elif MID == '0x8034c0b':
                return 'FT_6_MID_207'
	elif MID == '0x8034c0c':
                return 'FT_6_MID_208'
	elif MID == '0x8034c0d':
                return 'FT_6_MID_209'
	elif MID == '0x8034c0e':
                return 'FT_6_MID_210'
	elif MID == '0x8034c0f':
                return 'FT_6_MID_211'
	elif MID == '0x8034c10':
                return 'FT_6_MID_212'
	elif MID == '0x8034c11':
                return 'FT_6_MID_213'
	elif MID == '0x8034c12':
                return 'FT_6_MID_214'
	elif MID == '0x8034c13':
                return 'FT_6_MID_215'
	elif MID == '0x8034c14':
                return 'FT_6_MID_216'
	elif MID == '0x8034c15':
                return 'FT_6_MID_217'
	elif MID == '0x8034c16':
                return 'FT_6_MID_218'
	elif MID == '0x8034c17':
                return 'FT_6_MID_219'
	elif MID == '0x8034c18':
                return 'FT_6_MID_220'
	elif MID == '0x8034c19':
                return 'FT_6_MID_221'
	elif MID == '0x8034c1a':
                return 'FT_6_MID_222'
	elif MID == '0x8034c1b':
                return 'FT_6_MID_223'
	elif MID == '0x8034c1c':
                return 'FT_6_MID_224'
	elif MID == '0x8034c1d':
                return 'FT_6_MID_225'
	elif MID == '0x8034c1e':
                return 'FT_6_MID_226'
	elif MID == '0x8034c21':
                return 'FT_6_MID_227'
	elif MID == '0x8034c22':
                return 'FT_6_MID_228'
	elif MID == '0x8034c23':
                return 'FT_6_MID_229'
	elif MID == '0x8034c24':
                return 'FT_6_MID_230'
	elif MID == '0x8034c25':
                return 'FT_6_MID_231'
	elif MID == '0x8034c26':
                return 'FT_6_MID_232'
	elif MID == '0x8034c27':
                return 'FT_6_MID_233'
	elif MID == '0x8034c28':
                return 'FT_6_MID_234'
	elif MID == '0x8034c29':
                return 'FT_6_MID_235'
	elif MID == '0x8034c2a':
                return 'FT_6_MID_236'
	elif MID == '0x8034c2b':
                return 'FT_6_MID_237'
	elif MID == '0x8034c2c':
                return 'FT_6_MID_238'
	elif MID == '0x8034c2d':
                return 'FT_6_MID_239'
	elif MID == '0x8034c2e':
                return 'FT_6_MID_240'
	elif MID == '0x8034c2f':
                return 'FT_6_MID_241'
	elif MID == '0x8034c41':
                return 'FT_6_MID_242'
	elif MID == '0x8034c42':
                return 'FT_6_MID_243'
	elif MID == '0x8034c43':
                return 'FT_6_MID_244'
	elif MID == '0x8034c46':
                return 'FT_6_MID_245'
	elif MID == '0x8034c47':
                return 'FT_6_MID_246'
	elif MID == '0x8034c48':
                return 'FT_6_MID_247'
	elif MID == '0x8034c49':
                return 'FT_6_MID_248'
	elif MID == '0x8034c4a':
                return 'FT_6_MID_249'
	elif MID == '0x8034c61':
                return 'FT_6_MID_250'
	elif MID == '0x8034c62':
                return 'FT_6_MID_251'
	elif MID == '0x8034c63':
                return 'FT_6_MID_252'
	elif MID == '0x8034c64':
                return 'FT_6_MID_253'
	elif MID == '0x8034c65':
                return 'FT_6_MID_254'
	elif MID == '0x8034c66':
                return 'FT_6_MID_255'
	elif MID == '0x8034d08':
                return 'FT_6_MID_256'
	elif MID == '0x8034d09':
                return 'FT_6_MID_258'
	elif MID == '0x8034d18':
                return 'FT_6_MID_259'
	elif MID == '0x8034d19':
                return 'FT_6_MID_260'
	elif MID == '0x8034d60':
                return 'FT_6_MID_261'
	elif MID == '0x8034d61':
                return 'FT_6_MID_262'
	elif MID == '0x8034d62':
                return 'FT_6_MID_263'
	elif MID == '0x8034dc0':
                return 'FT_6_MID_264'
	elif MID == '0x8034dc1':
                return 'FT_6_MID_265'
	else:
		return MID


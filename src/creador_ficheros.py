import csv
from operator import itemgetter
import os

class creador_ficheros():
    def __init__(self):
        pass

    def get_files(files):
        zynq_nam = list()
        for file in files:
            if file[-4:] == '.csv':
                zynq_nam.append(file)
        return zynq_nam

    def get_name(file):
        name = ""
        flag = 0
        cont = 0
        for i in file[:-7]:
            if i.isnumeric():
                flag = 1
                cont = 0
            if flag == 1:
                cont += 1
            name += i
            if cont == 3:
                name += "-"
        return name

    def get_pins(zynq_name):
        cont=0
        pin_name = []
        pin_num = []
        pin_bank = []

        path = './chips/zupall/'+zynq_name
        with open(path) as csvarchive:
            entrada = csv.reader(csvarchive)
            lista=[]
            for reg in entrada:
                lista.append(reg)
            
        for string in lista:
            cont += 1
            if "Pin" in string:
                break
        lista = lista[cont+1:-2]
        lista=sorted(lista, key=itemgetter(3))

        pines = []
        for pin in lista:
            pin_name = pin[1]
            pin_num = pin[0]
            pin_bank = pin[3]
            pines.append([pin_num, pin_name, pin_bank])

        return pines


    def listado(pines):
        pin_bank_ant = ""
        new_bank = 0
        pin_bank = []
        cont = -1
        pines = sorted(pines, key=itemgetter(2))

        for pin in pines:
            if pin[1][-len(pin[2]):] == pin[2]:
                pin[1] = pin[1][:-(len(pin[2])+1)]

            if pin[2] != pin_bank_ant:
                new_bank = 1
                cont += 1
            if new_bank == 1:
                pin_bank.append([pin])
                new_bank = 0
            else:
                pin_bank[cont].append(pin)
            pin_bank_ant = pin[2]

        bank_gnd = []
        bank_mgtav = []
        bank_ngnd = []
        bank_ps_mgt = []
        bank_vcc = []
        bank_nc  =[]
        pin_bank2 = []
        for na in pin_bank:
            if na[0][2] == "NA":
                for na2 in na:
                    if na2[1][:3] == "GND":
                        bank_gnd.append(na2)
                    elif na2[1][:5] == "MGTAV":
                        bank_mgtav.append(na2)
                    elif na2[1][:6] == "PS_MGT":
                        bank_ps_mgt.append(na2)
                    elif na2[1][:3] == "VCC":
                        bank_vcc.append(na2)
                    elif na2[1][:2] == "NC":
                        bank_nc.append(na2)
                    else:
                        bank_ngnd.append(na2)
                if bank_vcc:
                    pin_bank2.append(bank_vcc)
                if bank_gnd:
                    pin_bank2.append(bank_gnd)
                if bank_mgtav:
                    pin_bank2.append(bank_mgtav)
                if bank_ngnd:
                    pin_bank2.append(bank_ngnd)
                if bank_nc:
                    pin_bank2.append(bank_nc)
            else:
                pin_bank2.append(na)
        
        pin_bank3 = []
        pin_gnd = []
        for i in pin_bank2:
            if i[0][1][:3] == "GND":
                if len(i) > 100:
                    for t in i:
                        pin_gnd.append(t)
                        if len(pin_gnd) == 100:
                            pin_bank3.append(pin_gnd)
                            pin_gnd=[]
                    if pin_gnd:
                        pin_bank3.append(pin_gnd)
            else:
                pin_bank3.append(i)
        
        return pin_bank3




    def generador(pins, name):
        wr = ""
        cont = 0

        for pin in pins:
            cont += 1
            wr += "\n\t\t(symbol \"" + name + "_" + str(cont) + "_1\""
            # agregar rectangulo
            wr += create_square(pin)

            # agregar pines
            wr += create_pin(pin)


            wr += "\n\t\t)"

        return wr




    bidirec=["PS_MIO", "IO_", "PS_DDR_DQS_N", "PS_DDR_DQS_P", "DONE", "INIT_B", "PS_DDR_DQ", "T0_DQS", "T1_DQS", "T2_DQS", "T3_DQS"]
    power=["VCC", "PS_MIO_V", "GND", "PS_DDR_VREF", "VREF"]
    output=["TDO", "PS_DDR_CKP", "PS_DDR_CKN", "PS_DDR_CKE", "PS_DDR_CS_B", "PS_DDR_RAS_B", "PS_DDR_CAS_B", "PS_DDR_WE_B", "PS_DDR_BA", "PS_DDR_A", "PS_DDR_ODT", "PS_DDR_DRST_B", "PS_DDR_DM", "PS_DDR_VRP", "PS_DDR_VRN", \
        "MGTXTXP", "MGTPTXP", "MGTXTXN", "MGTPTXN",]

    def create_pin(pin_list):
        """
        crear pines
        """
        mitad = 0
        cont = 0
        wr = ""
        lon = len(pin_list)
        if lon > 20:
            mitad = 1

        for pin in pin_list:
            tipo = "input"
            name = pin[1]
            number = pin[0]
            wr += "\n\t\t\t(pin " 
            #tipo de pin
            for b in bidirec:
                if pin[1].find(b) != -1: #   [:len(b)] == b:
                    tipo = "bidirectional"
            for p in power:
                if pin[1].find(p) != -1: #[:len(p)] == p:
                    tipo = "power_in"
            for o in output:
                if pin[1].find(o) != -1: #[:len(o)] == o:
                    tipo = "output"
            if pin[1] == "NC":
                tipo = "no_connect"
            wr += tipo 
            #posicion
            if mitad == 1:
                if cont <= lon/2:
                    pos_y = (int(lon/4) - int(cont))*1.27*2
                else:
                    pos_y = (int(lon/4) - int(cont-lon/2))*1.27*2
            else:
                pos_y = (int(lon/2) - int(cont))*1.27*2

            cont += 1
            if mitad == 1:
                if cont <= lon:
                    dir = 180
                else:
                    dir = 0
            else:
                dir = 180
            wr += " line"
            wr += "\n\t\t\t\t(at " + str(10+1.27*4) + " " + str(pos_y) + " " + str(dir) + ")"
            wr += "\n\t\t\t\t(length " +  str(1.27*4) +")\n"
            #nombre
            wr += "\n\t\t\t\t(name \"" + name + "\""
            wr += "\n\t\t\t\t\t(effects"
            wr += "\n\t\t\t\t\t\t(font"
            wr += "\n\t\t\t\t\t\t\t(size 1.27 1.27)"
            wr += "\n\t\t\t\t\t\t)"
            wr += "\n\t\t\t\t\t)"
            wr += "\n\t\t\t\t)"
            #numero
            wr += "\n\t\t\t\t(number \"" + number + "\""
            wr += "\n\t\t\t\t\t(effects"
            wr += "\n\t\t\t\t\t\t(font"
            wr += "\n\t\t\t\t\t\t\t(size 1.27 1.27)"
            wr += "\n\t\t\t\t\t\t)"
            wr += "\n\t\t\t\t\t)"
            wr += "\n\t\t\t\t)"
            wr += "\n\t\t\t)"
        return wr

    def create_square(pin):
        """
        crear rectangulo
        """
        max = 0

        # calculo del rectangulo
        #dimensiones
        for l in pin:
            rt = len(l[1])
            if rt > max:
                max = rt

        if max < 19:
            x = 10       # check this numbers
        else:
            x = max    #check this numbers
        

        #calculo de la otra mitad, para añadir el otro lado
        lon = int(len(pin)/2)   # encima/debajo cero
        mitad = 0

        if lon >= 75:
            mitad = 1

        if mitad == 1:  #izda/dcha
            h = int(lon/2)*100+200
        else:
            h = 20

        # agregar rectangulo
        p1_pos = (x, h)
        if mitad == 1:
            p2_pos = (-x, -h)
        else:
            p2_pos = (0, -h)

        wr = "\n\t\t\t(rectangle"
        wr += "\n\t\t\t\t(start " + str(p1_pos[0]) + " " + str(p1_pos[1]) + ")"
        wr += "\n\t\t\t\t(end " + str(p2_pos[0]) + " " + str(p2_pos[1]) + ")"
        wr += "\n\t\t\t\t(stroke"
        wr += "\n\t\t\t\t\t(width 0)"
        wr += "\n\t\t\t\t\t(type default)"
        wr += "\n\t\t\t\t)"
        wr += "\n\t\t\t\t(fill"
        wr += "\n\t\t\t\t\t(type none)"
        wr += "\n\t\t\t\t)"
        wr += "\n\t\t\t)"

        return wr

    # def create_text(text):
    #     pos = (a,b)

    #     wr = "(text \""+ text + "\" (at " + pos[0] + " " + pos[1] + " 0)\n\
    #                 (effects (font (size 1.27 1.27)))\n      )"
        
    #     return wr

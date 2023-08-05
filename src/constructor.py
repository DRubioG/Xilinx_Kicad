import csv
from operator import itemgetter
import os

def get_files(files):
    zynq = []
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
    # return lista, capas

def generador_pines(pins):
    

    for pin in pins:
        lon = int(len(pin)/2)
        mitad = 0
        max = 0

        if lon >= 75:
            mitad = 1

        for l in pin:
            rt = len(l[1])
            if rt > max:
                max = rt

        if max < 19:
            x = 650 -200      # check this numbers
        else:
            x = 1000    #check this numbers
        
        if mitad == 1:
            u = int(lon/2)*100+200
        else:
            u = lon*100+200
        

        # agregar rectangulo
        wr += create_square((str(x), str(u)), (str(-x), str(-u)))

        # agregar pines
        for i in pin:

            wr += create_pin(i)


    pass

def create_pin(name, number, bank):
    wr = "\t\t\t(pin " 
    #tipo de pin
    wr += tipo 
    #posicion
    wr += " line (at " + pos_x + " " + pos_y + " " + dir + ") (length 2.54)"
    #nombre
    wr += "\t\t\t\t(name \"" + name + "\" (effects (font (size 1.27 1.27))))\n"
    #numero
    wr += "\t\t\t\t(name \"" + number + "\" (effects (font (size 1.27 1.27))))\n"
    wr += "\t\t\t)\n"
    return wr

def create_square(p1_pos, p2_pos):

    wr = "\t\t\t(rectangle (start " + p1_pos[0] + " " + p1_pos[1] + ") \
        (end " + p2_pos[0] + " " + p2_pos[1] + ")\n\
            \t\t\t\t(stroke (width 0) (type default))\n\
            \t\t\t\t(fill (type none))\n\t\t\t)\n"

    return wr

def create_text(text):
    pos = (a,b)

    wr = "(text \""+ text + "\" (at " + pos[0] + " " + pos[1] + " 0)\n\
        \t\t\t\t(effects (font (size 1.27 1.27)))\n\t\t\t)"
    
    return wr

if __name__=="__main__":
    files = os.listdir('./chips/zupall/')

    zynq_nam = get_files(files)

    f = open("Zynq_Ultrascale+.kicad_sym", "w")

    wr = "(kicad_symbol_lib (version 20220914) (generator kicad_symbol_editor)\n"

    for chip in zynq_nam:
        name = get_name(chip)

        pines = get_pins(chip)

        lista = listado(pines)
        

        wr += "\t(symbol \"" + name + "\" (in_bom yes) (on_board yes)  \
\t\t(property \"Reference\" \"U\" (at 0 0 0)\n \
\t\t(effects (font (size 1.27 1.27)))\n \
\t\t)\n \
\t\t(property \"Value\" \"\" (at 0 0 0)\n \
\t\t\t(effects (font (size 1.27 1.27)))\n \
\t\t)\n \
\t\t(property \"Footprint\" \"\" (at 0 0 0)\n \
\t\t\t(effects (font (size 1.27 1.27)) hide)\n \
\t\t)\n \
\t\t(property \"Datasheet\" \"\" (at 0 0 0)\n \
\t\t\t(effects (font (size 1.27 1.27)) hide)\n \
\t\t)\n \
\t\t(property \"ki_locked\" \"\" (at 0 0 0)\n \
\t\t\t(effects (font (size 1.27 1.27)))\n \
\t\t)\n"
# \t\t(symbol \"" + name + "_" + capa + "_1\" 
        wr += generador_pines(lista)
    wr += "\t)\n)"

    f.close()
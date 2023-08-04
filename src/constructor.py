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

    return lista, capas

def generador_pines():
    pass

def create_pin(name, number, bank):
    wr = "\t\t\t(pin "
    #tipo de pin

    #posicion

    #nombre
    wr += "\t\t\t\t(name \"" + name + "\" (effects (font (size 1.27 1.27))))\n"
    #numero
    wr += "\t\t\t\t(name \"" + number + "\" (effects (font (size 1.27 1.27))))\n"
    wr += "\t\t\t)\n"
    return wr

def create_square():
    p1_pos = (a,b)
    p2_pos = (c,d)

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

        lista, capas = listado(pines)
        

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
        wr += generador_pines()
    wr += "\t)\n)"

    f.close()
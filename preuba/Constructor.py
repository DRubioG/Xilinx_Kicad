import csv, operator
from operator import itemgetter
import os

#leer todos loss archivos
zynq_nam=[]
zynq=[]
cont=os.listdir('./zupall/')


#limite de contador
p=0
for archivo in cont:
   # if p==2:
    #    break
    #if archivo=="xczu9cgffvc900pkg.csv" or archivo=="xqzu9egffrc900pkg.csv":
    #    pass
    if archivo[-4:]== '.csv':
        zynq_nam.append(archivo)
        zynq.append(archivo[:-4])
        
    p+=1
#print(zynq)
pin=[]
pin_nam=[]
bank=[]

def leer_pines(k):
    cont=0
    ##Extraer nombre de pines, número y banco
    path='./zupall/' + zynq_nam[k]
    with open(path)  as csvarchivos:
        entrada=csv.reader(csvarchivos)
        lista=[]
        for reg in entrada:
            lista.append(reg)
    for string in lista:
        cont+=1
        if "Pin" in string:
            
            break
  #  print(cont)
   # res=["Pin" in string for string in lista]
   # if res==True:
   #     print("True")
   #  print(res)
    lista=lista[cont+1:-2]   #eliminamos las 82 primeras lineas y las dos ultimas, que no continene pines
  #  print(lista)
    lista=sorted(lista, key=itemgetter(3))
    #lista=sorted(lista, key=itemgetter(3))  #ordenar por el numero de banco
    #print(lista)
    pin=[]
    pin_nam=[]
    bank=[]
    for i in range(len(lista)): #clasificacion de pines
        pin.append(lista[i][0]) #meter los numeros de los pines en la lista 'pines'
       # print(pin)
        pin_nam.append(lista[i][1]) #meter los nombres de los pines en la lista 'pin_nam''
       # print(i)
        bank.append(lista[i][3]) #meter los bancos de cada pin en la lista 'bank'
    return pin, pin_nam, bank
#print(pin)

def listado(pin, pin_nam, bank):
    '''generador de lista de tuplas con todos los pines con sus nombres'''
    lista2=[]   #lista donde se mete la lista de valores
    lista1=[]   # lista donde se mete cada valor
    estado=0    # maq esta para banco NA
    bank_prev=bank[0]   #inicialización para conseguir que entre el primer pin

    bank_gnd=[]     # banco de GND
    bank_gnd_aux=[]
    list_aux=[]
    bank_mgt=[]     # banco de MGT
    bank_psmgt=[]   # banco de PSMGT
    bank_vcc=[]     # banco de VCC
    bank_nc=[]      # banco deNC
    lista_bnk=[bank_gnd, bank_mgt, bank_psmgt, bank_vcc, bank_nc]
    for i in range(len(pin)):
        
        if bank_prev != bank[i]:
            bank_prev=bank[i]
            if bank[i]=="NA":
                estado=1
            else:
                lista1=sorted(lista1, key=itemgetter(1))
                lista2.append(lista1)
                lista1=[]
        lista1.append([pin[i], pin_nam[i]])

        if estado==1:
            if pin_nam[i][:3]=="GND":
                bank_gnd.append(lista1[0])
            elif pin_nam[i][:5]=="MGTAV":
                bank_mgt.append(lista1[0])
            elif pin_nam[i][:6]=="PS_MGT":
                bank_psmgt.append(lista1[0])
            elif pin_nam[i][:3]=="VCC":
                bank_vcc.append(lista1[0])
            elif pin_nam[i][:2]=="NC":
                bank_nc.append(lista1[0])
            lista1=[]

    for t in lista_bnk:
        list_aux=[]
        if len(t)!=0:
            if len(t) >100:
                num=1
                for r in range(len(t)):
                    list_aux.append(t[r])
                    if r == 100*num:
                        lista2.append(list_aux)
                        num+=1
                        list_aux=[]
                lista2.append(list_aux)
            else:
                lista2.append(t)
    return lista2, len(lista2)
    
def generador_pines(lista):
    pines=lista
    ln=lon_lista(pines)
    #print(len)
    kicad=""
    
    for i in range(len(pines)):
        mitad=0
        max=0
        est=0
        leng=lon_lista(pines[i])
        ln=int(leng/2)
        #print(leng)
        if leng >=75:
            mitad=1

        #agregar rectangulo
        for l in range(leng):
            rt=len(pines[i][l][1])
            if rt >max:
                max=rt
        #print(max)
        if max < 19:
            x=650
        else:
            x=1000
        
        if mitad==1:
            u=int(ln/2)
        else:
            u=ln
        #print(u*100+200)
        kicad+="\nS "+ str(x-200) + " " + str(u*100+200) + " " + str(-x+200) + " " + str(-u*100-200) + " "+ str(i+1) + " 1 0 f"

        
        # agregar pines
        for j in range(leng):
           # x='650'
            lado='L'
            if mitad==1:
                dif=int((ln-j*2)/2)
                if j > leng/2:
                    if est==0:
                        x=-x
                        est=1
                    lado='R'
                    dif=int((ln-(j-ln)*2)/2)
            else:
                dif=ln-j

            kicad+=pin_create(pines[i][j][0], pines[i][j][1], 100*(dif), i+1, x=str(x), dir=lado)
    return kicad

def pin_create(pin_nam, num_pin, pos_pin, capa, x='650',  long='200', dir='L', text_tam='50', num_tam='50', Morg='1', visi='I'):
    return "\nX "+str(num_pin)+" " +str(pin_nam)+ " " + x +" "+str(pos_pin)+ " "+ str(long)+ " " + str(dir) + " " + str(text_tam) + " " +str(num_tam) + " " + str(capa) + " " +str(Morg)+" " +str(visi)


def lon_lista(lista):
    return len(lista)

def num_capas():    #numero de bancos
    bank_prev=""
    cont=0
    cont=pin_nam.count("GND")
    div=int(cont/100)
    banko=sorted(bank)
    for k in range(len(bank)):
        if bank_prev!=banko[k]:
            cont+=1
            bank_prev=banko[k]
    return cont+div

def num_pines(banco):   #numero de pines por banco
    return bank.count(banco)

bidirec=["PS_MIO", "IO_", "PS_DDR_DQS_N", "PS_DDR_DQS_P", "DONE", "INIT_B", "PS_DDR_DQ", "T0_DQS", "T1_DQS", "T2_DQS", "T3_DQS"]
power=["VCC", "PS_MIO_V", "GND", "PS_DDR_VREF", "VREF"]
output=["TDO", "PS_DDR_CKP", "PS_DDR_CKN", "PS_DDR_CKE", "PS_DDR_CS_B", "PS_DDR_RAS_B", "PS_DDR_CAS_B", "PS_DDR_WE_B", "PS_DDR_BA", "PS_DDR_A", "PS_DDR_ODT", "PS_DDR_DRST_B", "PS_DDR_DM", "PS_DDR_VRP", "PS_DDR_VRN", \
    "MGTXTXP", "MGTPTXP", "MGTXTXN", "MGTPTXN",]
#creador de pines
def create_pin():
    pin_kicad=""
    bank_prev=""
    capa=0
    visi='I'
    sq_y1=0
    sq_y2=0
    pin_nam_prev=0
    init=400
    t=0
    ult_capa=0
    cont_gnd=0
    def pin_create(pin_nam, num_pin, pos_pin, capa, x='650',  long='200', dir='L', text_tam='50', num_tam='50', Morg='1', visi='I'):
        return "X "+str(pin_nam)+" " +str(num_pin)+ " " + x +" "+str(pos_pin)+ " "+ str(long)+ " " + str(dir) + " " + str(text_tam) + " " +str(num_tam) + " " + str(capa) + " " +str(Morg)+" " +str(visi)

    for j in range(len(pin)):

        ##Asignacion de capas
        t+=1
        visi='I'
        if bank[j]!= bank_prev  :
            capa+=1
            if capa<num_capas():
                visi='I'
                bank_prev=bank[j]
                t=0
                init=num_pines(bank[j])*50
                print("init banco ", bank[j], init)
                sq_y1=init+200
                sq_y2=-init-100
                pin_kicad+="\nS 450 "+ str(sq_y1) + " -700 " + str(sq_y2) + " " + str(capa) + " 1 0 f"
            elif capa==num_capas():
                if ult_capa==0:
                    t=0
                    #print("Entro1")
                    ult_capa=1
                 #   visi='W'
                    gnd=pin_nam.count("GND")
                    init=(gnd)*50
                    sq_y1=init+200
                    sq_y2=-init-100
                    pin_kicad+="\nS 450 "+ str(sq_y1) + " -600 " + str(sq_y2) + " " + str(capa) + " 1 0 f"
            else:
                capa=num_capas()+1
        if ult_capa==1:
            if pin_nam[j]=="GND":
               # visi="W"
                capa=num_capas()
                capa_ult=capa
                pin_nam_prev=1
           # elif pin_nam[j]=="NC":

            else:
               # visi="W"
                if pin_nam_prev==1:
                    #print("entro2")
                    t=0
                    pin_nam_prev=0
                    capa=capa_ult+1
                    init=(num_pines(bank[j])-gnd)*50
                   # print((num_pines(bank[j])-gnd)*50)
                    sq_y1=init+200
                    sq_y2=-init-100 
                    pin_kicad+="\nS 450 "+ str(sq_y1) + " -600 " + str(sq_y2) + " " + str(capa) + " 1 0 f"
      
      #definición de cada tipo de pin
        for l in bidirec:
            if pin_nam[j][:len(l)]==l:
                visi="B"
        for o in power:
            if pin_nam[j][:len(o)]==o:
                visi="W"
        for h in output:
            if pin_nam[j][:len(h)]==h:
                visi="O"
        if pin_nam[j]=="NC":
            visi="N"

        pin_kicad+="\n"+pin_create(pin_nam[j],pin[j], (init-t*100), capa, visi=visi)
    return pin_kicad


def longitud():
    lon_max=0
    cont=0
    for k in range(len(bank)):
        lon=bank.count(bank[k])
        #print(lon)
        if lon>lon_max:
            lon_max=lon
    return lon_max



#apertura de fichero
f=open("ZynqUltra.lib", "w")


wr="EESchema-LIBRARY Version 2.4 \n#encoding utf-8"

#print(dat)

j=0
for i in zynq:
    p=""
    cont=0
    flag=0
    y=0
    i=i[:-3]
  #  print(i)
    for lh in range(len(i)):
       # print("letra ->", i[lh])
        if i[lh].isnumeric():
            flag=1
           # print("FLAG")
        if flag==1:
        #    print("\t\t\tflag -> 1")
        #    print((i[lh].isalpha()))
            if (i[lh].isalpha())== True:
                cont+=1
       #         print("i[lh]: ", i[lh])
      #          print("cont: ", cont)

        if cont>2 and y==0:
            #if y==0:
            y=1
            # print("dentro")
            p+="-"+i[lh]
            flag=0
        else:
          #  print("Restante")
            p+=i[lh]
     #   print("nombre actual -> ", p)
       # print("--------------------------------")

   # print("nombre final->", p)
    print(p)
    pin, pin_nam, bank=leer_pines(j)
    lista, capas=listado(pin, pin_nam, bank)
   # print(capas)
    dat=-int(longitud()*50+150)
    wr+="\n#\n# "+p+"\n#"
    wr+="\nDEF "+p.upper()+" U 0 40 Y Y "+str(capas)+" L N"
    #print("numero de bancos: ", num_capas())
    wr+="\nF0  \"U\" -550 "+str(-3000-100)+" 50 H V C CNN" #posicion del identificador
    wr+="\nF1  \""+ p.upper() +"\" -450 "+str(3100)+" 50 H V C CNN" #posicion del nombre del simbolo
    wr+="\nF2  \"\" 0 "+str(3000)+" 50 H I C CNN"
    wr+="\nF3  \"\" 0 "+str(3000)+" 50 H I C CNN"
    wr+="\nDRAW"
   # wr+=create_pin()
    #listado(pin, pin_nam, bank)
    wr+=generador_pines(lista)
    wr+="\nENDDRAW"
    wr+="\nENDDEF"
    j=j+1
wr+="\n#\n#End library"
#Escritura
f.write(wr)
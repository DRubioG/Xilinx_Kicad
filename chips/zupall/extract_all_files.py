import csv
import os
import shutil

cont = os.listdir("./chips/zupall")
path = "./"
# os.mkdir("./chips/zupall/new_folder")

for archivo in cont:
    if archivo[-4:] == ".csv":
        with open("./chips/zupall/"+archivo)  as csvarchivos:
            entrada=csv.reader(csvarchivos)
            lista=[]
            for reg in entrada:
                lista.append(reg)

        for line in lista:
            if line[0].find("Device") != -1:
                device = line[0].split(" ")[-1]
                if device.find("/") != -1:
                    files = device.split("/")
                    con = 0
                    for f in files:
                        if con != 0:
                            shutil.copy("./chips/zupall/" + archivo, "./chips/zupall/new_folder/"+f+".csv")
                        con = 1


                    print("encontrado")
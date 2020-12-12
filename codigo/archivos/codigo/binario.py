from datetime import datetime
import os
import time
import sys

FILE_INPUT = "input.txt"
FILE_OUTPUT = "output.txt"
FILE_OUT_TEMP = "temp.txt"
DATE_FORMAT = "%d %m %Y %H:%M:%S %p"

def main():

    ipconfig = os.system("ipconfig")
    print(ipconfig)

    ejecutando = True
    count = 0    
    while ejecutando:
        print(datetime.strftime(datetime.now(),DATE_FORMAT))

        try:            
            read_file = open(FILE_INPUT,"r")
            text = read_file.readlines()
            read_file.close()
            write_file = open(FILE_OUTPUT,"w+")

            print("Elementos encontrados: ", str(len(text)))
            
            for t in text:
                
                if t == "0":
                    print(t)
                    print(ejecutando)
                    ejecutando = False
                    print(ejecutando)
                    break

                write_file.writelines(t)
            
            write_file.close()

        except FileNotFoundError as fnf:
            print("Archivo no existe")
            ejecutando = False
            break
        except FileExistsError as fee:
            print("Archivo existe error")
            ejecutando = False
            break
        finally:
            if not ejecutando:
                try:
                    print("Validando archivo...")              
                    if not os.path.exists(FILE_OUT_TEMP):
                        os.rename(FILE_OUTPUT,FILE_OUT_TEMP)
                    else:
                        os.remove(FILE_OUT_TEMP)
                        os.rename(FILE_OUTPUT,FILE_OUT_TEMP)
                        print("Backup generado.")
                except FileNotFoundError as e:
                    print(e.values)
        print("sleep...")
        count+=1
        print("Procesos ejecutados: ", count)
        time.sleep(60)
        print("wake up...")
    print("bye.")
main()
#DOCUMENTACION:
#https://rico-schmidt.name/pymotw-3/datetime/index.html
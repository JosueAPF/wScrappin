#!/usr/bin/env python
#tecnica de web scraping
#uso de terminal tables para la creacion de un menu chafa XD
#para salir del menu y sub-menus pulsar q
import urllib.request
from terminaltables import AsciiTable

class web_s():

    def __init__(self):

        while True:

            frame = [['Web Scraping','press solo numeros'],
                     ['1. Extraccion de sitio web',' 2. ayuda']]

            table = AsciiTable(frame)
            print(table.table)
            break
    def ifs(self):
        while True:
            user_input = input("opciones (1-2):")
            if user_input == "1":
                try:
                    self.lol = input('ingrese una url valida (http//:www.web.net) :')
                    datos = urllib.request.urlopen(self.lol).read().decode()
                    print(datos)
                    break
                except ValueError:
                    print("url no valido utilize una url valida HDP")
                finally :
                    pass
            elif user_input == "2":
                print("Puedes usar este link")
                print("https://niinnongmon.com/scraping/")
            elif user_input == "q":
                break
            else:
                print("\n")

   

while True:
    print("r = repit , q = exit")
    info = web_s()
    info.ifs()
    user_input = input(":")
    if user_input == "r":
        info = web_s()
        info.ifs()
    elif user_input == "q":
        break
        
    

 




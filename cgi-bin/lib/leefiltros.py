#!/usr/bin/env python3
error = False
ruta = "/home/artus/dev/python/proxyMonitor/dominios_bloqueados"
filtros = ""

try:
    file_filtros = open(ruta).readlines()

    for linea in file_filtros:
        filtros = filtros + linea

        
except:
    mensaje_error = "<h2>ERROR: no se ha podido encontrar el archivo</h2>"
    error = True
    #print(error)
    

    #print(address0, netmask0, network0, broadcast0)
    

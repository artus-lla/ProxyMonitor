#!/usr/bin/env python3
error = False
rutai = "/home/artus/dev/python/proxyMonitor/interfaces"
try:
    datosRed = open(rutai).readlines()
    # Obtener índice de la lista para encontrar parámet
    # i = 0
    # for linea in datosRed:
    #     print(i, linea, end='')
    #     i = i + 1
    
    # eth0 - desde índice 9
    addr0 = datosRed[9][9:]
    netm0 = datosRed[10][9:]
    netw0 = datosRed[11][9:]
    broa0 = datosRed[12][11:]

    # eth1
    addr1 = datosRed[16][9:]
    netm1 = datosRed[17][9:]
    netw1 = datosRed[18][9:]
    broa1 = datosRed[19][11:]
    gate1 = datosRed[20][9:]
except:
    mensaje_error = "<h2>ERROR: no se ha podido encontrar el archivo</h2>"
    error = True
    #print(error)
    

    #print(address0, netmask0, network0, broadcast0)
    

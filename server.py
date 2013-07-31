#!/usr/bin/env python3

import sys, os
from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 20020

manejador = CGIHTTPRequestHandler
manejador.cgi_directories = ["/cgi-bin"] # Directorio de los scripts

# Si se ingresa como argumento un puerto lo toma y reemplaza por el valor de PORT
if len(sys.argv) > 1:
       PORT = sys.argv[1]

addres_server = ('localhost', int(PORT))

# CGIHTTPRequestHandler es el manejador
serverHTTP = HTTPServer(addres_server, manejador)

print("Servidor CGI escuchando en {} puerto {}".format(addres_server[0], addres_server[1]))

# # Se inicia el ciclo infinito de escucha del servidor
serverHTTP.serve_forever()

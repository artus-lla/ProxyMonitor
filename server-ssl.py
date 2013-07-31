#!/usr/bin/env python3

import sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl

PORT = 20030

# Si se ingresa como argumento un puerto lo toma y reemplaza por el valor de PORT
if len(sys.argv) > 1:
       PORT = sys.argv[1]


addres_server = ('localhost', int(PORT))
# CGIHTTPRequestHandler es el manejador
handler = CGIHTTPRequestHandler
serverHTTP = HTTPServer(addres_server, handler)
#handler.cgi_directories = ["/cgi-bin/"]

# Agregar ssl
serverHTTP.socket = ssl.wrap_socket(serverHTTP.socket,
                                    certfile='./server.pem',
                                     server_side=True)

print("Servidor CGI escuchando en el puerto", PORT)

# # Se inicia el ciclo infinito de escucha del servidor
serverHTTP.serve_forever()
print(PORT, addres_server)


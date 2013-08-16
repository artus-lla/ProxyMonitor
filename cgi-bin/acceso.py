#!/usr/bin/env python3

import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html
import lib.core as core

mi_html.insertar_content_type()

usuario_auth = b'YWRtaW4='
password_auth = b'YWRtaW4x'

def validar_usuario_y_contrasenia(correcto = False):
    # Obtener campos del formulario
    campos = cgi.FieldStorage()

    usuario = campos.getvalue('usuario_input')
    contrasenia = campos.getvalue('password_input')
    
    # Nos aseguramos que los campos no estén vacíos
    if usuario == None or contrasenia == None:
        correcto = False
    elif core.decodificar(usuario_auth).decode() != usuario:
        correcto = False
    elif core.decodificar(password_auth).decode() != contrasenia:
        correcto = False
    else:
        correcto = True        

    return correcto
        

if validar_usuario_y_contrasenia() is True:
    mi_html.encabezado("ProxyMonitor - Inicio")
    print("<br /><br /><h4>Bienvenido a ProxyMonitor</h4>")
    mi_html.pie()
else:
    print("<br/><h2>ERROR: Acceso denegado</h2>")

if __name__ == "__main__":
    pass
    

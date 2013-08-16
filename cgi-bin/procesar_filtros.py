#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html
mi_html.insertar_content_type()

campos = cgi.FieldStorage()
# Valores textarea
filtros  = campos.getvalue('filtros_textarea')

fileb = open("dominios_bloqueados", 'w')
fileb.write(filtros)
fileb.close()

print("<h3>OK... Cambios aplicados</h3>")
print('<br /><a href="/cgi-bin/filtros.py">Volver</a>')

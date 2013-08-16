#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html

#try:
mi_html.insertar_content_type()
mi_html.encabezado_red()
mi_html.pie()


#except:
#    print("<h2>ERROR: No se ha encontrado el archivo interfaces")


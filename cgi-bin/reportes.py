#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html

mi_html.insertar_content_type()
mi_html.encabezado_reportes()
mi_html.pie()


#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html

mi_html.encabezado("ProxyMonitor - Inicio")
print("<br /><br /><h4>Bienvenido a ProxyMonitor</h4>")
mi_html.pie()


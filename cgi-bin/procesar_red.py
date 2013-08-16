#!/usr/bin/env python3
import cgi, cgitb
cgitb.enable()

import lib.mi_html as mi_html
mi_html.insertar_content_type()

campos = cgi.FieldStorage()
# Valores eth0
env_ip_eth0      = campos.getvalue('dir_ip_eth0_input')
env_mask_eth0    = campos.getvalue('mask_red_eth0_input')
env_network_eth0 = campos.getvalue('network_eth0_input')
env_broad_eth0   = campos.getvalue('broad_eth0_input')


# Valores eth1
env_ip_eth1      = campos.getvalue('dir_ip_eth1_input')
env_mask_eth1    = campos.getvalue('mask_red_eth1_input')
env_network_eth1 = campos.getvalue('network_eth1_input')
env_broad_eth1   = campos.getvalue('broad_eth1_input')
env_gatew_eth1   = campos.getvalue('puerta_eth1_input')

# print(env_ip_eth0,
#       env_mask_eth0,
#       env_network_eth0,
#       env_broad_eth0,
      
#       env_ip_eth1,
#       env_mask_eth1,
#       env_network_eth1,
#       env_broad_eth1,
#       env_gatew_eth1
#       )

plantilla_interfaces="""\
# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
auto eth1

# Interfaz para conexión a la red local
iface eth0 inet static
	address {}
	netmask {}
	network {}
	broadcast {}
	
# Interfaz para conexión a Internet
iface eth1 inet static
	address {}
	netmask {}
	network {}
	broadcast {}
	gateway {}
""".format(env_ip_eth0, env_mask_eth0, env_network_eth0, env_broad_eth0, env_ip_eth1, env_mask_eth1, env_network_eth1, env_broad_eth1, env_gatew_eth1)

#print(plantilla_interfaces)

file = open('interfaces', 'w')
file.write(plantilla_interfaces)
file.close()
print("<h3>OK... Cambios aplicados</h3>")
print('<br /><a href="/cgi-bin/red.py">Volver</a>')




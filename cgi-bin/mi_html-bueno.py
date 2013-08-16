#!/usr/bin/env python3

import lib.interfaces as nic  #en red.py se llama desde lib

def insertar_content_type():
    print("Content-Type:text/html\n")


def encabezado(title):
    texto = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="description" content="ProxyMonitor: Monitor para un proxy de red" />
    <link rel="stylesheet" type="text/css" href="../../ui/css/main.css" />
    <title>
      {titulo}
    </title>
  </head>

  <body>
   <header>
    <h1>ProxyMonitor</h1>
   </header>
   
    <nav>
      <ul>
	<li><a href="red.py">Red</a></li>
	<li><a href="filtros.py">Filtros de contenido</a></li>
	<li><a href="reportes.py">Reportes</a></li>
      </ul>
    </nav>
""".format(titulo=title)

    print(texto)

## ====== Obtener datos de las interfaces de red y mostrarlos en html5 =====
nics = dict(ip_eth0 = nic.addr0,
            netmask_eth0 = nic.netm0,
            network_eth0 = nic.netw0,
            broadcast_eth0 = nic.broa0,
            gateway0 = nic.gate0,
            
            ip_eth1 = nic.addr1,
            netmask_eth1 = nic.netm1,
            network_eth1 = nic.netw1,
            broad_eth1 = nic.broa1, 
            gateway1 = nic.gate1)

def encabezado_red():
    texto = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="description" content="ProxyMonitor: Monitor para un proxy de
				      red" />
    <link rel="stylesheet" type="text/css"  href="../../ui/css/main.css" />

    <title>
      Red -  ProxyMonitor
    </title>
  </head>

  <body>
    <header>
      <h1><a href="inicio.py" title="Inicio">ProxyMonitor</a></h1>    
    </header>
    
    <nav>
      <ul>
	<li><a href="#" class="on-place">Red</a></li>
	<li><a href="filtros.py">Filtros de contenido</a></li>
	<li><a href="reportes.py">Reportes</a></li>
      </ul>
    </nav>
<section>
  <nav class="nav2">
    <a href="#" class="on-place2">Interfaces de red</a>
    </nav>
</section>
    <section class="section-contenedor">
      <section class="form-section">
	<form class="form-red">
	  <fieldset>
	    <legend>eth0</legend>
	    <div class="marco-red">
	      <div>
		<label for="dir_ip_eth0">Dirección IP:         </label>
		<input type="text" id="dir_ip_eth0" name="dir_ip_eth0_input"
		       required="required" autofocus="autofocus"
                       value="{ip_eth0}" />
	      </div>

	      <div>
		<label for="mask_red_eth0">Máscara de red:   </label>
		<input type="text" id="mask_red_eth0" name="mask_red_eth0_input"
	  	       required="required"
                       value="{netmask_eth0}"/>
	      </div>

              <div>
                <label for="network_eth0">Red:                     </label>
	      <input type="input" id="network_eth0" name="network_eth0_input"
	  	     required="required"
                     value="{network_eth0}" />
              </div>
    
              <div>
		<label for="broad_eth0">Broadcast:           </label>
		<input type="text" id="broad_eth0" name="broad_eth0_input"
	  	       value="{broadcast_eth0}" />
	      </div>

              <div>
		<label for="puerta_eth0">Puerta de enlace: </label>
		<input type="text" id="puerta_eth0" name="puerta_eth0_input"
	  	       value="{gateway0}" />
	      </div>
    
	    </div>
	 <!--
	    <div>
	      <input type="submit" name="boton_enviar_eth0" value="Guardar" />
            </div> -->

	  </fieldset>
	</form>
      </section>

      <section class="form-section">
        <form class="form-red">
	  <fieldset>
	    <legend>eth1</legend>
	    <div class="marco-red">
	      <div>
		<label for="dir_ip_eth1">Dirección IP:         </label>
		<input type="text" id="dir_ip_eth1" name="dir_ip_eth1_input"
		       required="required" autofocus="autofocus"
                       value="{ip_eth1}" />
	      </div>

	      <div>
		<label for="mask_red_eth1">Máscara de red:   </label>
		<input type="text" id="mask_red_eth1" name="mask_red_eth1_input"
	  	       required="required"
                 value="{netmask_eth1}"   />
	      </div>

	      <div>
		<label for="network_eth1">Red:                     </label>
		<input type="text" id="network_eth1" name="network_eth1_input"
                 value="{network_eth1}"  />
	      </div>

               <div>
		<label for="broad_eth1">Broadcast:           </label>
		<input type="text" id="broad_eth1" name="broad_eth1_input"
	  	  value="{broad_eth1}"     />
	      </div>

              <div>
		<label for="puerta_eth1">Puerta de enlace: </label>
		<input type="text" id="puerta_eth1" name="puerta_eth1_input"
	  	  value="{gateway1}"   />
	      </div>
    
	    </div>
	    

	   <!--
	    <div>
	      <input type="submit" name="boton_enviar_eth0" value="Guardar" />
            </div>  -->

	  </fieldset>

	</form>
<input type="submit"  name="ene" value="yes" />
      </section>
    </section>
""".format(**nics)
    print(texto)

def encabezado_filtros():
    texto = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="description" content="ProxyMonitor: Monitor para un proxy de
				      red" />
    <link rel="stylesheet" type="text/css"  href="../../ui/css/main.css" />

    <title>
      Filtros de contenido - ProxyMonitor
    </title>
  </head>

  <body>
   <header>
    <h1><a title="Inicio" href="inicio.py">ProxyMonitor</a></h1>
   </header>
   
    <nav>
      <ul>
	<li><a href="red.py">Red</a></li>
	<li><a href="#" class="on-place">Filtros de contenido</a></li>
	<li><a href="reportes.py">Reportes</a></li>
      </ul>
    </nav>
  
<section class="section-contenedor">
   <section>
	<form  class="marco-sitios-bloqueados">
	  <div>
	    <label for="agregar">Ingrese la dirección: </label>
	    <input type="text" id="agregar" name="agregar_iput"
		   autofocus="autofocus" />
	    <input type="submit" name="boton_agregar" value="Agregar" />
	  </div>
	</form>
   </section>

	<section>
	  <form class="marco-sitios-bloqueados">
	    <fieldset>
	      <legend>Lista de sitios bloqueados</legend>
	      <ol>
		<li>youtube.com <a href=""> Eliminar</a></li>
		<li>google.com <a href=""> Eliminar</a></li>
		<li>vimeo.com <a href=""> Eliminar</a></li>
	      </ol>
	    </fieldset>
	  </form>
	</section>
</section>"""



    print(texto)


def encabezado_reportes():
    texto = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="description" content="ProxyMonitor: Monitor para un proxy de
				      red" />
    <link rel="stylesheet" type="text/css"  href="../../ui/css/main.css" />

    <title>
      Reportes - ProxyMonitor
    </title>
  </head>

  <body>
   <header>
    <h1><a href="inicio.py" title="Inicio">ProxyMonitor</a></h1>
   </header>
   
    <nav>
      <ul>
	<li><a href="red.py">Red</a></li>
	<li><a href="filtros.py">Filtros de contenido</a></li>
	<li><a href="#" class="on-place">Reportes</a></li>
      </ul>
    </nav>
    <section class="frame">
    <iframe src="../sarg/index.html"></iframe> 
    </section>
    """

    print(texto)

def contenido():
    pass

def pie():
    texto = """
<footer>
     Copyleft © artus
    </footer>
    
  </body>
</html>
"""
    print(texto)

if __name__ == "__main__":
    encabezado("Título")

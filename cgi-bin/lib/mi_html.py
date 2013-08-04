#!/usr/bin/env python3

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
		       required="required" autofocus="autofocus" />
	      </div>

	      <div>
		<label for="mask_red_eth0">Máscara de red:   </label>
		<input type="text" id="mask_red_eth0" name="mask_red_eth0_input"
	  	       required="required" />
	      </div>

	      <div>
		<label for="puerta_eth0">Puerta de enlace: </label>
		<input type="text" id="puerta_eth0" name="puerta_eth0_input"
	  	       />
	      </div>
	    </div>
	    

	    <div class="marco-red">
	      <label for="puerta_eth0">Obtener una dirección IP automáticamente </label>
	      <input type="checkbox" id="puerta_eth0" name="puerta_eth0_input"
	  	     />
	    </div>

	    <div>
	      <input type="submit" name="boton_enviar_eth0" value="Guardar" />
            </div>
	  </fieldset>
	</form>
      </section>

      <section class="form-section">
        <form class="form-red">
	  <fieldset>
	    <legend>eth1</legend>
	    <div class="marco-red">
	      <div>
		<label for="dir_ip_eth0">Dirección IP:         </label>
		<input type="text" id="dir_ip_eth0" name="dir_ip_eth0_input"
		       required="required" autofocus="autofocus" />
	      </div>

	      <div>
		<label for="mask_red_eth0">Máscara de red:   </label>
		<input type="text" id="mask_red_eth0" name="mask_red_eth0_input"
	  	       required="required" />
	      </div>

	      <div>
		<label for="puerta_eth0">Puerta de enlace: </label>
		<input type="text" id="puerta_eth0" name="puerta_eth0_input"
	  	       />
	      </div>
	    </div>
	    

	    <div class="marco-red">
	      <label for="puerta_eth0">Obtener una dirección IP automáticamente </label>
	      <input type="checkbox" id="puerta_eth0" name="puerta_eth0_input"
	  	     />
	    </div>

	    <div>
	      <input type="submit" name="boton_enviar_eth0" value="Guardar" />
            </div>
	  </fieldset>
	</form>
	
	
      </section>
    </section>
"""
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
    </nav>"""

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

<header>
    <h1>Prototipo Minimarket La Esquina</h1>
    <p>Este prototipo fue creado para la 3era evaluación de proyecto de integración, es un proyecto creado con django con las funcionalidades básicas para el funcionamiento del minimarket la esquina</p>
  </header>
    <h2>2. Instalación</h2>
    <p>Pasos para instalar el proyecto localmente:</p>
    <pre><code># Se clona el repositorio y se ingresa a la carpeta
    git clone https://github.com/Benjarod/PrototipoLaEsquina.git
    cd PrototipoLaEsquina
  </code></pre>
  <hr/>
    <pre><code># Se crea el entorno virtual (hay que tener python instalado en el equipo)
    python -m venv env
  </code></pre>
  <hr/>
    <pre><code># Se inicia el entorno virtual
    .\env\Scripts\activate
  </code></pre>
  <hr/>
    <pre><code># Se ingresa a la carpeta "LaEsquina" y se instalan las librerias necesarias especificadas en el archivo "requeriments.txt"
    cd LaEsquina
    pip install -r requirements.txt
  </code></pre>
  <hr/>
    <pre><code># se sealizan las migraciones
    python manage.py migrate
  </code></pre>
    <hr/>
    <pre><code># Se Inicia el proyecto
    python manage.py runserver
  </code></pre>
</body>
</html>

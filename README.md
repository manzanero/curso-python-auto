# Curso de Automatización con Python 

Recursos del curso de automatización con Python


## Software necesario para el curso

Para poder empezar el curso se requiere:

### 1. Git

Software de control de versiones que se usará para guardar el progreso

1. Visitar https://git-scm.com/downloads
2. Seleccionar el sistema operativo para empezar la descarga
3. Iniciar el instalador y dejar todo por defecto
4. Ejecutar "C:/Program Files/Git/cmd/git-gui.exe" o poner "Git GUI" en el buscador de windows
5. Clicar en "Help" > "Show SSH Key" > "Generate Key", dejar vacío el campo de contraseña
6. Copiar la clave RSA pública generada
7. En caso de no tener una cuenta GitHub, navegar a https://github.com/ y crearla
8. Logándose en Github, ir a "Setting" del usuario > [SSH keys](https://github.com/settings/keys) > "New SSH Key"
9. Pegar la clave RSA pública y clicar "Add SSH Key"

### 2. Anaconda

Se trata de un paquete de aplicaciones para experimentar con código escrito en Python 

1. Visitar https://www.anaconda.com/products/individual para descargar la última distribución de Anaconda
2. Iniciar el instalador y dejar todo por defecto menos en opciones avanzadas, donde se desmarca la de "default Python"

### 3. Python

El intérprete base que ejecuta los archivos con la extensión ".py" que contienen el código

1. Visitar https://www.python.org/downloads/release/python-3100/ para descargar la última distribución de Python
2. Iniciar el instalador y elegir "customize installation", luego "next"
3. Marcar "Add Python to environment variables" y poner "C:/Users/{user}/Python310" como ruta de instalación
4. Al terminar la instalación, clicar la opción de "disable length limit", si aparece (requiere permisos de admin)

Para comprobar que la instalación es correcta y que las rutas "C:/Users/{user}/Python310/" y 
"C:/Users/{user}/Python310/Scripts/" están en el "path", abrir un cmd y poner:

```shell
python -V
```

El resultado debería ser "Python 3.10.0" en cualquier otro caso añadir a mano las rutas a la variable de entorno del
sistema "path" las dos rutas mencionadas

### 4. PyCharm

Editor de código especializado en Python

1. Descargar la versión "Community" del enlace https://www.jetbrains.com/es-es/pycharm/download/
2. Dejar todo por defecto o marcar opcionalmente "open folder as project" y crear acceso directo en el escritorio


## Clonar el repositorio del curso

1. Crear la carpeta "workspaces" en "C:/Users/{user}/" ("C:/Users/{user}/workspaces/")
2. Clicar con el botón derecho en la carpeta "workspaces" > "Git Bash Here" e introducir estos comandos:

```shell
git config --global user.name "{user_github}"
git config --global user.email {email}
git clone git@github.com:Manzanero/curso-python-auto.git  # si pide confirmación, escribir "yes" 
cp -r curso-python-auto/test-lab .
```

Esto habrá creado la carpeta "C:/Users/{user}/workspaces/test-lab" con todo el contenido del curso

Hasta aquí deberíamos contar con esta estructura de carpetas:

```
C:/
 ...
  +- Users/
  |   ...
  |    +- {user}/
  |        ...
  |         +- Anaconda3/
  |         +- Python310/
  |         +- workspaces/
  |              +- curso-python-auto/
  |              +- test-lab/
  +- Program Files/
      ...
       +- JetBrains/
            +- PyCharm Community Edition 2021/
```

## Abrir un capítulo del curso

1. Abrir Anaconda Navigator desde el menú de inicio
2. Ejecutar el módulo JupiterLab, se abrirá un navegador automáticamente en la url http://localhost:8888/lab
3. Con el Explorador de archivos de la izquierda navegar hasta "~/workspaces/test-lab" y seleccionar un capítulo


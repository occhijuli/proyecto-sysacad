# proyecto-sysacad

[Información Útil](https://cake-sushi-9a6.notion.site/Info-til-1c29afa16efd8055b44ddbd7f53260b8?pvs=4)


## Instalación

1. Cloná el repositorio.

2. Creá un entorno virtual en la carpeta del proyecto:
   ```bash
   python -m venv env_name
   ```
   O bien, podés crearlo en una carpeta diferente *(sugerido)*:
   ```bash
   python -m venv C:\Users\userX\environments\gral_env
   ```

3. Activá el entorno virtual. Dependiendo de la terminal que uses, el comando varía:

   **Git Bash (Windows):**
   ```bash
   source env_name/Scripts/activate
   ```

   **CMD (Windows):**
   ```cmd
   env_name\Scripts\activate
   ```

   Una vez activado, deberías ver algo como `(env_name)` al inicio de la línea en tu terminal.  
   Si no lo ves, probá con:
   ```bash
   which python
   ```

4. Instalá las dependencias en el entorno virtual seleccionado:
   ```bash
   pip install -r requirements.txt
   ```

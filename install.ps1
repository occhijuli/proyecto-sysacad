# Se necesitan tener los permisos de seguridad configurados con Set-ExecutionPolicy RemoteSigned
# Para ello, abrir la consola de PowerShell como administrador y ejecutar:
# Set-ExecutionPolicy RemoteSigned

# Activar el entorno virtual
# Cambiar la ruta del entorno virtual si es necesario
& "$env:USERPROFILE\environments\gral_env\Scripts\Activate.ps1"

Write-Host "✅ Entorno virtual 'gral_env' activado correctamente." -ForegroundColor Green

# Instalar dependencias
pip install -r requirements.txt
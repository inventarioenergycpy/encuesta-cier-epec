@echo off
setlocal
echo ==============================================================================
echo        DESPLIEGUE Y SINCRONIZACION: ENCUESTA CIER EPEC (2025-2026)
echo ==============================================================================
powershell -ExecutionPolicy Bypass -File "%~dp0scripts\vault_manager.ps1" -Action unlock
if %ERRORLEVEL% NEQ 0 (
    echo Despliegue cancelado.
    pause
    exit /b %ERRORLEVEL%
)

echo Sincronizando con GitHub...
git add .
git commit -m "update: actualizacion de analisis y dashboard CIER"
git push origin main
echo Despliegue completado exitosamente.
pause

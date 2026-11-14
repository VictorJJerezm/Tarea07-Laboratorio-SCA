# Laboratorio controlado – Tarea 07, SAST/SCA/SBOM

**Importante:** este repositorio es una aplicación de laboratorio **independiente** de OWASP NodeGoat. No constituye evidencia de que NodeGoat haya sido saneado. Se usará para obtener un **FAILED y un SUCCESS reales en el mismo laboratorio**, sin reducir la política CVSS >= 7.0 ni excluir dependencias de los escaneos.

## Prueba 1: falla esperada por vulnerabilidad conocida

1. Crea un repositorio de GitHub **nuevo y vacío**, llamado por ejemplo `Tarea07-Laboratorio-SCA` (sin README inicial).
2. Extrae este ZIP a una carpeta local y abre PowerShell en ella.
3. Publica el contenido (incluida la carpeta oculta `.github`) mediante:

   ```powershell
   git init -b main
   git add .
   git commit -m "Baseline SCA: lodash vulnerable"
   git remote add origin https://github.com/TU_USUARIO/Tarea07-Laboratorio-SCA.git
   git push -u origin main
   ```

4. Abre **Actions** y busca el workflow `Tarea 07 - Laboratorio controlado SAST SCA SBOM`.
5. Confirma que SAST y las pruebas funcionales se ejecutan. SCA debería detectar la dependencia `lodash@4.17.11` y bloquear por CVSS >= 7.0, además de generar el SBOM.
6. Conserva URL, captura FAILED, JSON, HTML y SBOM. Si el error fuera técnico, no lo presentes como vulnerabilidad: inspecciona el registro.

## Prueba 2: corregir de forma verificable

1. En la carpeta del repositorio, ejecuta:

   ```powershell
   npm install lodash@4.18.1 --save-exact --ignore-scripts --no-audit --no-fund
   npm test
   git add package.json package-lock.json
   git commit -m "Fix SCA: actualizar lodash a version corregida"
   git push origin main
   ```

2. En Actions, comprueba que Semgrep, Syft y Dependency-Check ejecuten de forma completa. **Solo considera SUCCESS si GitHub marca ambos jobs verdes y SCA genera un informe nuevo sin alertas bloqueantes**.
3. Descarga nuevo JSON/HTML y SBOM. Documenta comparación de versiones, alerta original, diferencia de reportes y commit correctivo.
4. Si `4.18.1` recibiera una nueva vulnerabilidad CVSS >= 7.0 al momento de ejecutar, consulta una versión posterior corregida, pruébala y vuelve a ejecutar; no suprimas el hallazgo.

## Limitaciones y alcance

- Este proyecto no demuestra una reparación de las 60 entradas bloqueantes de NodeGoat. La ejecución NodeGoat #7 permanece FAILED por esas alertas.
- El archivo `package-lock.json` se genera en GitHub Actions durante la primera ejecución y debe añadirse al repositorio con el commit correctivo. La versión de lodash está fijada exactamente en `package.json` desde el estado inicial.
- Los resultados dependen de las bases de datos de vulnerabilidades disponibles en la fecha de ejecución, por lo que nunca debe prometerse un resultado verde antes de verificarlo en GitHub.
- No publiques el laboratorio como servicio en Internet; solo requiere ejecución de análisis y pruebas dentro de GitHub Actions.

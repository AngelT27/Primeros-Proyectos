# Flujo de trabajo con Git y GitHub

Este documento describe el ciclo recomendado para editar, versionar y subir cambios al repositorio, además de una guía rápida para cuando no quieras complicarte.

---

## Ciclo recomendado (paso a paso)

1. **Edita y guarda**  
   - Abre el archivo `.py` que quieras modificar en VS Code.  
   - Realiza los cambios necesarios.  
   - Guarda con **Ctrl+S**.

2. **Revisa el estado**  
   ```bash
   git status
   ```
   Verás qué cambió (`modified`/`untracked`).

3. **Prepara el commit**  
   - Solo un archivo:  
     ```bash
     git add nombre_archivo.py
     ```
   - Todos los cambios:  
     ```bash
     git add .
     ```

4. **Confirma con mensaje claro**  
   ```bash
   git commit -m "fix: corregir cálculo de propina en Tip_calculator.py"
   ```

5. **Empuja a GitHub**  
   ```bash
   git push
   ```
   *(la primera vez en la rama:)*  
   ```bash
   git push -u origin main
   ```

6. **Si GitHub ya tenía cambios**  
   - Integra antes de empujar:  
     ```bash
     git pull --rebase origin main
     # Resuelve conflictos si aparecen
     git push
     ```

---

## Estilo sugerido para mensajes de commit

- `feat:` nueva funcionalidad  
- `fix:` corrección de bug  
- `refactor:` reestructura sin cambiar comportamiento  
- `docs:` cambios solo en documentación  
- `chore:` mantenimiento (config, `.gitignore`, etc.)

**Ejemplos:**
- `fix: no contar producto tras ValueError en precio`
- `feat: alineación dinámica de columnas`
- `chore: mover .py a OrderSystem y limpiar export`

---

## Guía rápida para subir cambios a GitHub

1. **Editar y guardar**  
   - Abre el archivo que quieras modificar.  
   - Haz los cambios.  
   - Guarda con **Ctrl+S**.

2. **Agregar cambios a Git**  
   - Solo un archivo:  
     ```bash
     git add nombre_archivo.py
     ```
   - Todos los cambios:  
     ```bash
     git add .
     ```

3. **Hacer commit**  
   ```bash
   git commit -m "Descripción breve del cambio"
   ```

4. **Subir a GitHub**  
   ```bash
   git push
   ```

5. **Verificar en GitHub**  
   - Abre tu repositorio en el navegador y confirma que los cambios estén.

---

💡 **Consejo:** Haz commits pequeños y con mensajes claros. Evita agrupar cambios sin relación en el mismo commit.
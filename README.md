# FFFFFFstudio — web del estudio y propuestas

Sitio estático servido con GitHub Pages.

- `index.html` — la web de FFFFFFstudio.
- `propuestas/<negocio>/index.html` — una maqueta por cliente potencial, cada una en su carpeta.
- `.nojekyll` — evita que GitHub procese el sitio con Jekyll.

## Publicarlo por primera vez

1. Crea un repositorio **público** en GitHub llamado `fffffstudio-web`.
2. Desde esta carpeta:

   ```bash
   git init
   git add .
   git commit -m "Web del estudio y primeras propuestas"
   git branch -M main
   git remote add origin https://github.com/aro42-ua/fffffstudio-web.git
   git push -u origin main
   ```

3. En GitHub: **Settings → Pages → Source: Deploy from a branch → Branch: main / (root)** y guarda.
4. En un par de minutos estará en `https://aro42-ua.github.io/fffffstudio-web/`.

## Añadir una propuesta nueva

```bash
mkdir -p propuestas/nombre-del-negocio
cp maqueta.html propuestas/nombre-del-negocio/index.html
git add . && git commit -m "Propuesta: Nombre del negocio" && git push
```

Queda publicada en `https://aro42-ua.github.io/fffffstudio-web/propuestas/nombre-del-negocio/`.

## Nota

Cada maqueta lleva una barra visible que dice "Propuesta de diseño · maqueta no oficial ·
FFFFFFstudio · Ángel Rubio". No la quites: deja claro que la página es una propuesta y no la
web real del negocio.

## Publicación automática desde Drive

Las maquetas nuevas llegan solas: la tarea diaria las deja en la carpeta pública de Drive
**"PUBLICAR - maquetas (carpeta publica)"** y el workflow `.github/workflows/sync-propuestas.yml`
las recoge cada 30 minutos y las publica en `propuestas/<slug>/`.

Configuración (una sola vez):

1. En Drive, la carpeta PUBLICAR tiene que estar compartida como **"Cualquier persona con el enlace → Lector"**.
2. Clave de API de Google (solo lectura de archivos públicos):
   console.cloud.google.com → proyecto nuevo → *APIs y servicios* → *Habilitar* "Google Drive API"
   → *Credenciales* → *Crear credenciales* → *Clave de API* → *Restringir clave* → solo "Google Drive API".
3. En GitHub: *Settings → Secrets and variables → Actions → New repository secret*:
   nombre `DRIVE_API_KEY`, valor la clave del paso 2.
4. Pestaña *Actions* → "Sincronizar propuestas desde Drive" → *Run workflow* para probarlo.

El script (`scripts/sync_drive.py`) solo escribe dentro de `propuestas/`, solo acepta archivos
llamados `maqueta-<slug>.html`, y no borra nada nunca. Para retirar una propuesta, borra su
carpeta a mano y haz push.

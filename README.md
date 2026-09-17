# FFFFFFstudio — web del estudio y propuestas

Sitio estático servido con GitHub Pages.

- `index.html` — la web de FFFFFFstudio.
- `propuestas/<negocio>/index.html` — una maqueta por cliente potencial, cada una en su carpeta.
- `.nojekyll` — evita que GitHub procese el sitio con Jekyll.

## Publicarlo por primera vez

1. Crea un repositorio **público** en GitHub llamado `fffffstudio` (o el nombre que prefieras).
2. Desde esta carpeta:

   ```bash
   git init
   git add .
   git commit -m "Web del estudio y primeras propuestas"
   git branch -M main
   git remote add origin https://github.com/TU-USUARIO/fffffstudio.git
   git push -u origin main
   ```

3. En GitHub: **Settings → Pages → Source: Deploy from a branch → Branch: main / (root)** y guarda.
4. En un par de minutos estará en `https://TU-USUARIO.github.io/fffffstudio/`.

## Añadir una propuesta nueva

```bash
mkdir -p propuestas/nombre-del-negocio
cp maqueta.html propuestas/nombre-del-negocio/index.html
git add . && git commit -m "Propuesta: Nombre del negocio" && git push
```

Queda publicada en `https://TU-USUARIO.github.io/fffffstudio/propuestas/nombre-del-negocio/`.

## Nota

Cada maqueta lleva una barra visible que dice "Propuesta de diseño · maqueta no oficial ·
FFFFFFstudio · Ángel Rubio". No la quites: deja claro que la página es una propuesta y no la
web real del negocio.

# 🧠 Célula IA · Hitofusion

Espacio público de coordinación del portafolio de inteligencia artificial y su plan director 2026.

- **Sitio:** https://hito2026.github.io/hito-celulaia-proyectos2026/
- **Repositorio:** https://github.com/hito2026/hito-celulaia-proyectos2026
- **Plan editable:** [`plan_directo/plan_director.md`](plan_directo/plan_director.md)
- **Borrador conservado:** [`plan_directo/borrador_original.md`](plan_directo/borrador_original.md)

## Actualizar la documentación

1. Editar el plan director en GitHub o en una copia local.
2. Registrar el cambio en Git y publicarlo en `main`.
3. Revisar el despliegue de **Pages** en GitHub y luego el sitio.

El sitio incluye directamente el Markdown: no hay una segunda copia del plan que mantener. Las propuestas y campos pendientes deben seguir identificados hasta su aprobación explícita.

```sh
git pull --ff-only origin main
# Editar plan_directo/plan_director.md
python3 -m unittest discover -s tests -v
git add plan_directo/plan_director.md
git commit -m "docs: update AI master plan"
git push origin main
```

## Sitio y verificación

GitHub Pages compila Jekyll desde la raíz de `main` (**Settings → Pages → Deploy from a branch**). `_config.yml` configura la ruta del proyecto y excluye tareas internas y pruebas del sitio. El repositorio completo sigue siendo público.

`index.html` aporta navegación y estructura; `assets/style.css` define el diseño inspirado en Notion, adaptable a móvil y preparado para teclado e impresión. No hay JavaScript, analítica, fuentes remotas ni dependencias de frontend.

Las pruebas con Python 3 comprueban inclusión del plan, destinos de navegación, configuración del subdirectorio y reglas responsive. No sustituyen la compilación Jekyll de Pages ni la revisión visual en navegador. Para previsualizar, se puede usar Jekyll si ya está instalado (`jekyll serve --baseurl /hito-celulaia-proyectos2026`); no es requisito para editar el Markdown.

## Criterios documentales

El plan propone una estructura alineada con prácticas de PMBOK, sin afirmar certificación, edición específica ni aprobación de presupuestos o fechas. La gestión del portafolio y la gestión de cada proyecto se distinguen; las fichas individuales deben completarse con el equipo.

**Todo es público:** no subir secretos, información de clientes ni documentos confidenciales. No hay afiliación con Notion ni PMI.

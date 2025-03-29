# Generador de contexto para Cody — Inclusión inteligente solo de Markdown

Este script está diseñado para **generar un archivo `cody.json`** que incluya únicamente los archivos `.md` relevantes desde un subdirectorio específico hacia abajo, permitiendo que [Cody (de Sourcegraph)](https://sourcegraph.com/cody) acceda solo al contexto más útil y evitando información innecesaria.

---

## 📌 Caso de uso

Imagina que estás trabajando en un proyecto con mucha documentación, con una estructura como esta:

```
proyecto-raiz/
├── .git/
├── tools/
│   └── scripts-antiguos/
├── docs/
│   └── materiales-formativos/
│       └── curso-A/
│           ├── unidad-1/
│           │   └── apuntes.md
│           ├── unidad-2/
│           │   └── ejercicios.md
│           └── resumen.md
└── README.md
```

En este caso, solo quieres que **Cody cargue contexto desde `curso-A/` en adelante**, y no desde todo el repositorio, ya que podría contener miles de archivos markdown antiguos o irrelevantes.

---

## 🎯 Qué hace este script

✅ Detecta automáticamente la **raíz del proyecto** al encontrar un directorio `.git` o `.vscode`  
✅ Desde el **directorio actual**, busca solo hacia abajo  
✅ Recopila todos los archivos `.md` y escribe un `cody.json` en la raíz del proyecto  
✅ Las rutas incluidas son **relativas a la raíz del proyecto**, como requiere Cody  
✅ Omite carpetas del sistema como `.git`, `node_modules`, `venv`, etc.

---

## 🧠 ¿Por qué no incluir todo el proyecto?

En repositorios grandes, incluir todos los `.md` puede provocar:

- ❌ Que Cody lea contenido desactualizado o irrelevante
- ❌ Problemas de rendimiento por exceso de contexto
- ❌ Respuestas confusas si analiza información ajena al trabajo actual

Este script resuelve eso al **limitar el contexto a solo la parte del proyecto en la que estás trabajando**, como una carpeta de curso, módulo o unidad, mientras genera el archivo de configuración en la raíz (donde Cody lo puede usar correctamente).

---

## 🚀 Cómo usarlo

1. Coloca el script en cualquier parte del proyecto
2. Abre una terminal en la **carpeta objetivo** (por ejemplo, `curso-A/`)
3. Ejecuta:

```bash
python generate_cody_json_md_files.py
```

4. El script:
   - Detectará la raíz del proyecto (por ejemplo, donde esté `.git`)
   - Generará el archivo `cody.json` en esa raíz
   - Incluirá únicamente archivos `.md` desde tu carpeta actual hacia abajo

---

## 📁 Ejemplo de salida `cody.json`

```json
{
  "context": {
    "include": [
      "docs/materiales-formativos/curso-A/unidad-1/apuntes.md",
      "docs/materiales-formativos/curso-A/unidad-2/ejercicios.md",
      "docs/materiales-formativos/curso-A/resumen.md"
    ],
    "exclude": []
  }
}
```

---

## 🛡️ Notas

- Cody solo lee `cody.json` si está ubicado en la **raíz del proyecto**  
- Las rutas deben ser **relativas a la raíz**, no al directorio desde donde ejecutas el script  
- Solo se incluyen archivos `.md` — ideal para flujos centrados en documentación  
- Puedes personalizar fácilmente el script para incluir otros tipos de archivo si lo necesitas

---

## 📦 Funcionalidades opcionales (próximamente)

- Copia de seguridad automática del `cody.json` existente  
- Logs con marcas de tiempo  
- Filtros personalizados por tipo de archivo  
- Modo simulación (dry-run)

---

## 🧑‍💻 Autor

Creado por **José Luis Íñigo**, también conocido como **Riskoo**

- GitHub: [github.com/joseluisinigo](https://github.com/joseluisinigo)  
- Web: [joseluisinigo.work](https://joseluisinigo.work)

---

## 📄 Licencia

Este script es libre para usar, modificar y redistribuir **siempre y cuando se mencione adecuadamente al autor original**.  
Es obligatorio acreditar a `José Luis Íñigo` / `Riskoo` en cualquier trabajo derivado o redistribución.

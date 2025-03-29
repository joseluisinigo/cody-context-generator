# Cody Context Generator — Markdown-only Smart Inclusion

This script is designed to **generate a `cody.json` file** that includes only relevant `.md` files from a specific subdirectory downward, allowing [Cody (by Sourcegraph)](https://sourcegraph.com/cody) to access the most useful context without noise.

---

## 📌 Use Case

Imagine you're working in a documentation-rich project like this:

```
project-root/
├── .git/
├── tools/
│   └── old-scripts/
├── docs/
│   └── training-materials/
│       └── course-A/
│           ├── unit-1/
│           │   └── notes.md
│           ├── unit-2/
│           │   └── exercises.md
│           └── summary.md
└── README.md
```

You only want **Cody to load context from `course-A/` and below**, not from the entire `project-root/`, which may contain thousands of irrelevant markdown files from archived tools, scripts, or external documentation.

---

## 🎯 What This Script Does

✅ Automatically finds the **project root** by detecting a `.git` or `.vscode` directory  
✅ From **your current working directory**, it searches **only downward**  
✅ Collects all `.md` files and writes a `cody.json` in the project root  
✅ All paths in the output are **relative to the project root**, as required by Cody  
✅ Skips system folders like `.git`, `node_modules`, `venv`, etc.

---

## 🧠 Why Not Include the Whole Project?

In large repositories, including every `.md` file can cause:

- ❌ Irrelevant or outdated content to be loaded by Cody
- ❌ Performance issues when the context is too large
- ❌ Confusing answers if Cody reads unrelated material

This script solves that by **limiting the context scope to only what you're working on**, typically a course/module/unit folder — while still writing the config at the root so Cody picks it up correctly.

---

## 🚀 How to Use

1. Place the script anywhere in your project
2. Open a terminal inside the **target folder** (e.g., `course-A/`)
3. Run:

```bash
python generate_cody_json_md_files.py
```

4. The script will:
   - Locate the project root (e.g., where `.git` is)
   - Generate `cody.json` there
   - Include only `.md` files from your current folder and downward

---

## 📁 Example `cody.json` Output

```json
{
  "context": {
    "include": [
      "docs/training-materials/course-A/unit-1/notes.md",
      "docs/training-materials/course-A/unit-2/exercises.md",
      "docs/training-materials/course-A/summary.md"
    ],
    "exclude": []
  }
}
```

---

## 🛡️ Notes

- Cody reads `cody.json` only from the **project root**.  
- Paths must be **relative to the root**, not to where the script runs.  
- Only `.md` files are included — this is intentional for documentation-heavy workflows.  
- You can easily customize the script to include other file types or patterns.

---

## 📦 Optional Features (coming soon?)

- Auto-backup of existing `cody.json`
- Timestamped logs
- Customizable file type filters
- Dry-run mode

---

## 🧑‍💻 Author

Created by **José Luis Íñigo** a.k.a. **Riskoo**

- GitHub: [github.com/joseluisinigo](https://github.com/joseluisinigo)  
- Website: [joseluisinigo.work](https://joseluisinigo.work)

---

## 📄 License

This script is free to use, modify, and redistribute **as long as proper credit is given to the original author**.  
Mentioning the author (`José Luis Íñigo` / `Riskoo`) is required in any derivative work or redistribution.

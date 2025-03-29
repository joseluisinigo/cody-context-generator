import os
import json

# Markers to detect the root of the project
PROJECT_ROOT_MARKERS = [".git", ".vscode"]

# Folders we want to exclude
EXCLUDED_FOLDERS = {".git", "venv", "__pycache__", "node_modules", ".vscode", ".idea", ".mypy_cache"}

def find_project_root(start_path):
    """
    Traverse upwards to find the root directory of the project.
    """
    current = os.path.abspath(start_path)
    while True:
        for marker in PROJECT_ROOT_MARKERS:
            if os.path.exists(os.path.join(current, marker)):
                return current
        parent = os.path.dirname(current)
        if parent == current:
            break
        current = parent
    raise RuntimeError("❌ Could not find project root (missing .git or .vscode)")

def collect_md_from_current_down(base_path, project_root):
    """
    Collect all .md files from the current directory downwards,
    and return their paths relative to the project root.
    """
    md_paths = []

    for current_dir, dirs, files in os.walk(base_path):
        # Filter out unwanted dirs
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FOLDERS]

        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(current_dir, file)
                relative_path = os.path.relpath(full_path, project_root)
                md_paths.append(relative_path.replace("\\", "/"))  # Normalize for Windows

    return md_paths

def generate_cody_json(md_paths, output_path):
    """
    Write the cody.json file to the root of the project.
    """
    config = {
        "context": {
            "include": md_paths,
            "exclude": []
        }
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"✅ cody.json generated at '{output_path}' with {len(md_paths)} .md files.")
    for path in md_paths:
        print(f"  - {path}")

if __name__ == "__main__":
    try:
        current_dir = os.getcwd()
        project_root = find_project_root(current_dir)
        md_files = collect_md_from_current_down(current_dir, project_root)
        cody_json_path = os.path.join(project_root, "cody.json")
        generate_cody_json(md_files, cody_json_path)
    except RuntimeError as e:
        print(str(e))

import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [
    PROJECT_ROOT / "naive_bayes_text" / "imdb_movie_review_classification_nb_sklearn.ipynb",
    PROJECT_ROOT / "svm_digits" / "handwritten_digits_classification_svm_sklearn.ipynb",
]
FORBIDDEN_PATTERNS = [
    re.compile(r"/Users/"),
    re.compile(r"/private/"),
    re.compile(r"api[_ -]?key\s*=", re.IGNORECASE),
    re.compile(r"access[_ -]?token\s*=", re.IGNORECASE),
    re.compile(r"password\s*=", re.IGNORECASE),
    re.compile(r"sk-[A-Za-z0-9]"),
]


def cell_text(cell):
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return str(source)

for notebook in NOTEBOOKS:
    data = json.loads(notebook.read_text())
    cells = data.get("cells", [])
    if not cells:
        raise SystemExit(f"{notebook} has no cells")
    if not any(cell.get("cell_type") == "code" for cell in cells):
        raise SystemExit(f"{notebook} has no code cells")
    for cell in cells:
        text = cell_text(cell)
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                raise SystemExit(f"{notebook.name}: forbidden marker {pattern.pattern}")
        if cell.get("cell_type") == "code":
            if cell.get("outputs"):
                raise SystemExit(f"{notebook.name}: code cell output is not cleared")
            if cell.get("execution_count") is not None:
                raise SystemExit(f"{notebook.name}: execution_count is not cleared")
    print(f"notebook valid: {notebook.name} cells={len(cells)}")

print("validate_notebooks passed")

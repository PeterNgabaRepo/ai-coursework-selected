from pathlib import Path
import importlib.util
import sys

sys.dont_write_bytecode = True

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = PROJECT_ROOT / "minimax_alpha_beta"
sys.path.insert(0, str(MODULE_DIR))


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


random_gametree = load_module("random_gametree", MODULE_DIR / "random_gametree.py")
minimax_module = load_module("minimax", MODULE_DIR / "minimax.py")

random_gametree.seed(5)
tree = random_gametree.gametree(10, 6)
root = tree.get_root()
tree.generate()
processed = minimax_module.minimax(root)

if processed <= 0:
    raise SystemExit("expected minimax to process at least one node")
if root.key not in {-1, 0, 1}:
    raise SystemExit(f"unexpected minimax score: {root.key}")

print(f"smoke_minimax passed: processed={processed}, score={root.key}")

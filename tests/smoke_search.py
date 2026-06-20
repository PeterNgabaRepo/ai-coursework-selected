from pathlib import Path
import importlib.util
import sys

sys.dont_write_bytecode = True


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "search_algorithms" / "hw2.py"
MAZE_PATH = PROJECT_ROOT / "search_algorithms" / "maze.txt"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


hw2 = load_module("hw2", MODULE_PATH)

maze = []
for line in MAZE_PATH.read_text().splitlines():
    maze.append([char for char in line if char not in {" ", "\n"}])

vertices = hw2.buildVectorList(maze)
edges = hw2.buildEdgeList(maze)
graph = hw2.graph(vertices, edges)

if not vertices:
    raise SystemExit("expected at least one traversable vertex")
if not edges:
    raise SystemExit("expected at least one edge")

hw2.BFS(graph, vertices[0])
visited = sum(1 for vertex in graph.vertices if vertex.parent != -1)

if visited == 0:
    raise SystemExit("expected BFS to visit at least one neighbor")

print(f"smoke_search passed: vertices={len(vertices)}, edges={len(edges)}, visited={visited}")

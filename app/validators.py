import ast
from app.config import BLOCKED_IMPORTS


def validate_code(code: str):
    tree = ast.parse(code)

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in BLOCKED_IMPORTS:
                    raise Exception(f"Blocked import: {alias.name}")

        if isinstance(node, ast.ImportFrom):
            if node.module:
                if node.module.split(".")[0] in BLOCKED_IMPORTS:
                    raise Exception(f"Blocked import: {node.module}")

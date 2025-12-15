#3️⃣ YAML Loader
#📄 src/tests_runner/loader.py

import yaml
from pathlib import Path


def load_test(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_tests_from_dir(dir_path: str):
    tests = []
    for path in Path(dir_path).rglob("*.yaml"):
        tests.append(load_test(path))
    return tests
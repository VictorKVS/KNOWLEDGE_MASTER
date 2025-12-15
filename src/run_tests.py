#6️⃣ Minimal CLI Runner
#📄 src/run_tests.py

from tests_runner.loader import load_tests_from_dir
from tests_runner.executor import TestExecutor


def main():
    executor = TestExecutor()
    tests = load_tests_from_dir("tests")

    for test in tests:
        executor.run(test)

    print(f"✅ All {len(tests)} tests passed")


if __name__ == "__main__":
    main()
#4️⃣ Assertions (laws)
#📄 src/tests_runner/assertions.py

class TestAssertionError(Exception):
    pass


def assert_equals(actual, expected, message):
    if actual != expected:
        raise TestAssertionError(f"{message}: expected={expected}, actual={actual}")
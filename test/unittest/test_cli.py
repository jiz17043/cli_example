import subprocess
import sys

def test_cli_example():
    result = subprocess.run([sys.executable, "src/cli_example.py", "TestUser"], capture_output=True, text=True)
    assert "Hello, TestUser! Welcome to the CLI example." in result.stdout

def test_greet_cli_default():
    result = subprocess.run([sys.executable, "src/greet_cli.py", "TestUser"], capture_output=True, text=True)
    assert "Hello, TestUser!" in result.stdout

def test_greet_cli_custom():
    result = subprocess.run([sys.executable, "src/greet_cli.py", "TestUser", "--greeting", "Hi"], capture_output=True, text=True)
    assert "Hi, TestUser!" in result.stdout

def test_math_cli_add():
    result = subprocess.run([sys.executable, "src/math_cli.py", "2", "3", "--operation", "add"], capture_output=True, text=True)
    assert "Result: 5" in result.stdout

def test_math_cli_subtract():
    result = subprocess.run([sys.executable, "src/math_cli.py", "5", "2", "--operation", "subtract"], capture_output=True, text=True)
    assert "Result: 3" in result.stdout

def test_math_cli_multiply():
    result = subprocess.run([sys.executable, "src/math_cli.py", "4", "3", "--operation", "multiply"], capture_output=True, text=True)
    assert "Result: 12" in result.stdout

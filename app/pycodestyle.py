import os
import sys
import subprocess


def run_flake8(script_path):
    """Run flake8 on the specified script."""
    flake8_command = f"flake8 {script_path} --max-line-length=120"
    flake8_result = subprocess.run(flake8_command, shell=True, capture_output=True, text=True, check=False)
    print("flake8 output:")
    print(flake8_result.stdout)
    print(flake8_result.stderr)


def run_pylint(script_path):
    """Run pylint on the specified script."""
    pythonpath = os.pathsep.join([os.getcwd(), os.path.join(os.getcwd(), "backend"), os.path.join(os.getcwd(), "frontend")])
    pylint_command = (
        f"PYTHONPATH={pythonpath} pylint {script_path} "
        "--max-line-length=120 "
        "--disable=C0103,C0114,C0115 "
        "--generated-members=cv2.*"
    )
    pylint_result = subprocess.run(pylint_command, shell=True, capture_output=True, text=True, check=False)
    print("pylint output:")
    print(pylint_result.stdout)
    print(pylint_result.stderr)


def run_linters(script_path):
    """Run flake8 and pylint on the specified script."""
    run_flake8(script_path)
    run_pylint(script_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pycodestyle.py <your_script.py>")
    else:
        run_linters(sys.argv[1])

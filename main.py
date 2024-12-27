import os
import subprocess
import sys

def create_setup_py(script_name):
    setup_content = f"""
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("{script_name}")
)
"""
    with open("setup.py", "w") as f:
        f.write(setup_content)

def compile_with_cython(script_name):
    create_setup_py(script_name)
    subprocess.run([sys.executable, "setup.py", "build_ext", "--inplace"])

def obfuscate_with_pyarmor(script_name):
    subprocess.run(["pyarmor", "pack", "-x", "--exclude", "pandas", "--exclude", "numpy", "-e", "--onefile", script_name])

def main():
    if len(sys.argv) != 2:
        print("Usage: python automate.py <script_name.py>")
        sys.exit(1)
    
    script_name = sys.argv[1]
    
    if not script_name.endswith(".py"):
        print("Only .py (Python files) are supported.")
        sys.exit(1)

    print("Starting the obfuscation process...")
    
    # Step 1: Convert Python script to Cython and compile
    print("Compiling with Cython...")
    compile_with_cython(script_name)
    
    # Step 2: Obfuscate the compiled extension with PyArmor
    print("Obfuscating with PyArmor...")
    obfuscate_with_pyarmor(script_name)
    
    print("Process completed successfully!")

if __name__ == "__main__":
    main()	
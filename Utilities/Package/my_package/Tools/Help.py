# coding: utf-8



import os
import inspect
import importlib.util

def help():
    print("Please select a package and function in the following format:")
    print("from {package} select {function}\n")
    print("Below are the list of available packages:\n")
    
    # Set the directory to scan
    target_dir = os.path.join(os.getcwd(), "..")  # This points to the parent directory of 'Utilities'

    # Walk through the directory structure
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # Skip the Help.ipynb file and main.py, and ensure we only include .py files
            if file.endswith(".py") and file not in ["Help.ipynb", "main.py"]:
                # Get the module path relative to the target directory
                module_path = os.path.relpath(os.path.join(root, file), target_dir)
                module_name = module_path.replace(os.sep, ".").rstrip(".py")
                
                # Dynamically import the module
                try:
                    spec = importlib.util.spec_from_file_location(module_name, os.path.join(root, file))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Get all functions in the module
                    functions = inspect.getmembers(module, inspect.isfunction)
                    
                    # Print the module name and its functions
                    if functions:
                        print(f"{module_name}:")
                        for func_name, _ in functions:
                            print(f"  {func_name}")
                        print()
                except Exception as e:
                    pass
                    # print(f"Could not load module {module_name}: {e}")


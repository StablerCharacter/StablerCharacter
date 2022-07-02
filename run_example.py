import sys
import os
import importlib

if not os.path.isdir(os.path.join(os.getcwd(), "examples", sys.argv[1])):
    print("The example you specified does not exist.")
    sys.exit(1)
print(f"Running {sys.argv[1]}...")

sys.path.append(os.getcwd())
importlib.import_module(f"examples.{sys.argv[1]}")

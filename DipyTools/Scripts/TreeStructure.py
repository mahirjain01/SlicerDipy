import importlib
import inspect
import pkgutil
import dipy
import warnings

dipy_subpackages = ["io", "reconst", "segment", "tracking",]

warnings.filterwarnings('ignore') 

def list_dipy_contents():
    dipy_structure = {}

    for subpackage_name in dipy_subpackages:
        full_subpackage_name = f"dipy.{subpackage_name}"

        try:
            subpackage_module = importlib.import_module(full_subpackage_name)
            dipy_structure[subpackage_name] = {}
        except ImportError:
            continue

        if hasattr(subpackage_module, "__path__"):
            for module_info in pkgutil.iter_modules(subpackage_module.__path__):
                module_name = module_info.name
                full_module_name = f"{full_subpackage_name}.{module_name}"
                
                try:
                    module = importlib.import_module(full_module_name)
                    dipy_structure[subpackage_name][module_name] = []
                except ImportError:
                    continue

                for name, obj in inspect.getmembers(module, inspect.isfunction):
                    dipy_structure[subpackage_name][module_name].append(name)

    return dipy_structure

# dipy_structure = list_dipy_contents()

# for subpackage, modules in dipy_structure.items():
#     print(f"\nSubpackage: {subpackage}")
#     for module, functions in modules.items():
#         print(f"  Module: {module}")
#         for func in functions:
#             print(f"    Function: {func}")

from os.path import dirname, basename, isfile
import glob
from kezbot import *


def __list_all_modules():
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(f"{dirname(__file__)}/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(any(mod == module_name for module_name in all_modules) for mod in to_load):
                quit(1)

        else:
            to_load = all_modules

        if NO_LOAD:
            return [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]

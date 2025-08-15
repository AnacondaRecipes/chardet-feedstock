import os, importlib
m = importlib.import_module("test")
m.EXPECTED_FAILURES = {os.path.normpath(p) for p in m.EXPECTED_FAILURES}

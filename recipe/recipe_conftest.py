# On Windows, some tests were failing because the test data paths in
# EXPECTED_FAILURES were not normalized to a cross-platform format.
# As a result, path comparisons between the expected failures list
# and the actual file paths did not match on Windows.
# This file fixes the issue by normalizing all paths in EXPECTED_FAILURES
# (using os.path.normpath), ensuring the tests run correctly on Windows
# and other platforms.

import os, importlib
m = importlib.import_module("test")
m.EXPECTED_FAILURES = {os.path.normpath(p) for p in m.EXPECTED_FAILURES}

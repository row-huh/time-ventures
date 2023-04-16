import main
import pytest
import sys

sys.path.append("C:/Users/rohaa/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/_pytest")
print(sys.path)

def test_validate_username():
    assert main.validate_username("12") == False
    assert main.validate_username("roha") == "roha"
    
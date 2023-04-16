import main
import pytest
import sys


def test_validate_username():
    assert main.validate_username("12") == False
    assert main.validate_username("roha") == "roha"
    
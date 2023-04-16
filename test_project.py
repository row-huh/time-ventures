import project
import pytest
import sys


def test_validate_username():
    assert project.validate_username("12") == False
    assert project.validate_username("roha") == "roha"

def test_validate_username():
    assert project.validate_username("12") == False
    assert project.validate_username("roha") == "roha"

def test_validate_username():
    assert project.validate_username("12") == False
    assert project.validate_username("roha") == "roha"
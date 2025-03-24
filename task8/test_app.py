import pytest #unused...warning1
from app import add
#empty line warning2
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

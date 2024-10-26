import pytest, arrow
from dt_arrow import days_after_birth, years_from_birth, leap_years_in_range


def test_days_after_birth():
    assert days_after_birth(2024, 10,20) == (6, 0)

def test_years_from_birth():
    assert years_from_birth(5, 0) == (0,5)

def test_leap_years_in_range():
    assert leap_years_in_range(arrow.get(2024,01,01), arrow.now('US/Eastern')) == 1



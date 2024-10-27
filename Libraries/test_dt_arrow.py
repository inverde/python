import pytest, arrow
import warnings
from dt_arrow import days_after_birth, years_from_birth, leap_years_in_range

warnings.filterwarnings("ignore")

def test_days_after_birth():
    with pytest.deprecated_call():
        assert days_after_birth(2024, 10,20) == (6, 0)

def test_years_from_birth():
    assert years_from_birth(5, 0) == (0,5)

def test_leap_years_in_range():
    with pytest.raises(AssertionError):
        assert leap_years_in_range((2020, 2024)) == 0



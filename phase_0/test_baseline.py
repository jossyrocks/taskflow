from baseline import calculate_workday
import pytest


def test_calculate_workday_under_time():
    result = calculate_workday(6)
    assert result == {"status": "under_time", "hours": 2}


def test_calculate_workday_over_time():
    result = calculate_workday(12)
    assert result == {"status": "overtime", "hours": 4}


def test_calculate_workday_full_day():
    result = calculate_workday(8)
    assert result == {"status": "full_day", "hours": 0}

def test_calculate_workday_lower_boundary():
    result = calculate_workday(0)
    assert result == {"status": "under_time", "hours": 8}

def test_calculate_workday_upper_boundary():
    result = calculate_workday(24)
    assert result == {"status": "overtime", "hours": 16}

def test_calculate_workday_less_than_lower_boundary():
    with pytest.raises(ValueError):
        calculate_workday(-1)

def test_calculate_workday_higher_than_upper_boundary():
    with pytest.raises(ValueError):
        calculate_workday(25)
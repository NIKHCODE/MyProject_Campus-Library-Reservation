import pytest

from ski_resort_pass import (
    process_resort_bookings,
    check_chairlift_anemometer,
)


# --------------------------------------------------
# PROCESS RESORT BOOKINGS
# --------------------------------------------------

def test_invalid_groups_input():
    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 15.0)


def test_negative_facility_fee():
    with pytest.raises(ValueError):
        process_resort_bookings([], -10.0)


def test_inactive_group_is_skipped():
    groups = [
        {
            "is_active": False,
            "duration": "full_day",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result == {
        "total_revenue": 0.0,
        "status": "ZERO_SALES"
    }


def test_season_pass():
    groups = [
        {
            "is_active": True,
            "duration": "season",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 300.0


def test_half_day_pass():
    groups = [
        {
            "is_active": True,
            "duration": "half_day",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 50.0


def test_invalid_pass_duration():
    groups = [
        {
            "is_active": True,
            "duration": "weekly",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["status"] == "ZERO_SALES"


def test_child_discount():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 10}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 48.0


def test_senior_discount():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 70}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 56.0


def test_invalid_skier_age():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 0}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["status"] == "ZERO_SALES"


def test_blackout_override_full_day():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [
                {
                    "age": 30,
                    "blackout_override": True
                }
            ]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 40.0


def test_blackout_override_half_day():
    groups = [
        {
            "is_active": True,
            "duration": "half_day",
            "skiers": [
                {
                    "age": 30,
                    "blackout_override": True
                }
            ]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 0.0
    assert result["status"] == "ZERO_SALES"


def test_gear_rental_charge():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [
                {
                    "age": 30,
                    "gear_rental": True
                }
            ]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 115.0


def test_lodge_locker_fee():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "includes_lodge_locker": True,
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["total_revenue"] == 95.0


def test_default_group_values():
    groups = [
        {
            "is_active": True
        }
    ]

    result = process_resort_bookings(groups, 15.0)

    assert result["status"] == "ZERO_SALES"


def test_audit_review_after_five_rejections():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 0}]
        }
        for _ in range(5)
    ]

    result = process_resort_bookings(groups, 15.0)

    
    assert result["status"] == "AUDIT_REVIEW"


# --------------------------------------------------
# CHAIRLIFT ANEMOMETER
# --------------------------------------------------

def test_no_wind_data():
    assert check_chairlift_anemometer([]) == "NO_DATA"


def test_safe_wind_conditions():
    wind_streams = [
        [20, 25, 30, 35],
        [15, 22, 28]
    ]

    assert check_chairlift_anemometer(wind_streams) == "SAFE_OPERATION"


def test_single_high_wind_reading():
    assert check_chairlift_anemometer([[50]]) == "SAFE_OPERATION"


def test_two_consecutive_high_wind_readings():
    assert check_chairlift_anemometer([[50, 52]]) == "SUSPEND_LIFT"


def test_high_wind_interrupted_by_safe_reading():
    wind_streams = [[50, 30, 52, 55]]

    assert check_chairlift_anemometer(wind_streams) == "SUSPEND_LIFT"


def test_high_wind_readings_on_separate_lifts():
    wind_streams = [
        [50],
        [52]
    ]

    assert check_chairlift_anemometer(wind_streams) == "SAFE_OPERATION"


def test_wind_exactly_at_threshold():
    assert check_chairlift_anemometer([[45, 45]]) == "SAFE_OPERATION"
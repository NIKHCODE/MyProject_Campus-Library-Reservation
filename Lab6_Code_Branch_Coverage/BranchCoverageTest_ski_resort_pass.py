import pytest

from ski_resort_pass import (
    process_resort_bookings,
    check_chairlift_anemometer,
)


# ==================================================
# INPUT VALIDATION
# ==================================================

def test_invalid_groups_type():
    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 15.0)


def test_negative_facility_fee():
    with pytest.raises(ValueError):
        process_resort_bookings([], -1.0)


def test_valid_empty_groups():
    result = process_resort_bookings([], 15.0)
    assert result["status"] == "ZERO_SALES"


# ==================================================
# GROUP PROCESSING AND PASS DURATION BRANCHES
# ==================================================

def test_inactive_group():
    groups = [{"is_active": False}]
    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


def test_active_group_with_default_duration():
    groups = [
        {
            "is_active": True,
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 80.0


@pytest.mark.parametrize(
    "duration, expected",
    [
        ("season", 300.0),
        ("full_day", 80.0),
        ("half_day", 50.0),
    ],
)
def test_all_valid_pass_durations(duration, expected):
    groups = [
        {
            "is_active": True,
            "duration": duration,
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == expected


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


def test_empty_skiers_list():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": []
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


# ==================================================
# SKIER AGE AND DISCOUNT BRANCHES
# ==================================================

def test_invalid_age_branch():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 0}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


def test_child_age_branch():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 11}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 48.0


def test_adult_age_branch():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 80.0


def test_senior_age_branch():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 65}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 56.0


# ==================================================
# BLACKOUT OVERRIDE BRANCHES
# ==================================================

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
                },
                {
                    "age": 30
                }
            ]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 0.0


# ==================================================
# GEAR RENTAL AND LOCKER BRANCHES
# ==================================================

def test_gear_rental_enabled():
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


def test_gear_rental_disabled():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 30, "gear_rental": False}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 80.0


def test_lodge_locker_included():
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


def test_lodge_locker_not_included():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "includes_lodge_locker": False,
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 80.0


# ==================================================
# FINAL STATUS BRANCHES
# ==================================================

def test_audit_review_status():
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


def test_completed_status():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 30}]
        }
    ]

    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "COMPLETED"


def test_zero_sales_status():
    result = process_resort_bookings([], 15.0)
    assert result["status"] == "ZERO_SALES"


# ==================================================
# CHAIRLIFT ANEMOMETER BRANCHES
# ==================================================

def test_empty_wind_streams():
    assert check_chairlift_anemometer([]) == "NO_DATA"


def test_safe_wind_readings():
    assert check_chairlift_anemometer([[20, 30, 40]]) == "SAFE_OPERATION"


def test_single_high_wind_reading():
    assert check_chairlift_anemometer([[50]]) == "SAFE_OPERATION"


def test_two_consecutive_high_wind_readings():
    assert check_chairlift_anemometer([[50, 51]]) == "SUSPEND_LIFT"


def test_high_wind_streak_reset():
    assert check_chairlift_anemometer(
        [[50, 30, 50]]
    ) == "SAFE_OPERATION"


def test_high_wind_streak_across_separate_lifts():
    assert check_chairlift_anemometer(
        [[50], [51]]
    ) == "SAFE_OPERATION"


def test_high_wind_after_reset():
    assert check_chairlift_anemometer(
        [[50, 30, 51, 52]]
    ) == "SUSPEND_LIFT"
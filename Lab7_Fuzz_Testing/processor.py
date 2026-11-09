
from datetime import datetime
import math


def parse_season_pass_validity(date_str):
    if not isinstance(date_str, str):
        return "Pass Expiry: INVALID (EXPIRED)"

    try:
        date = datetime.strptime(date_str, "%Y/%m/%d")

        valid = date.year >= 2026

        status = "VALID" if valid else "EXPIRED"

        return (
            f"Pass Expiry: {date.year:04d}-"
            f"{date.month:02d}-{date.day:02d} ({status})"
        )

    except ValueError:
        return "Pass Expiry: INVALID (EXPIRED)"


def compute_trail_gradient(elevation_str):
    if not isinstance(elevation_str, str):
        return 0.0

    try:
        parts = elevation_str.split(":")

        if len(parts) != 2:
            return 0.0

        drop = float(parts[0])
        distance = float(parts[1])

        if not math.isfinite(drop) or not math.isfinite(distance):
            return 0.0

        if drop < 0 or distance <= 0:
            return 0.0

        gradient_pct = (drop / distance) * 100.0

        return round(gradient_pct, 2)

    except ValueError:
        return 0.0


def calculate_lift_access_tier(zone_code):
    zone_rates = {
        "BEG": 35.0,
        "INT": 60.0,
        "ADV": 85.0,
        "ALL": 110.0
    }

    if not isinstance(zone_code, str):
        return 0.0

    prefix = zone_code.strip().upper()[:3]

    return zone_rates.get(prefix, 0.0)


def main():
    print("==== Running parse_season_pass_validity ====")
    d_input = input("Enter pass expiry (YYYY/MM/DD): ")
    print(parse_season_pass_validity(d_input))

    print("\n==== Running compute_trail_gradient ====")
    e_input = input("Enter drop:distance (e.g. 250:1000): ")
    print("Gradient %:", compute_trail_gradient(e_input))

    print("\n==== Running calculate_lift_access_tier ====")
    z_input = input("Enter zone code (e.g. BEG, INT, ALL): ")
    print("Lift Pass Price: $", calculate_lift_access_tier(z_input))


if __name__ == "__main__":
    main()

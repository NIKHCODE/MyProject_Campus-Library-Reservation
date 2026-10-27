"""Manage warehouse assets and their scheduled maintenance inspections."""

import json
import tempfile
from datetime import datetime, timedelta

# Application state
assets = {}
SERVICE_INTERVAL_DAYS = 90


def register_asset(asset_id, machine_type, logs=None):
    """Register a warehouse asset and record its registration."""
    if not isinstance(asset_id, str) or not asset_id.strip():
        raise ValueError("Asset ID cannot be empty.")

    if not isinstance(machine_type, str) or not machine_type.strip():
        raise ValueError("Machine type cannot be empty.")

    if logs is None:
        logs = []

    if asset_id in assets:
        raise ValueError(f"Asset {asset_id} is already registered.")

    assets[asset_id] = {
        "type": machine_type,
        "last_service": datetime.now().strftime("%Y-%m-%d"),
    }

    logs.append(asset_id)
    print(
        f"Registered {asset_id} - "
        f"total registrations this run: {len(logs)}"
    )


def update_service_date(asset_id, service_date):
    """Update an asset's last-service date after validating the input."""
    if asset_id not in assets:
        print("Asset not found.")
        return

    try:
        parsed_date = datetime.strptime(service_date, "%Y-%m-%d")
    except (ValueError, TypeError):
        print("Invalid date. Use YYYY-MM-DD format.")
        return

    assets[asset_id]["last_service"] = parsed_date.strftime("%Y-%m-%d")


def due_for_inspection(service_interval_days=SERVICE_INTERVAL_DAYS):
    """Return asset IDs whose last service exceeds the inspection interval."""
    if (
        not isinstance(service_interval_days, int)
        or isinstance(service_interval_days, bool)
        or service_interval_days <= 0
    ):
        raise ValueError("Service interval must be a positive integer.")

    due = []
    current_time = datetime.now()

    for asset_id, asset_details in assets.items():
        last_service = datetime.strptime(
            asset_details["last_service"], "%Y-%m-%d"
        )

        if current_time - last_service > timedelta(
            days=service_interval_days
        ):
            due.append(asset_id)

    return due


def change_interval(days):
    """Validate and return a service interval in days."""
    if not isinstance(days, int) or isinstance(days, bool) or days <= 0:
        raise ValueError("Service interval must be a positive integer.")

    return days


def export_service_report(file="maintenance.json"):
    """Export registered assets to a JSON service report."""
    with open(file, "w", encoding="utf-8") as report_file:
        json.dump(assets, report_file, indent=2)

    print(f"Report written to {file}")


def write_scratch_copy():
    """Write asset data to a securely created temporary JSON file."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        encoding="utf-8",
        delete=False,
    ) as scratch_file:
        json.dump(assets, scratch_file, indent=2)
        scratch_path = scratch_file.name

    print(f"Scratch copy at {scratch_path}")


def print_alerts(service_interval_days):
    """Print alerts for assets whose inspections are overdue."""
    for asset_id in due_for_inspection(service_interval_days):
        print(
            f"ALERT: inspection overdue for "
            f"{asset_id} {assets[asset_id]['type']}"
        )


def main():
    """Run a demonstration of the warehouse maintenance system."""
    register_asset("FL-01", "Forklift")
    register_asset("CV-07", "Conveyor")
    register_asset("PJ-03", "Pallet Jack")

    update_service_date("FL-01", "2025-01-15")
    update_service_date("XX-99", "2025-02-01")

    service_interval_days = change_interval(90)

    service_date = input(
        "Last service date for CV-07 (YYYY-MM-DD, Enter to skip): "
    )

    if service_date:
        update_service_date("CV-07", service_date)

    if not assets:
        raise RuntimeError("No assets are registered.")

    print_alerts(service_interval_days)
    export_service_report()
    write_scratch_copy()


if __name__ == "__main__":
    main()

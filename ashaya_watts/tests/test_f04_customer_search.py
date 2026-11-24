
"""Unit & Acceptance Tests for F-04 Customer Interface Search (Ashaya Watts)."""

import pytest


# TC-04.01: TS-1 [AC-1] - Positive
def test_ts1_search_filters_by_model(client):
    response = client.get("/api/public/vehicles?q=Corolla")

    assert response.status_code == 200

    vehicles = response.get_json()

    assert len(vehicles) > 0

    for vehicle in vehicles:
        assert "corolla" in vehicle["model"].lower()

    availability = [vehicle["availability"] for vehicle in vehicles]

    assert "Available Now" in availability
    assert "Upcoming Arrival" in availability


# TC-04.02: TS-1 [AC-1] - Positive
def test_ts1_search_filters_by_make_and_model(client):
    response = client.get("/api/public/vehicles?q=Honda")

    assert response.status_code == 200

    vehicles = response.get_json()

    assert len(vehicles) > 0

    for vehicle in vehicles:
        assert vehicle["make"].lower() == "honda"

    response = client.get("/api/public/vehicles?q=Honda+Civic")

    assert response.status_code == 200

    vehicles = response.get_json()

    assert len(vehicles) > 0

    for vehicle in vehicles:
        assert vehicle["make"].lower() == "honda"
        assert vehicle["model"].lower() == "civic"


# TC-04.03: TS-2 [AC-1] - Negative
def test_ts2_nonexistent_vehicle_search(client):
    response = client.get("/api/public/vehicles?q=XYZ123")

    assert response.status_code == 200
    assert response.get_json() == []

    # Check that the message appears on the customer page.
    response = client.get("/browse?q=XYZ123")

    assert response.status_code == 200
    assert b"No matching vehicles found" in response.data


# TC-04.04: TS-3 [AC-2] - Positive
def test_ts3_internal_financial_data_not_exposed(client):
    response = client.get("/api/public/vehicles?q=Corolla")

    assert response.status_code == 200

    vehicles = response.get_json()

    assert len(vehicles) > 0

    upcoming = [
        vehicle for vehicle in vehicles
        if vehicle["availability"] == "Upcoming Arrival"
    ]

    assert len(upcoming) > 0

    for vehicle in upcoming:
        assert vehicle["estimated_arrival"] is not None

    # Check that restricted information is not returned.
    for vehicle in vehicles:
        assert "base_foreign_price" not in vehicle
        assert "base_currency" not in vehicle
        assert "bill_of_lading" not in vehicle
        assert "deposit_paid" not in vehicle
        assert "internal_purchasing_cost" not in vehicle


# TC-04.05: TS-4 [AC-2] - Negative
def test_ts4_restricted_financial_data_access(client):
    # Attempt to request restricted fields through the public API.
    response = client.get(
        "/api/public/vehicles?q=Corolla"
        "&fields=base_foreign_price,base_currency,bill_of_lading"
    )

    assert response.status_code == 200

    vehicles = response.get_json()

    assert len(vehicles) > 0

    for vehicle in vehicles:
        assert "base_foreign_price" not in vehicle
        assert "base_currency" not in vehicle
        assert "bill_of_lading" not in vehicle
        assert "deposit_paid" not in vehicle
        assert "internal_purchasing_cost" not in vehicle

        # Check that the public detail page also hides restricted fields.
        detail = client.get(f"/vehicle/{vehicle['id']}")

        assert detail.status_code == 200
        assert b"base_foreign_price" not in detail.data
        assert b"Internal Purchasing Cost" not in detail.data

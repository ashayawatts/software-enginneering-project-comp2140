"""Unit & Acceptance Tests for F-01 Shipment and Inventory Tracking (Randre Fearon)."""

import pytest


@pytest.mark.skip(reason="TODO (Randre): Implement TS-1 [AC-1] valid Bill of Lading lookup")
def test_ts1_valid_bol_retrieves_status_and_eta():
    pass


@pytest.mark.skip(reason="TODO (Randre): Implement TS-2 [AC-1] invalid/non-existent BoL error handling")
def test_ts2_invalid_bol_handled_gracefully():
    pass


@pytest.mark.skip(reason="TODO (Randre): Implement TS-3 [AC-2] delayed shipment visibly highlighted")
def test_ts3_delayed_status_is_highlighted():
    pass

"""
tests.py
Unit tests for file.py (battery sizing script).
These will FAIL if the sizing result is wrong.
"""

import math

# Expected reference values from the project spec
EXPECTED_DAILY_LOAD = 576.0  # Wh
EXPECTED_NET_DAILY = EXPECTED_DAILY_LOAD / (1 - 0.05)  # ≈ 606.3 Wh
EXPECTED_BATTERY_WH = EXPECTED_NET_DAILY * 3          # ≈ 1818.9 Wh
EXPECTED_BATTERY_AH = EXPECTED_BATTERY_WH / 48        # ≈ 37.9 Ah

# Tolerances (allow ±1 Wh or ±0.1 Ah rounding)
TOL_WH = 1.0
TOL_AH = 0.1

def test_daily_load_energy():
    """Daily load must equal 576 Wh (±1)."""
    from file import energy_per_day
    assert math.isclose(energy_per_day, EXPECTED_DAILY_LOAD, abs_tol=TOL_WH), \
        f"Expected {EXPECTED_DAILY_LOAD}, got {energy_per_day}"

def test_net_daily_energy():
    """Net energy with 5% loss must equal ≈606.3 Wh/day (±1)."""
    from file import net_energy_per_day
    assert math.isclose(net_energy_per_day, EXPECTED_NET_DAILY, abs_tol=TOL_WH), \
        f"Expected {EXPECTED_NET_DAILY}, got {net_energy_per_day}"

def test_battery_wh_and_ah():
    """Battery sizing must be ≈1819 Wh and ≈37.9 Ah (tolerances)."""
    from file import battery_required_Wh
    calc_Ah = battery_required_Wh / 48
    assert math.isclose(battery_required_Wh, EXPECTED_BATTERY_WH, abs_tol=TOL_WH), \
        f"Expected {EXPECTED_BATTERY_WH}, got {battery_required_Wh}"
    assert math.isclose(calc_Ah, EXPECTED_BATTERY_AH, abs_tol=TOL_AH), \
        f"Expected {EXPECTED_BATTERY_AH}, got {calc_Ah}"

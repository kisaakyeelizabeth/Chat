# Ensure required packages are available (for Pyodide / micropip environments)
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import micropip
    import asyncio
    async def install_and_import():
        await micropip.install(["numpy", "matplotlib"])
        globals()["np"] = __import__("numpy")
        import matplotlib.pyplot as plt
        globals()["plt"] = plt
    asyncio.get_event_loop().run_until_complete(install_and_import())
#!/usr/bin/env python3
"""
file.py
Solar battery pack sizing for a 48V IoT node with 3-day autonomy.

Steps:
1. Define hourly load profile (24 values, in Watts).
2. Scale profile to 576 Wh/day average consumption.
3. Apply 5% cable loss.
4. Compute battery Wh required for 3 days autonomy.
5. Plot load profile vs battery discharge over 3 days.
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Step 1: Define hourly load profile (Watts)
# Example profile: base load + peaks during day
base_load = 10  # W
profile = np.array([
    5, 5, 5, 5,    # midnight - 4am low activity
    8, 10, 15, 20, # 4-8am wakeup / comms
    25, 30, 30, 25,# 8am-12pm peak sensing
    20, 15, 15, 20,# afternoon moderate
    25, 30, 20, 15,# evening high
    10, 8, 6, 5    # late night
])

# ----------------------------
# Step 2: Scale to 576 Wh/day
hours = np.arange(24)
energy_per_day_raw = profile.sum()  # Wh since each entry is W*1h
scaling = 576.0 / energy_per_day_raw
profile = profile * scaling
energy_per_day = profile.sum()

# ----------------------------
# Step 3: Apply 5% cable loss
net_energy_per_day = energy_per_day / (1 - 0.05)

# ----------------------------
# Step 4: Compute battery size
days_autonomy = 3
battery_required_Wh = net_energy_per_day * days_autonomy

# ----------------------------
# Step 5: Simulate battery discharge
# Assume fully charged battery at start (capacity = battery_required_Wh)
battery_capacity = battery_required_Wh
soc = [battery_capacity]  # state of charge
timeline_load = np.tile(profile, days_autonomy)  # 3 days load sequence

for load in timeline_load:
    soc.append(soc[-1] - load / (1 - 0.05))  # include cable loss

soc = np.array(soc)

# ----------------------------
# Results
print("=== Battery Sizing Result ===")
print(f"Daily energy demand (at load): {energy_per_day:.2f} Wh")
print(f"Net energy demand (with 5% cable loss): {net_energy_per_day:.2f} Wh/day")
print(f"Battery required for {days_autonomy} days autonomy: {battery_required_Wh:.2f} Wh")
print(f"Equivalent at 48 V: {battery_required_Wh/48:.2f} Ah")

# ----------------------------
# Step 6: Plot
fig, ax1 = plt.subplots(figsize=(10,6))

# Plot load profile for one day
ax1.bar(hours, profile, color='tab:blue', alpha=0.6, label="Hourly Load (W)")
ax1.set_xlabel("Hour of Day")
ax1.set_ylabel("Load Power (W)", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xticks(range(0,24,2))

# Twin axis for battery SOC
ax2 = ax1.twinx()
ax2.plot(np.arange(len(soc)), soc, color='tab:red', linewidth=2, label="Battery State of Charge (Wh)")
ax2.set_ylabel("Battery SoC (Wh)", color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title("Load Profile vs Battery Discharge over 3 Days Autonomy")
fig.tight_layout()
plt.show()

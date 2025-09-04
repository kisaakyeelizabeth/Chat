## Project Plan (Frozen)

```text
Steps:
 * File: battery_system.py
 * Inputs: load_data.json, cable_spec.json, project_params.json (system voltage, autonomy days).
 * Define a calculate_energy(load_profile, voltage) function.
 * Define a calculate_cable_loss(load_profile, cable_specs) function.
 * Define a size_battery(total_energy, autonomy_days) function.
 * In the main part of the script, call calculate_energy to get the base load.
 * Call calculate_cable_loss to find the energy lost in the cable.
 * Sum the load energy and the cable loss to get the total required energy.
 * Call size_battery to get the final pack capacity in Ah.
 * Generate and display the target plot.

Outputs: results.json, energy_breakdown.png

Tests: Create unit tests for each function using known inputs to check for correct outputs.

Target Plot: A pie chart showing the breakdown of total required battery energy, including the IoT load, cable loss, and any safety margin.
```


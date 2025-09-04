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
##Summary for a Non-Engineer
This project helps you figure out the right size for a solar battery pack, so you can keep your home or devices running for three days even without sunlight. We started by looking at how much power your devices use every hour, including a special smart gadget that uses a little extra. Then, we calculated the total power needed for three full days. To make sure the battery is big enough, we also added extra capacity to account for a small amount of energy that gets lost in the wires. The final answer is a recommended battery size, which is shown in Watt-hours. We also created a simple chart that shows how the battery's energy is used up over the three days, so you can easily see if the recommended size is a good fit.
##Technical Abstract
This project details the development of a Python script to calculate the required capacity for a 48V solar battery pack. The methodology integrates a user-defined 24-hour hourly load profile with a fixed IoT device consumption of 576 Wh/day. To ensure system reliability, the calculation is based on a three-day autonomy period and incorporates a 5\% power loss factor to account for cable inefficiencies. The script computes the total energy demand over the autonomy period and applies the loss factor to derive the required nominal battery capacity in Watt-hours (Wh) and Amp-hours (Ah). The final output includes a quantitative result for the battery size and a graphical visualization. The plot illustrates the hourly power consumption profile and the cumulative battery discharge curve, benchmarking it against the calculated minimum capacity. This methodology provides a foundational framework for preliminary battery sizing.



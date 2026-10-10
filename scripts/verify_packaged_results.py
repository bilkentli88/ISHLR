from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "results" / "paper"

def close(a, b, tol=1e-10):
    return abs(float(a) - float(b)) <= tol

# Synthetic compact-vs-explicit validation.
g = json.loads((PAPER/"global_compatibility"/"global_compatibility_summary.json").read_text())
assert g["leaves"] == 16
assert g["internal_nodes"] == 12
assert g["trajectory_flow_variables"] == 170
assert g["compact_leaf_variables"] == 16
assert g["compact_inequalities"] == 135
assert g["max_full_vs_compact_leaf_endpoint_difference"] < 1e-12
assert g["max_full_vs_compact_random_objective_difference"] < 1e-12
assert close(g["mean_hierarchy_only_width"], 0.31963059267737526)
assert close(g["mean_last_horizon_width"], 0.11484074798142302)
assert close(g["mean_all_horizon_width"], 0.10966039454569984)
assert g["largest_scaling_leaves"] == 256
assert g["largest_scaling_inequalities"] == 12512

# General-tree theorem/stress-test record.
t = json.loads((PAPER/"general_tree"/"general_tree_theorem_gate_summary.json").read_text())
assert t["random_tree_fixtures"] == 24
assert t["total_random_support_objectives"] == 240
assert t["global_max_full_vs_compact_support_difference"] < 1e-12
assert t["global_max_constructive_coupling_residual"] < 1e-12
assert t["changing_selection_strictly_tightened_leaves"] == 12
assert t["changing_selection_nonredundant_earlier_constraints"] == 4

# Sample-analogue record.
s = json.loads((PAPER/"sample_analog"/"sample_analog_consistency_gate_summary.json").read_text())
assert close(s["endpoint_error_loglog_slope"], -0.45241227895202746)
assert close(s["endpoint_error_reduction_small_to_large_n"], 0.7481284972243707)
assert close(s["largest_n_raw_lp_feasibility"], 1.0)
assert close(s["largest_n_p90_eta_hat"], 0.0)

# Archived manuscript real-data record (no live API calls).
r = json.loads((PAPER/"real_data"/"reported_real_data_summary.json").read_text())
assert r["analysis_configuration"]["observation_created_window"] == {"start": "2022-01-01", "end": "2024-12-31"}
assert r["analysis_configuration"]["max_genera"] == 8
assert r["analysis_configuration"]["max_species_per_genus"] == 5
assert r["analysis_configuration"]["min_observations_per_species"] == 15
assert r["initial_coarse_start_cohort"] == {"observations": 695, "species": 22, "genera": 8}
assert r["cleaned_cohort"] == {"observations": 639, "species": 21, "genera": 8, "compatible_event_rate": 0.979895, "withdrawn_event_rate": 0.041958}
assert close(r["raw_feasibility_thresholds"]["cleaned_all_horizons"], 9.532272)
assert close(r["raw_feasibility_thresholds"]["cleaned_final_horizon"], 1.0)
assert close(r["hierarchy_only_mean_width"], 0.00871898)

p12 = r["sensitivity_path"]["12"]
assert p12["raw_feasible_full_history"] is True
assert close(p12["eta_all"], 0.0)
assert close(p12["all_mean_width"], 0.00404156)
assert close(p12["final_mean_width_common_relaxation"], 0.00563621)
assert close(p12["tightening_vs_hierarchy"], 0.536)
assert close(p12["tightening_vs_final"], 0.283)

p6 = r["sensitivity_path"]["6"]
assert p6["raw_feasible_full_history"] is False
assert close(p6["eta_all"], 0.000149707)
assert close(p6["all_mean_width"], 0.00349597)
assert close(p6["final_mean_width_common_relaxation"], 0.00566301)

rob = r["unfiltered_robustness_at_gamma12"]
assert rob["observations"] == 695 and rob["species"] == 22 and rob["genera"] == 8
assert rob["raw_feasible"] is True
assert close(rob["gamma_min_all_reported_approx"], 10.22)
assert close(rob["tightening_vs_hierarchy"], 0.453)
assert close(rob["tightening_vs_final"], 0.097)
assert rob["strictly_tightened_species"] == 21
assert rob["unchanged_species"] == "Larus smithsonianus"

with (PAPER/"real_data"/"reported_sensitivity_table.csv").open(newline="") as f:
    table = {int(row["gamma"]): row for row in csv.DictReader(f)}
assert table[12]["raw_feasible_full_history"] == "Yes"
assert table[6]["raw_feasible_full_history"] == "No"
assert table[8]["raw_feasible_full_history"] == "No"
assert table[20]["raw_feasible_full_history"] == "Yes"

assert (PAPER/"real_data"/"reported_sensitivity_path.pdf").exists()
assert (PAPER/"real_data"/"reported_sensitivity_path.png").exists()

print("All packaged paper-result checks passed.")

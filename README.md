# Informatively Stopped Hierarchical Label Refinement

Reproducibility package for the manuscript **“Informatively Stopped Hierarchical Label Refinement: Sharp Identification and Sensitivity Analysis.”**

The repository contains the theory-development notebooks, paper-level synthetic validation notebooks and outputs, the sample-analogue experiment, and an executable iNaturalist trajectory-reconstruction pipeline together with an archived record of the manuscript real-data results.

## Repository structure

```text
notebooks/
  development/
    01_theory_gate.ipynb
    02_method_gate.ipynb
  paper/
    03_global_compatibility_gate.ipynb
    04_general_tree_theorem_gate.ipynb
    05_sample_analog_consistency_gate.ipynb
    06_inaturalist_cleaned_reproduction.ipynb
results/
  development/
  paper/
    global_compatibility/
    general_tree/
    sample_analog/
    real_data/
    paper_reported_metrics.json
scripts/
  verify_packaged_results.py
requirements.txt
```

## Main paper-level validation

`03_global_compatibility_gate.ipynb` reproduces the primary 16-leaf / 12-internal-node fixture used for the compact-vs-explicit comparison. In the packaged rerun it yields 170 explicit trajectory-flow variables, 16 compact leaf variables, 135 affine inequalities, numerical agreement of compact and explicit endpoints, and the hierarchy/final/all mean widths used in the manuscript. It also includes the scaling fixture up to 256 leaves.

`04_general_tree_theorem_gate.ipynb` stress-tests the projection result across 24 additional rooted trees and 240 random linear objectives, constructs compatible couplings, and audits temporal nonredundancy.

`05_sample_analog_consistency_gate.ipynb` reproduces the finite-sample sample-analogue experiment with sample sizes 250 through 5000. The packaged rerun gives the manuscript endpoint-error log-log slope (`-0.4524`), the 74.81% endpoint-error reduction, 100% raw feasibility at the largest sample size, and zero 90th-percentile minimum relaxation there.

## Real-data analysis

`06_inaturalist_cleaned_reproduction.ipynb` is aligned with the final manuscript analysis:

- target taxon: Aves;
- observation-created window: 2022-01-01 through 2024-12-31;
- candidate metadata pool: 4000 observations;
- induced hierarchy: up to eight genera and five species per genus, with at least 15 candidate observations per species and at least two eligible species per genus;
- coarse start: the first compatible, non-withdrawn identification must have rank genus/family/order/class and defines time zero;
- horizons: 0/1/7/30/90 days;
- trajectory: deepest compatible state reached so far (monotone compatible envelope);
- quality audit: exclude a species when compatible-event rate is below 85% or withdrawn-event rate exceeds 20%;
- sensitivity grid: Gamma = 6/8/12/20;
- principal unrelaxed setting: Gamma = 12;
- raw-feasibility threshold search for both all-horizon and final-horizon systems;
- unfiltered-cohort robustness analysis at Gamma = 12.

The temporal comparison uses the **same full-history minimum relaxation** for the all-horizon and final-horizon models at settings requiring relaxation.

Because iNaturalist is a live service, the exact historical API snapshot is not embedded. `results/paper/real_data/` therefore stores the validated values reported in the manuscript. The principal cleaned-cohort result at `Gamma=12` uses no relaxation and reduces mean species-level identified width by 53.6% relative to hierarchy-only information and by 28.3% relative to the final horizon. The archived full-history raw-feasibility threshold is approximately `9.53` (`9.532272` in the numerical search record), while the final-horizon threshold is `1`. The 695-observation robustness analysis remains raw-feasible at `Gamma=12` and retains positive temporal tightening.

## Quick verification

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Check the packaged result files:

```bash
python scripts/verify_packaged_results.py
```

The synthetic notebooks are CPU-only and can be rerun locally or in Google Colab. The iNaturalist notebook requires internet access to the public iNaturalist API. The verification script does **not** call the live API; it checks the packaged synthetic outputs and the archived manuscript real-data record.

## Reproducibility status

The synthetic paper-level notebooks were rerun successfully when the package was assembled; their generated CSV/JSON/PNG outputs are included under `results/paper/`. The iNaturalist analysis uses a live external service, so the repository separates the executable reconstruction notebook from the immutable manuscript result record. This avoids presenting a future live-API rerun as though it were the historical analysis snapshot.

## License

This repository is released under the MIT License. See `LICENSE`.

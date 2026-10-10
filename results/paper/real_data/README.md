# Real-data manuscript record

This directory stores the **validated values reported in the manuscript** for the iNaturalist study. These files are an audit record, not a frozen copy of the underlying iNaturalist API responses.

The source is live: identifications can be withdrawn or added, current taxon assignments can change, and taxonomy mappings can be revised. Consequently, a future run of `notebooks/paper/06_inaturalist_cleaned_reproduction.ipynb` may not reproduce the historical cohort exactly.

## Files

- `analysis_configuration.json` records the final cohort-construction and sensitivity-analysis settings used by the manuscript.
- `reported_species_resolution.csv` corresponds to manuscript Table 4.
- `reported_sensitivity_table.csv` corresponds to manuscript Table 5 and now also records raw feasibility and mean widths used for the sensitivity-path figure. Widths marked approximate were retained only at the precision available from the archived analysis/figure record.
- `reported_real_data_summary.json` is the consolidated manuscript audit record: initial and cleaned cohorts, quality audit, raw-feasibility thresholds, the full sensitivity path, and the unfiltered robustness analysis.
- `reported_unfiltered_robustness.json` isolates the 695-observation robustness result at `Gamma=12`.
- `reported_sensitivity_path.pdf` and `.png` reproduce the manuscript sensitivity-path figure from the validated run.

## Final analysis definition

The manuscript uses Aves observations created from 2022-01-01 through 2024-12-31. The current species assignment defines the root-to-species reference lineage. Withdrawn and outside-lineage identifications are retained for auditing but are not trajectory states. Only observations whose first compatible, non-withdrawn identification is genuinely coarse (genus/family/order/class) enter the coarse-start cohort, and that event defines time zero. The reconstructed state at each later horizon is the deepest compatible node reached so far: a **monotone compatible envelope**, not a reconstruction of the platform's historical consensus taxon.

The cleaned manuscript cohort contains 639 observations from 21 species and eight genera. The principal unrelaxed analysis is `Gamma=12`; the archived full-history raw-feasibility threshold is approximately `9.53` (numerical search record `9.532272`), while the final-horizon threshold is `1`. The unfiltered 695-observation robustness analysis has a full-history threshold of approximately `10.22` and remains raw-feasible at `Gamma=12`.

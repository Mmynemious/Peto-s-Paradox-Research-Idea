# Peto’s Paradox–Inspired p53 Stabilizer Design
Computational Docking of a De Novo Peptide Binder to MDM2

# Project Overview
Elephants (Loxodonta africana) exhibit remarkably low cancer incidence despite their large body size and long lifespan — a phenomenon known as Peto’s Paradox. One proposed explanation is their expanded repertoire of TP53 retrogenes, which enhance apoptotic responses under DNA damage.

In humans, the tumor suppressor protein p53 is negatively regulated by MDM2, which binds to the N-terminal p53 transactivation domain and targets it for degradation. Disrupting the p53–MDM2 interaction is therefore a well-established anti-cancer strategy.

This project explores whether a short, de novo–designed peptide, conceptually inspired by p53-like stabilizing mechanisms, can bind to the canonical MDM2 p53-binding cleft, using in-silico structure prediction and docking.

This is a computational feasibility study, not a therapeutic claim.

# Workflow Summary

- Select MDM2–p53 structural reference
- Design a short peptide candidate
- Predict peptide structure with AlphaFold2
- Manually position peptide near MDM2 binding site
- Perform blind protein–peptide docking with ZDOCK
- Inspect top docking poses for biologically relevant binding

# Step-by-Step Methodology
# 1. Structural Reference Selection

- Target protein: Human MDM2
- Reference complex: MDM2 bound to p53 N-terminal peptide
- PDB ID: 1YCR
- Source:
https://www.rcsb.org/structure/1YCR

This structure defines the canonical p53-binding pocket on MDM2 (key residues include Leu54, Ile61, Phe91, Val93).

# 2. Peptide Design

A short peptide (~13 amino acids) was designed conceptually to act as a p53 stabilizer, inspired by the idea of enhanced p53 activity (not direct sequence copying from elephant TP53 retrogenes).

The peptide is treated as a novel binder, not a known biological sequence.

# 3. Peptide Structure Prediction

Tool: AlphaFold2 via ColabFold
https://github.com/sokrypton/ColabFold

Settings:
- Single-sequence mode (no MSA)
- No templates
- AlphaFold2-ptm models
- Best model selected by pLDDT

Output:
- p53stabiliser_26e09_unrelaxed_rank_001_*.pdb

# 4. Structural Preparation in PyMOL

- Software: PyMOL
- https://pymol.org/

Steps performed:

- Loaded MDM2 structure (1YCR.cif)
- Loaded predicted peptide structure
- Identified chains:

MDM2 → chain A

Peptide → chain B

- Roughly positioned peptide near the known p53-binding cleft
- Saved separate files for docking:

mdm2_for_docking.pdb
peptide_positioned_for_docking.pdb


This positioning was not treated as a final pose, only as a reasonable starting geometry.

# 5. Protein–Peptide Docking

Docking server: ZDOCK
https://zdock.wenglab.org/

Settings:
- Model: ZDOCK 3.0.2
- Docking mode: Protein–Protein (used for peptide)
- Residue constraints: None (blind docking)
- Receptor: MDM2
- Ligand: Peptide
- Rationale:

Blind docking avoids bias when no experimentally validated interface constraints are available.

The goal is to test whether the peptide naturally prefers the p53 pocket.

Outputs downloaded:
- Receptor PDB
- Ligand PDB
- Top 10 docked complex predictions

# 6. Docking Analysis

- Analysis tool: PyMOL
- For each of the top-ranked ZDOCK models:
- Inspected peptide binding location
- Checked proximity to canonical p53-binding residues on MDM2
- Evaluated whether binding occurred:

inside the p53 hydrophobic cleft (desired) or elsewhere on the protein surface

This qualitative structural inspection determines whether the peptide is a plausible MDM2 binder worth further refinement.

# Current Status

✅ Peptide successfully folded with AlphaFold2

✅ Docked against MDM2 using ZDOCK

🔍 Binding pose analysis in progress

No binding affinity calculations or molecular dynamics simulations have been performed yet.

Limitations
- No experimental validation
- No binding free-energy calculations
- Blind docking only (no hotspot constraints)
- Single peptide candidate tested
- This work is exploratory and hypothesis-generating.

**Potential Next Steps**

- Rosetta FlexPepDock refinement
- Binding affinity estimation (MM/GBSA, FoldX)
- Peptide sequence optimization
- Comparison against known MDM2 inhibitors
- Molecular dynamics simulations

**Disclaimer**

This project is for educational and research purposes only.
It does not propose a validated therapeutic intervention.

🧬 Protein Binding Prediction Toolkit
A lightweight, modular Python framework for exploring protein–protein and protein–peptide interactions.

This project provides two complementary pipelines:

3D-based interface scoring (using PDB structures)

NLP-based sequence embeddings (using ProtBERT)

Both pipelines share the same philosophy:
simple, interpretable, modular, and easy to extend.

📁 Project Structure
Code
protein_binding/
│
├── io.py                 # Load PDB structures
├── features.py           # Extract interface residues
├── models.py             # Simple 3D scoring model
├── sampling.py           # Pose generation (placeholder)
├── pipeline.py           # 3D end-to-end pipeline
│
├── nlp_embeddings.py     # ProtBERT embeddings for sequences
├── nlp_models.py         # Simple NLP-based interaction model
├── nlp_pipeline.py       # Sequence-only prediction pipeline
│
├── run.py                # Run 3D pipeline
└── run_nlp.py            # Run NLP pipeline
🚀 Quickstart
Install dependencies
bash
pip install torch transformers biopython scikit-learn
🧩 1. 3D Pipeline (PDB-based)
This pipeline:

Loads a protein complex from a PDB file

Identifies interface residues

Scores the interface using a simple heuristic

Ranks poses (if multiple are generated)

Run it:

bash
python run.py
You can modify run.py to point to your own PDB file:

python
pdb_path = "examples/mdm2_peptide_complex.pdb"
🧬 2. NLP Pipeline (Sequence-based)
This pipeline uses ProtBERT to embed protein sequences as vectors and computes an interaction probability using cosine similarity.

Run it:

bash
python run_nlp.py
Example inside run_nlp.py:

python
seq_a = "MSEQNNTEMTFQIQRIYTKDISFEAPNAPHVFQKDW"
seq_b = "GSDVVVQTPVQENYQKSVR"
Output:

Code
NLP-based protein–protein interaction prediction
------------------------------------------------
Interaction probability: 0.742
🧠 Why Two Pipelines?
3D pipeline → useful when you have structures (PDBs, docking outputs, AlphaFold models)

NLP pipeline → useful when you only have sequences or want fast screening

You can combine both later into a hybrid model.

🛠️ Extending the Toolkit
This architecture is intentionally modular:

Replace simple_interface_score() with a learned model

Add real docking to sampling.py

Train a classifier in nlp_models.py

Add batch jobs for Lyceum Cloud

Integrate Rosetta/FlexPepDock outputs

Everything is plug-and-play.

📌 Notes
ProtBERT loads once and stays cached for fast inference

GPU acceleration is automatic if available

No external docking tools are required to get started

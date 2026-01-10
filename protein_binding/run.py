from pipeline import run_binding_pipeline

if __name__ == "__main__":
    pdb_path = "examples/mdm2_peptide_complex.pdb"
    results = run_binding_pipeline(pdb_path, chain_a="A", chain_b="B",
                                   n_poses=32, top_k=5)

    for score, idx, pose in results:
        print(f"Pose {idx} score = {score:.3f}")

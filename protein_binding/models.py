import numpy as np

AA_HYDROPHOBIC = set(["A", "V", "I", "L", "M", "F", "Y", "W"])

def simple_interface_score(interface_residues):
    # Very rough: reward hydrophobic contacts, penalize buried charges, etc.
    score = 0.0
    for res in interface_residues:
        resname = res.get_resname().strip()
        if resname in AA_HYDROPHOBIC:
            score -= 1.0  # lower is “better”
    return score

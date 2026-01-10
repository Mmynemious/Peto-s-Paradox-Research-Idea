import numpy as np

def get_interface_residues(structure, chain_id_a, chain_id_b, cutoff=8.0):
    chain_a = structure[0][chain_id_a]
    chain_b = structure[0][chain_id_b]

    interface = set()
    for res_a in chain_a:
        if not res_a.has_id("CA"):
            continue
        ca_a = res_a["CA"].coord
        for res_b in chain_b:
            if not res_b.has_id("CA"):
                continue
            ca_b = res_b["CA"].coord
            if np.linalg.norm(ca_a - ca_b) <= cutoff:
                interface.add(res_a)
                interface.add(res_b)
    return list(interface)

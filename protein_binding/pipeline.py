from io import load_structure
from features import get_interface_residues
from models import simple_interface_score
from sampling import generate_poses

def run_binding_pipeline(pdb_path, chain_a, chain_b, n_poses=32, top_k=5):
    base_structure = load_structure(pdb_path)
    poses = generate_poses(base_structure, n_poses=n_poses)

    scored = []
    for i, pose in enumerate(poses):
        interface = get_interface_residues(pose, chain_a, chain_b)
        score = simple_interface_score(interface)
        scored.append((score, i, pose))

    scored.sort(key=lambda x: x[0])  # lower is better
    return scored[:top_k]

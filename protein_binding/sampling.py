def generate_poses(initial_structure, n_poses=32):
    # TODO: integrate with a real docking engine or use random rigid-body moves
    # For now, return the same structure as a trivial baseline
    return [initial_structure] * n_poses

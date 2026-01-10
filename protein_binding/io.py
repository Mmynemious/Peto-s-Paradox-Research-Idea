from Bio.PDB import PDBParser

def load_structure(pdb_path, structure_id="prot"):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(structure_id, pdb_path)
    return structure

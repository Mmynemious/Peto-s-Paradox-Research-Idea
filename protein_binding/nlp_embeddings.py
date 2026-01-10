# nlp_embeddings.py

from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

# Load once at module import (cheap amortized, but does cost RAM)
_MODEL_NAME = "Rostlab/prot_bert"

_tokenizer = None
_model = None
_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _load_model():
    global _tokenizer, _model
    if _tokenizer is None or _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(_MODEL_NAME, do_lower_case=False)
        _model = AutoModel.from_pretrained(_MODEL_NAME)
        _model.to(_device)
        _model.eval()


def embed_sequence(seq: str) -> np.ndarray:
    """
    Turn an amino acid sequence into a fixed-size embedding vector.
    """
    _load_model()

    # ProtBERT expects spaces between residues: "M S E Q ..."
    seq = seq.replace(" ", "").upper()
    spaced = " ".join(list(seq))

    tokens = _tokenizer(spaced, return_tensors="pt")
    tokens = {k: v.to(_device) for k, v in tokens.items()}

    with torch.no_grad():
        output = _model(**tokens)

    # Mean-pool over sequence length dimension -> [hidden_size]
    embedding = output.last_hidden_state.mean(dim=1).squeeze(0)
    return embedding.detach().cpu().numpy()

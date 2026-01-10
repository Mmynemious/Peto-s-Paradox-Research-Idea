# nlp_pipeline.py

from typing import Dict
from nlp_embeddings import embed_sequence
from nlp_models import SimpleNLPInteractionModel


def predict_interaction_from_sequences(
    seq_a: str,
    seq_b: str,
    model: SimpleNLPInteractionModel | None = None,
) -> Dict[str, float]:
    """
    High-level NLP-only interaction prediction from two protein sequences.
    """
    if model is None:
        model = SimpleNLPInteractionModel()

    emb_a = embed_sequence(seq_a)
    emb_b = embed_sequence(seq_b)

    prob = model.predict_interaction_probability(emb_a, emb_b)

    return {
        "interaction_probability": float(prob),
    }

# nlp_models.py

import numpy as np
from dataclasses import dataclass
from typing import Tuple


@dataclass
class SimpleNLPInteractionModel:
    """
    Minimal, hand-crafted 'model' using embeddings only.
    Replace this later with a trained classifier if you want.
    """

    def _featurize_pair(self, emb1: np.ndarray, emb2: np.ndarray) -> np.ndarray:
        # Basic interaction features: concat, diff, elementwise product
        return np.concatenate([emb1, emb2, emb1 - emb2, emb1 * emb2])

    def score_pair(self, emb1: np.ndarray, emb2: np.ndarray) -> float:
        """
        Returns a pseudo 'interaction score' in [0, 1] range.
        For now: use cosine similarity as a proxy, mapped to [0, 1].
        """
        a = emb1 / (np.linalg.norm(emb1) + 1e-8)
        b = emb2 / (np.linalg.norm(emb2) + 1e-8)
        cos_sim = float(np.dot(a, b))
        # Map from [-1, 1] to [0, 1]
        return (cos_sim + 1.0) / 2.0

    def predict_interaction_probability(
        self, emb1: np.ndarray, emb2: np.ndarray
    ) -> float:
        return self.score_pair(emb1, emb2)

# run_nlp.py

from nlp_pipeline import predict_interaction_from_sequences


if __name__ == "__main__":
    # Example sequences – replace with your real proteins
    seq_a = "MSEQNNTEMTFQIQRIYTKDISFEAPNAPHVFQKDW"
    seq_b = "GSDVVVQTPVQENYQKSVR"

    result = predict_interaction_from_sequences(seq_a, seq_b)

    print("NLP-based protein–protein interaction prediction")
    print("------------------------------------------------")
    print(f"Interaction probability (0–1): {result['interaction_probability']:.3f}")

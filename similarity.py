import sys
import numpy as np

from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

def read_pairs() -> tuple[list[str],list[str]]:
    first, second = list(), list()
    for line in sys.stdin:
        line = line.strip()
        try:
            f, s = line.split("[SEP]")
            first.append(f)
            second.append(s)
        except ValueError:
            print(f"Warning: Malformed line '{line}' skipped...", file=sys.stderr)
    return first, second
    
def encode_sentences(model: SentenceTransformer, sentences:list[str]) -> np.ndarray:
    return model.encode(sentences)

def main():
    first, second = read_pairs()
    model = SentenceTransformer("bert-base-nli-mean-tokens")
    first_enc = encode_sentences(model, first)
    second_enc = encode_sentences(model, second)
    for f_enc, s_enc in zip(first_enc, second_enc):
        print(cosine(f_enc, s_enc))


if __name__ == "__main__":
    main()

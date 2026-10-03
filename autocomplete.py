import re


def tokenize(text: str) -> list[str]:
    """Cleans raw text and splits it into lowercase word tokens."""
    # Convert to lowercase
    text = text.lower()

    # Match word sequences of alphanumeric characters and apostrophes (e.g., don't)
    tokens = re.findall(r"\b[a-z0-9']+\b", text)
    return tokens


def load_corpus(filepath: str) -> list[str]:
    """Reads a text file and returns a list of tokens."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return tokenize(content)

def extract_bigrams(tokens: list[str]) -> list[tuple[str, str]]:
    """Generates consecutive word pairs (w1, w2) from a list of tokens."""
    return list(zip(tokens[:-1], tokens[1:]))

if __name__ == "__main__":
    # Test reading and tokenizing our corpus
    tokens = load_corpus("corpus.txt")
    print(f"Total tokens loaded: {len(tokens)}")
#    print(f"First 15 tokens: {tokens[:15]}")

    bigrams = extract_bigrams(tokens)
    print(f"Total bigrams generated: {len(bigrams)}")
    print(f"First 5 bigrams: {bigrams[:5]}")
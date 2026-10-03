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


if __name__ == "__main__":
    # Test reading and tokenizing our corpus
    tokens = load_corpus("corpus.txt")
    print(f"Total tokens loaded: {len(tokens)}")
    print(f"First 15 tokens: {tokens[:15]}")
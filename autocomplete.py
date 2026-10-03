from collections import Counter, defaultdict
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

def build_model(
    bigrams: list[tuple[str, str]],
) -> defaultdict[str, Counter[str]]:
    """Builds a lookup table mapping each word to the counts of words that follow it."""
    model = defaultdict(Counter)
    for w1, w2 in bigrams:
        model[w1][w2] += 1
    return model


if __name__ == "__main__":
    # Test reading and tokenizing our corpus
    tokens = load_corpus("corpus.txt")
#    print(f"Total tokens loaded: {len(tokens)}")
#    print(f"First 15 tokens: {tokens[:15]}")

    bigrams = extract_bigrams(tokens)
#    print(f"Total bigrams generated: {len(bigrams)}")
#    print(f"First 5 bigrams: {bigrams[:5]}")

    model = build_model(bigrams)

    # Let's inspect what follows a common word like 'the' or 'of'
    test_word = "the"
    print(
        f"Top 5 words that follow '{test_word}': {model[test_word].most_common(5)}"
    )

    test_word_2 = "gift"
    print(
        f"Top 5 words that follow '{test_word_2}': {model[test_word_2].most_common(5)}"
    )
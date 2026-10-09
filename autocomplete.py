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

def predict_next(
    model: defaultdict[str, Counter[str]],
    current_word: str,
    prefix: str = "",
    top_k: int = 3,
) -> list[tuple[str, int]]:
    """Suggests the top_k most likely next words given current_word,

    optionally filtered by a starting letter/prefix.
    """
    current_word = current_word.lower().strip()
    prefix = prefix.lower().strip()

    # If the word was never seen in our training corpus, we cannot predict
    if current_word not in model:
        return []

    followers = model[current_word]

    # Case 1: The user started typing the next word (filter by prefix)
    if prefix:
        matches = [
            (word, count)
            for word, count in followers.items()
            if word.startswith(prefix)
        ]
        # Sort descending by count
        matches.sort(key=lambda pair: pair[1], reverse=True)
        return matches[:top_k]

    # Case 2: No prefix, return the most common following words
    return followers.most_common(top_k)

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
#    test_word = "the"
#    print(
#        f"Top 5 words that follow '{test_word}': {model[test_word].most_common(5)}"
#    )

#    test_word_2 = "gift"
#    print(
#        f"Top 5 words that follow '{test_word_2}': {model[test_word_2].most_common(5)}"
#    )

   # Test 1: Full word prediction
    print("Suggestions after 'gift':")
    print(predict_next(model, "gift", top_k=3))

    # Test 2: Prefix filtering (after 'the', words starting with 'm')
    print("\nSuggestions after 'the' starting with 'm':")
    print(predict_next(model, "the", prefix="m", top_k=3))

    # Test 3: Unseen word test
    print("\nSuggestions after unseen word 'computer':")
    print(predict_next(model, "computer", top_k=3))
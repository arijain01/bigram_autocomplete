# Bigram Autocomplete Model

A lightweight, purely statistical language model built in Python that predicts the next word in a sequence using bigram frequencies. 

## How It Works
This project implements a classic Markov chain approach to language modeling (a Bigram model). It:
1. Ingests a raw text corpus (*The Gift of the Magi*).
2. Cleans and tokenizes the text into lowercase words.
3. Pairs consecutive words into bigrams `(w1, w2)`.
4. Builds a frequency distribution table using Python's `collections.Counter`.
5. Predicts the most probable next word based on historical frequency, including support for prefix filtering.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/arijain01/bigram_autocomplete.git](https://github.com/arijain01/bigram_autocomplete.git)
   cd bigram_autocomplete
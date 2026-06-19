from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.ngram_generator import NGram
import json


class BPE:

    def __init__(self, num_merges: int):
        self.num_merges = num_merges
        self.merges = DynamicArray()

        self.token_to_id = {}
        self.id_to_token = {}

        self.corpus = None
        self.base_symbols = DynamicArray()

        # adding unknown token for unknown symbols
        self.UNK_TOKEN = "<UNK>"

    def word_to_symbols(self, word: str) -> tuple:
        symbols = DynamicArray()

        for char in word:
            symbols.append(char)

        return tuple(symbols)

    def get_pair_frequencies(self, symbols: tuple):

        pair_frequencies = {}

        bigram_generator = NGram(2)
        pairs = bigram_generator.generate(symbols)

        for pair in pairs:

            if pair in pair_frequencies:
                pair_frequencies[pair] += 1
            else:
                pair_frequencies[pair] = 1

        return pair_frequencies

    def get_best_pair(self, pair_frequencies: dict):
        best_pair = None
        best_frequency = 0

        for pair, frequency in pair_frequencies.items():
            if frequency > best_frequency:
                best_frequency = frequency
                best_pair = pair

        return best_pair

    def merge_pair(self, symbols: tuple, pair: tuple):

        merged_symbols = DynamicArray()

        i = 0
        while i < len(symbols):

            if i < len(symbols) - 1 and (symbols[i], symbols[i + 1]) == pair:

                merged_symbols.append(pair[0] + pair[1])
                i += 2
            else:
                merged_symbols.append(symbols[i])
                i += 1

        return tuple(merged_symbols)

    def train(self, words: DynamicArray):

        # Convert words to symbol tuples
        corpus = DynamicArray()

        for word in words:

            symbols = self.word_to_symbols(word)

            for symbol in symbols:
                if symbol not in self.base_symbols:
                    self.base_symbols.append(symbol)

            corpus.append(self.word_to_symbols(word))

        # Perform multiple merge operations
        for _ in range(self.num_merges):

            pair_frequencies = {}

            # count pair frequencies across entire corpus
            for symbols in corpus:

                word_frequencies = self.get_pair_frequencies(symbols)

                for pair, frequency in word_frequencies.items():
                    if pair in pair_frequencies:
                        pair_frequencies[pair] += frequency
                    else:
                        pair_frequencies[pair] = frequency

            # Find most frequent pair
            best_pair = self.get_best_pair(pair_frequencies)

            # If no pairs to merge
            if best_pair is None:
                break

            # Save learned merge rule
            self.merges.append(best_pair)

            # Apply merge to every word
            new_corpus = DynamicArray()

            for symbols in corpus:
                new_corpus.append(self.merge_pair(symbols, best_pair))

            corpus = new_corpus

        # store the final corpus
        self.corpus = corpus

        # build vocab automatically in training
        self.build_token_vocab()

        return corpus

    def encode(self, word: str) -> tuple:

        symbols = self.word_to_symbols(word)

        for pair in self.merges:

            symbols = self.merge_pair(symbols, pair)

        return symbols

    def decode(self, symbols: tuple) -> str:

        decoded_word = "".join(symbols)

        return decoded_word

    # Save merges
    def save_merges(self, filepath: str):

        merge_list = []

        for pair in self.merges:
            merge_list.append(list(pair))

        with open(filepath, "w") as file:
            json.dump(merge_list, file, indent=4)

    # Save merges
    def load_merges(self, filepath: str):

        self.merges = DynamicArray()

        with open(filepath, "r") as file:
            merge_list = json.load(file)

        for pair in merge_list:
            self.merges.append(tuple(pair))

    # token vocabulary
    def build_token_vocab(self):

        self.token_to_id = {self.UNK_TOKEN: 0}
        self.id_to_token = {0: self.UNK_TOKEN}

        current_id = 1

        # adding base symbols first
        for symbol in self.base_symbols:

            if symbol not in self.token_to_id:
                self.token_to_id[symbol] = current_id
                self.id_to_token[current_id] = symbol

                current_id += 1

        # adding merged symbols from corpus
        for symbols in self.corpus:

            for symbol in symbols:

                if symbol not in self.token_to_id:

                    self.token_to_id[symbol] = current_id
                    self.id_to_token[current_id] = symbol

                    current_id += 1

    # Encode to IDs
    def encode_to_ids(self, word: str):

        symbols = self.encode(word)

        token_ids = DynamicArray()

        for symbol in symbols:
            token_ids.append(
                self.token_to_id.get(symbol, self.token_to_id[self.UNK_TOKEN])
            )

        return token_ids

    # Decode IDs to text
    def decode_ids(self, token_ids: DynamicArray) -> str:

        symbols = DynamicArray()

        for token_id in token_ids:

            if token_id not in self.id_to_token:
                raise ValueError(f"Unknown token id: {token_id}")

            symbols.append(self.id_to_token[token_id])

        return self.decode(tuple(symbols))

    # Save vocabulary
    def save_vocab(self, filepath: str):

        with open(filepath, "w") as file:
            json.dump(self.token_to_id, file, indent=4)


def main() -> None:
    "Entry point for manual execution."

    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = BPE(3)

    bpe.train(words)

    bpe.save_vocab("vocab.json")


if __name__ == "__main__":
    main()

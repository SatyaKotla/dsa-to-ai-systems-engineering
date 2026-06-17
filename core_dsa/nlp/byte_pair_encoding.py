from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.ngram_generator import NGram


class BPE:

    def __init__(self, num_merges: int):
        self.num_merges = num_merges
        self.merges = DynamicArray()

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

        return corpus

    def encode(self, word: str) -> tuple:

        symbols = self.word_to_symbols(word)

        for pair in self.merges:

            symbols = self.merge_pair(symbols, pair)

        return symbols


def main() -> None:
    "Entry point for manual execution."

    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = BPE(3)

    corpus = bpe.train(words)

    print(corpus.to_list())

    print(bpe.merges.to_list())

    print(bpe.encode("slowest"))


if __name__ == "__main__":
    main()

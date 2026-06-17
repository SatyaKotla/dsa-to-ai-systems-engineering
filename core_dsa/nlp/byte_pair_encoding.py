from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.ngram_generator import NGram


class BPE:

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


def main() -> None:
    "Entry point for manual execution."

    text = "hello"

    bpe = BPE()
    symbols = bpe.word_to_symbols(text)
    pair = ("h", "e")

    print(bpe.merge_pair(symbols, pair))


if __name__ == "__main__":
    main()

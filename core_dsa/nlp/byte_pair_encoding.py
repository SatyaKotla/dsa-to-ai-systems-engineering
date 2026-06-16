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


def main() -> None:
    "Entry point for manual execution."

    text = "abab"

    bpe = BPE()
    symbols = bpe.word_to_symbols(text)

    print(bpe.get_pair_frequencies(symbols))


if __name__ == "__main__":
    main()

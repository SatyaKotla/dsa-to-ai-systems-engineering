from core_dsa.nlp.ngram_generator import NGram
from core_dsa.arrays.dynamic_array import DynamicArray


class ByteLevelBPE:

    def __init__(self, num_merges: int):

        self.num_merges = num_merges

        self.token_to_id = {}
        self.id_to_token = {}

        for byte in range(256):
            self.token_to_id[(byte,)] = byte
            self.id_to_token[byte] = (byte,)

    def word_to_symbols(self, text: str) -> tuple:

        symbols = DynamicArray()

        for byte in text.encode("utf-8"):
            symbols.append((byte,))

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

    bpe = ByteLevelBPE(1)

    word = "low"

    symbols = bpe.word_to_symbols(word)

    print(f"symbols: {symbols}")

    pair_frequencies = bpe.get_pair_frequencies(symbols)

    print(f"pair frequencies: {pair_frequencies}")

    best_pair = bpe.get_best_pair(pair_frequencies)

    print(f"best pair: {best_pair}")

    merged_pair = bpe.merge_pair(symbols, pair=((108,), (111,)))

    print(f"merged_pair: {merged_pair}")


if __name__ == "__main__":
    main()

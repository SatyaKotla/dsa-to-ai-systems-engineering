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

    def word_to_bytes(self, text: str) -> tuple:

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


def main() -> None:
    "Entry point for manual execution."

    bpe = ByteLevelBPE(1)

    word = "low"

    print(bpe.word_to_bytes(word))


if __name__ == "__main__":
    main()

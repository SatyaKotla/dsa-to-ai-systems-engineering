from core_dsa.nlp.ngram_generator import NGram
from core_dsa.arrays.dynamic_array import DynamicArray


class ByteLevelBPE:

    def __init__(self, num_merges: int):

        self.num_merges = num_merges
        self.merges = DynamicArray()

        self.token_to_id = {}
        self.id_to_token = {}

        for byte in range(256):
            self.token_to_id[(byte,)] = byte
            self.id_to_token[byte] = (byte,)

        self.corpus = None

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

    def train(self, words: DynamicArray):

        # Convert words to symbol tuples
        corpus = DynamicArray()

        for word in words:

            symbols = self.word_to_symbols(word)

            corpus.append(symbols)

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

    # token vocabulary
    def build_token_vocab(self):

        # 256 byte tokens already exist
        current_id = len(self.token_to_id)

        # Add learned merge tokens
        for pair in self.merges:
            merged_token = pair[0] + pair[1]

            if merged_token not in self.token_to_id:
                self.token_to_id[merged_token] = current_id
                self.id_to_token[current_id] = merged_token
                current_id += 1

        # adding merged symbols from corpus
        for symbols in self.corpus:

            for symbol in symbols:

                if symbol not in self.token_to_id:

                    self.token_to_id[symbol] = current_id
                    self.id_to_token[current_id] = symbol

                    current_id += 1


def main() -> None:
    "Entry point for manual execution."

    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    print(bpe.merges.to_list())
    print(dict(list(bpe.token_to_id.items())[-3:]))


if __name__ == "__main__":
    main()

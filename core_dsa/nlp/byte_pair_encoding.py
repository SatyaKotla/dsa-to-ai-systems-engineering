from core_dsa.arrays.dynamic_array import DynamicArray


class BPE:

    def word_to_symbols(self, word: str) -> tuple:
        symbols = DynamicArray()

        for char in word:
            symbols.append(char)

        return tuple(symbols)


def main() -> None:
    "Entry point for manual execution."

    text = "hello"

    bpe = BPE()

    print(bpe.word_to_symbols(text))


if __name__ == "__main__":
    main()

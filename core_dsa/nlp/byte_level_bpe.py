class ByteLevelBPE:

    def word_to_bytes(self, text: str) -> tuple:

        return tuple(text.encode("utf-8"))


def main() -> None:
    "Entry point for manual execution."

    bpe = ByteLevelBPE()

    word1 = "low"
    word2 = "cafe"
    word3 = "🚀"

    print(f"{word1} in bytes is {bpe.word_to_bytes(word1)}")
    print(f"{word2} in bytes is {bpe.word_to_bytes(word2)}")
    print(f"{word3} in bytes is {bpe.word_to_bytes(word3)}")


if __name__ == "__main__":
    main()

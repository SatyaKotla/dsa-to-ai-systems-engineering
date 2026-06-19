class ByteLevelBPE:

    def __init__(self):

        self.token_to_id = {}
        self.id_to_token = {}

        for byte in range(256):
            self.token_to_id[(byte,)] = byte
            self.id_to_token[byte] = (byte,)

    def word_to_bytes(self, text: str) -> tuple:

        return tuple(text.encode("utf-8"))


def main() -> None:
    "Entry point for manual execution."

    bpe = ByteLevelBPE()

    print(bpe.id_to_token[108])
    print(bpe.token_to_id[(108,)])


if __name__ == "__main__":
    main()

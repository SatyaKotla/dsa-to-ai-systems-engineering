from core_dsa.arrays.dynamic_array import DynamicArray


class ManualTokenizer:

    def tokenize(self, text: str) -> DynamicArray:
        tokens = DynamicArray()
        current_word = DynamicArray()

        for char in text:

            if char.isalpha():
                current_word.append(char.lower())

            else:
                if len(current_word) > 0:
                    word = "".join(char for char in current_word)

                    tokens.append(word)
                    current_word = DynamicArray()

        # to add the edge case
        if len(current_word) > 0:
            word = "".join(char for char in current_word)

            tokens.append(word)

        return tokens


def main() -> None:
    "Entry point for manual execution."

    text = "Hello, world!"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()

from core_dsa.arrays.dynamic_array import DynamicArray


class SentenceTokenizer:

    def tokenize(self, text: str):
        sentences = DynamicArray()
        current_sentence = DynamicArray()

        for char in text:
            if char in {".", "?", "!"}:
                current_sentence.append(char)
                sentence = "".join(char for char in current_sentence)
                sentence = sentence.strip()
                sentences.append(sentence)
                current_sentence = DynamicArray()
            else:
                current_sentence.append(char)

        if len(current_sentence) > 0:
            sentence = "".join(char for char in current_sentence)
            sentence = sentence.strip()
            sentences.append(sentence)

        return sentences


def main() -> None:
    "Entry point for manual execution."

    text = "Hello, world! How are you? What's up!"
    tokenizer = SentenceTokenizer()
    tokens = tokenizer.tokenize(text)

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()

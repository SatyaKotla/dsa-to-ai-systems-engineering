from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.tokenizer import ManualTokenizer


class Vocabulary:

    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}

    def add_word(self, word: str):

        if word in self.word_to_id:
            return

        else:
            new_id = len(self.word_to_id)

            self.word_to_id[word] = new_id
            self.id_to_word[new_id] = word

    def build(self, tokens: DynamicArray):

        for token in tokens:
            self.add_word(token)

    def encode(self, tokens: DynamicArray):
        encoded_list = DynamicArray()

        for token in tokens:
            try:
                encoded_list.append(self.word_to_id[token])

            except KeyError:
                raise KeyError(f"Token '{token}' not found in vocabulary")

        return encoded_list


def main() -> None:
    "Entry point for manual execution."

    text = "hello world hello world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    vocab = Vocabulary()

    vocab.build(tokens)

    tokens = ["hello", "world"]

    encoded = vocab.encode(tokens)
    print(encoded.to_list())


if __name__ == "__main__":
    main()

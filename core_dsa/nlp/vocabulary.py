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


def main() -> None:
    "Entry point for manual execution."

    text = "hello world hello world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    vocab = Vocabulary()

    vocab.build(tokens)

    print(vocab.id_to_word)
    print(vocab.word_to_id)


if __name__ == "__main__":
    main()

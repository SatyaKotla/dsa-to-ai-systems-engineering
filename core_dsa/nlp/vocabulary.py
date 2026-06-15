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

    def decode(self, token_ids: DynamicArray):
        decoded_list = DynamicArray()

        for token_id in token_ids:
            try:
                decoded_list.append(self.id_to_word[token_id])

            except KeyError:
                raise KeyError(f"Token ID '{token_id}' not found in vocabulary")

        return decoded_list


def main() -> None:
    "Entry point for manual execution."

    text = "hello world hello world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    vocab = Vocabulary()

    vocab.build(tokens)

    token_ids = [0, 1]

    decoded = vocab.decode(token_ids)
    print(decoded.to_list())


if __name__ == "__main__":
    main()

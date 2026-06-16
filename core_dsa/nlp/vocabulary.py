from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.tokenizer import ManualTokenizer


class Vocabulary:

    PAD_TOKEN = "<PAD>"
    UNK_TOKEN = "<UNK>"
    BOS_TOKEN = "<BOS>"
    EOS_TOKEN = "<EOS>"

    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}

        self.add_word(self.PAD_TOKEN)
        self.add_word(self.UNK_TOKEN)
        self.add_word(self.BOS_TOKEN)
        self.add_word(self.EOS_TOKEN)

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
        unknown_id = self.word_to_id[self.UNK_TOKEN]

        for token in tokens:
            try:
                encoded_list.append(self.word_to_id[token])

            except KeyError:
                encoded_list.append(unknown_id)

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

    text = "hello world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    vocab = Vocabulary()

    vocab.build(tokens)

    print(f"ID to word mappings: {vocab.id_to_word}")
    print(f"Word to ID mappings: {vocab.word_to_id}")
    new_text = "hello chatgpt world"
    new_tokens = tokenizer.tokenize(new_text)
    encoded_list = vocab.encode(new_tokens)
    decoded_list = vocab.decode(encoded_list)
    print(f"Input text: {new_text}")
    print(f"Encoded: {encoded_list.to_list()}")
    print(f"Decoded: {decoded_list.to_list()}")


if __name__ == "__main__":
    main()

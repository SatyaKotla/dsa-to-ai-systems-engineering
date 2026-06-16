from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.tokenizer import ManualTokenizer


class Vocabulary:

    PAD_TOKEN = "<PAD>"
    UNK_TOKEN = "<UNK>"
    BOS_TOKEN = "<BOS>"
    EOS_TOKEN = "<EOS>"

    def __init__(self):
        self.word_to_id = {}  # Word to ID mappings
        self.id_to_word = {}  # ID to word mappings
        self.word_counts = {}  # Word frequency count

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

            if token in self.word_counts:
                self.word_counts[token] += 1
            else:
                self.word_counts[token] = 1

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

    def add_special_tokens(self, tokens: DynamicArray) -> DynamicArray:
        begin_token = self.BOS_TOKEN
        end_token = self.EOS_TOKEN

        new_tokens = DynamicArray()

        new_tokens.append(begin_token)

        for token in tokens:
            new_tokens.append(token)

        new_tokens.append(end_token)

        return new_tokens

    def get_word_frequency(self, word: str) -> int:

        try:
            return self.word_counts[word]

        except KeyError:
            return 0

    def get_all_frequencies(self):

        return self.word_counts


def main() -> None:
    "Entry point for manual execution."

    text = "hello world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    vocab = Vocabulary()

    vocab.build(tokens)
    print(f"Frequency of words : {vocab.get_all_frequencies()}")
    print(f"Frequency of hello: {vocab.get_word_frequency('hello')}")


if __name__ == "__main__":
    main()

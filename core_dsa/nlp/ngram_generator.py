from core_dsa.arrays.dynamic_array import DynamicArray
from core_dsa.nlp.tokenizer import ManualTokenizer


class NGram:

    def __init__(self, n: int):

        if n <= 0:
            raise ValueError("n must be greater than 0")

        self.n = n

    def generate(self, sequence) -> DynamicArray:

        n_grams = DynamicArray()

        for start in range(len(sequence) - self.n + 1):
            n_gram_temp = DynamicArray()
            for i in range(self.n):
                n_gram_temp.append(sequence[start + i])
            n_grams.append(tuple(n_gram_temp))

        return n_grams


def main() -> None:
    "Entry point for manual execution."

    text = "Hello, world, hi, how are you "
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    bigram = NGram(2)
    print(bigram.generate(tokens).to_list())
    trigram = NGram(3)
    print(trigram.generate(tokens).to_list())


if __name__ == "__main__":
    main()

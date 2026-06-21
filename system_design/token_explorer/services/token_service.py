from core_dsa.nlp.tokenizer import ManualTokenizer
from core_dsa.nlp.byte_pair_encoding import BPE
from core_dsa.nlp.byte_level_bpe import ByteLevelBPE


class TokenService:

    def __init__(self, num_merges=1):

        self.word_tokenizer = ManualTokenizer()
        self.character_bpe = BPE(num_merges=num_merges)
        self.byte_bpe = ByteLevelBPE(num_merges=num_merges)

    def tokenize_word(self, text: str):
        tokens = self.word_tokenizer.tokenize(text=text).to_list()

        return {"tokens": tokens, "token_count": len(tokens)}

    def tokenize_character(self, text: str):

        tokens = list(text)

        return {"tokens": tokens, "token_count": len(tokens)}

    def tokenize_character_bpe(self, text: str):

        tokens = list(self.character_bpe.encode(text))

        return {"tokens": tokens, "token_count": len(tokens)}

    def tokenize_byte_bpe(self, text: str):

        tokens = list(self.byte_bpe.encode(text))

        token_ids = self.byte_bpe.encode_to_ids(text)

        return {
            "tokens": tokens,
            "token_ids": token_ids.to_list(),
            "token_count": len(tokens),
        }

    def compare(self, text: str):

        return {
            "word": self.tokenize_word(text),
            "character": self.tokenize_character(text),
            "character_bpe": self.tokenize_character_bpe(text),
            "byte_bpe": self.tokenize_byte_bpe(text),
        }


def main() -> None:
    "Entry point for manual execution."

    service = TokenService()

    result = service.compare("lowest lower low")

    print(result)


if __name__ == "__main__":
    main()

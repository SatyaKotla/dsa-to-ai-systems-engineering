####################################################
# ------- TESTS FOR SENTENCE TOKENIZER ------- #####
####################################################
from core_dsa.nlp.sentence_tokenizer import SentenceTokenizer

# Basic sentences


def test_sentence_tokenizer_basic():

    tokenizer = SentenceTokenizer()

    result = tokenizer.tokenize("Hello world. How are you?")

    assert result.to_list() == ["Hello world.", "How are you?"]


# Single sentence
def test_sentence_tokenizer_single():

    tokenizer = SentenceTokenizer()

    result = tokenizer.tokenize("Hello world.")

    assert result.to_list() == ["Hello world."]


# Empty input
def test_sentence_tokenizer_empty():

    tokenizer = SentenceTokenizer()

    result = tokenizer.tokenize("")

    assert result.to_list() == []

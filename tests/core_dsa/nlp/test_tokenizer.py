####################################################
# ------- TESTS FOR TOKENIZER ------- ##############
####################################################
from core_dsa.nlp.tokenizer import ManualTokenizer


# Basic tests
def test_manual_tokenizer_basic():
    text = "Hello, world!"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    assert tokens.to_list() == ["hello", "world"]


def test_manual_tokenizer_comma():
    text = "hello,,,,world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    assert tokens.to_list() == ["hello", "world"]


def test_manual_tokenizer_space():
    text = "Hello    world"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    assert tokens.to_list() == ["hello", "world"]


def test_manual_tokenizer_empty():
    text = ""
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    assert tokens.to_list() == []


def test_manual_tokenizer_lowercase():
    text = "Python"
    tokenizer = ManualTokenizer()
    tokens = tokenizer.tokenize(text)

    assert tokens.to_list() == ["python"]

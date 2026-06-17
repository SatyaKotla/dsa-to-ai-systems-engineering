####################################################
# ------- TESTS FOR VOCABULARY ------- #############
####################################################
from core_dsa.nlp.vocabulary import Vocabulary
from core_dsa.arrays.dynamic_array import DynamicArray


# Build vocabulary
def test_vocab_build():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")
    tokens.append("world")

    vocab.build(tokens)

    assert vocab.word_to_id["hello"] == 4
    assert vocab.word_to_id["world"] == 5


# Encode known words
def test_vocab_encode():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")
    tokens.append("world")

    vocab.build(tokens)

    encoded = vocab.encode(tokens)

    assert encoded.to_list() == [4, 5]


# Encode unknown word
def test_vocab_encode_unknown():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")

    vocab.build(tokens)

    query = DynamicArray()
    query.append("unknown")

    encoded = vocab.encode(query)

    assert encoded.to_list() == [vocab.word_to_id[vocab.UNK_TOKEN]]


# Decode
def test_vocab_decode():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")
    tokens.append("world")

    vocab.build(tokens)

    decoded = vocab.decode([4, 5])

    assert decoded.to_list() == ["hello", "world"]


# Special tokens
def test_vocab_add_special_tokens():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")

    result = vocab.add_special_tokens(tokens)

    assert result.to_list() == [vocab.BOS_TOKEN, "hello", vocab.EOS_TOKEN]


# Padding
def test_vocab_padding():

    vocab = Vocabulary()

    tokens = DynamicArray()

    tokens.append("hello")

    padded = vocab.pad_sequence(tokens=tokens, max_length=3)

    assert padded.to_list() == ["hello", vocab.PAD_TOKEN, vocab.PAD_TOKEN]

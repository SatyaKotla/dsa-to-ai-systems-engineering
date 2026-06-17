####################################################
# ------- TESTS FOR VOCABULARY ------- #############
####################################################
from core_dsa.nlp.ngram_generator import NGram
from core_dsa.arrays.dynamic_array import DynamicArray


# Bigram
def test_bigram_generation():
    tokens = DynamicArray()

    tokens.append("i")
    tokens.append("love")
    tokens.append("nlp")

    bigram = NGram(2)

    result = bigram.generate(tokens)

    assert result.to_list() == [("i", "love"), ("love", "nlp")]


# Trigram
def test_trigram_generation():
    tokens = DynamicArray()

    tokens.append("i")
    tokens.append("love")
    tokens.append("nlp")

    trigram = NGram(3)

    result = trigram.generate(tokens)

    assert result.to_list() == [("i", "love", "nlp")]


# n > length
def test_ngram_large_n():
    tokens = DynamicArray()

    tokens.append("hello")

    bigram = NGram(2)

    result = bigram.generate(tokens)

    assert result.to_list() == []

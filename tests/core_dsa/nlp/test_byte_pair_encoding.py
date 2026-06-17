####################################################
# ------- TESTS FOR BYTE PAIR ENCODER ------- ######
####################################################
from core_dsa.nlp.byte_pair_encoding import BPE
from core_dsa.arrays.dynamic_array import DynamicArray


# Word to symbols
def test_word_to_symbols():
    bpe = BPE(1)

    assert bpe.word_to_symbols("hello") == ("h", "e", "l", "l", "o")


# Pair frequencies
def test_pair_frequencies():
    bpe = BPE(1)

    result = bpe.get_pair_frequencies(("a", "b", "a", "b"))

    assert result == {("a", "b"): 2, ("b", "a"): 1}


# Best pair
def test_best_pair():
    bpe = BPE(1)

    best = bpe.get_best_pair({("a", "b"): 5, ("b", "c"): 2})

    assert best == ("a", "b")


# Merge pair
def test_merge_pair():
    bpe = BPE(1)

    result = bpe.merge_pair(("l", "o", "w"), ("l", "o"))

    assert result == ("lo", "w")


# Train learns merges
def test_bpe_training():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = BPE(3)

    bpe.train(words)

    assert len(bpe.merges) > 0


# Encode + Decode
def test_bpe_roundtrip():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = BPE(3)

    bpe.train(words)

    word = "slowest"

    encoded = bpe.encode(word)

    decoded = bpe.decode(encoded)

    assert decoded == word


# Save/Load merges
def test_bpe_save_load_merges():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe1 = BPE(3)

    bpe1.train(words)

    bpe1.save_merges("merges.json")

    bpe2 = BPE(3)

    bpe2.load_merges("merges.json")

    encoded1 = bpe1.encode("slowest")
    encoded2 = bpe2.encode("slowest")

    assert encoded1 == encoded2

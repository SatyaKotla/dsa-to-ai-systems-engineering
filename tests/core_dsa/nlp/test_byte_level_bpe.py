####################################################
# ------- TESTS FOR BYTE LEVEL BPE ------- ######
####################################################
from core_dsa.nlp.byte_level_bpe import ByteLevelBPE
from core_dsa.arrays.dynamic_array import DynamicArray

# Test Save/Load Round Trip


def test_save_load_roundtrip():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    ids_before = bpe.encode_to_ids("lowest")

    bpe.save_merges("merges.json")
    bpe.save_vocab("vocab.json")

    bpe2 = ByteLevelBPE(3)

    bpe2.load_merges("merges.json")
    bpe2.load_vocab("vocab.json")

    ids_after = bpe2.encode_to_ids("lowest")

    assert ids_before.to_list() == ids_after.to_list()


# Decode round trip
def test_decode_roundtrip():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    text = "lowest"

    ids = bpe.encode_to_ids(text)

    decoded = bpe.decode_ids(ids)

    assert decoded == text


# Unicode
def test_unicode():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    text = "hello 🚀"

    ids = bpe.encode_to_ids(text)

    decoded = bpe.decode_ids(ids)

    assert decoded == text


# special token encoding
def test_special_tokens_encoding():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    text = "lowest"

    ids = bpe.encode_to_ids(text, add_special_tokens=True)

    assert ids[0] == bpe.token_to_id[bpe.BOS_TOKEN]
    assert ids[-1] == bpe.token_to_id[bpe.EOS_TOKEN]


# special token decoding
def test_special_tokens_decoding():
    words = DynamicArray()

    words.append("low")
    words.append("lower")
    words.append("lowest")

    bpe = ByteLevelBPE(3)

    bpe.train(words)

    text = "lowest"

    ids = bpe.encode_to_ids(text, add_special_tokens=True)

    decoded = bpe.decode_ids(ids, skip_special_tokens=True)

    assert decoded == "lowest"

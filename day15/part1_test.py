from part1 import hash_alg


def test_hash_alg():
    """Test hash_alg function."""
    assert hash_alg("HASH") == 52
    assert hash_alg("rn=1") == 30
    assert hash_alg("cm-") == 253
    assert hash_alg("qp=3") == 97
    assert hash_alg("cm=2") == 47
    assert hash_alg("qp-") == 14
    assert hash_alg("pc=4") == 180
    assert hash_alg("ot=9") == 9
    assert hash_alg("ab=5") == 197
    assert hash_alg("pc-") == 48
    assert hash_alg("pc=6") == 214
    assert hash_alg("ot=7") == 231

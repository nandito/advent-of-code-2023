from part1 import get_numbers


def test_get_numbers():
    """Test get_numbers function."""
    assert get_numbers("1234") == "14"
    assert get_numbers("91212129") == "99"
    assert get_numbers("1one") == "11"
    assert get_numbers("one1") == "11"
    assert get_numbers("one1one") == "11"
    assert get_numbers("one2one1") == "21"
    assert get_numbers("one2one1one") == "21"
    assert get_numbers("1abc2") == "12"
    assert get_numbers("pqr3stu8vwx") == "38"
    assert get_numbers("a1b2c3d4e5f") == "15"
    assert get_numbers("treb7uchet") == "77"

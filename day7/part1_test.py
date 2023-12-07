from part1 import get_hand_type, order_deck_by_strength, sort_func


def test_get_hand_type():
    """Test get_hand_type function"""
    assert get_hand_type("KKKKK") == "five of a kind"
    assert get_hand_type("KKK2K") == "four of a kind"
    assert get_hand_type("23332") == "full house"
    assert get_hand_type("T55J5") == "three of a kind"
    assert get_hand_type("QQQJA") == "three of a kind"
    assert get_hand_type("KK677") == "two pair"
    assert get_hand_type("KTJJT") == "two pair"
    assert get_hand_type("32T3K") == "one pair"
    assert get_hand_type("QJTKA") == "high card"


def test_sort_func():
    """Test sort_func function"""
    assert sort_func(("KKKKK", "1")) == "11111"
    assert sort_func(("KKK2K", "2")) == "111c1"


def test_order_deck_by_strength():
    """Test order_deck_by_strength function"""
    assert order_deck_by_strength([("KKKKK", "1"), ("KKK2K", "2")]) == [
        ("KKKKK", "1"),
        ("KKK2K", "2"),
    ]
    assert order_deck_by_strength([("KKK2K", "2"), ("KKKKK", "1")]) == [
        ("KKKKK", "1"),
        ("KKK2K", "2"),
    ]
    assert order_deck_by_strength([("KKK2K", "2"), ("KKKKK", "1"), ("KTJJT", "3")]) == [
        ("KKKKK", "1"),
        ("KKK2K", "2"),
        ("KTJJT", "3"),
    ]

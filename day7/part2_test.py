from part2 import get_highest_card, process_joker


def test_process_joker():
    """Test process_joker"""
    assert process_joker("32T3K") == ("32T3K", "32T3K")
    assert process_joker("T55J5") == ("T55J5", "T5555")
    assert process_joker("KTJJT") == ("KTJJT", "KTTTT")
    assert process_joker("QQQJA") == ("QQQJA", "QQQQA")
    assert process_joker("QQKKJ") == ("QQKKJ", "QQKKK")
    assert process_joker("JJJJ3") == ("JJJJ3", "33333")
    assert process_joker("JJJA3") == ("JJJA3", "AAAA3")
    assert process_joker("JJJJJ") == ("JJJJJ", "AAAAA")
    assert process_joker("QQTTJ") == ("QQTTJ", "QQTTQ")
    assert process_joker("33JJJ") == ("33JJJ", "33333")
    assert process_joker("324JA") == ("324JA", "324AA")


def test_get_highest_card():
    """Test get_highest_card"""
    assert get_highest_card("32T3K") == "K"
    assert get_highest_card("32TJK") == "K"
    assert get_highest_card("J2TAK") == "A"
    assert get_highest_card("2345J") == "5"
    assert get_highest_card("JTQAK") == "A"
    assert get_highest_card("TJQKA") == "A"
    assert get_highest_card("AKQJT") == "A"

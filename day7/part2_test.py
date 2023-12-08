from part2 import process_joker


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

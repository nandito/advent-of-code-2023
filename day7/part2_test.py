from part2 import process_joker


def test_process_joker():
    """Test process_joker"""
    assert process_joker("32T3K") == ("32T3K", "32T3K")
    assert process_joker("T55J5") == ("T55J5", "T5555")
    assert process_joker("KTJJT") == ("KTJJT", "KTTTT")
    assert process_joker("QQQJA") == ("QQQJA", "QQQQA")

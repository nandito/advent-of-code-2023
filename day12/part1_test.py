from part1 import get_arrangement_count


def test_get_arrangement_count():
    """Test get_arrangement_count()"""
    # Added `.` to the end where it was missing, otherwise the last character
    # was wrong
    assert get_arrangement_count("???.###.", (1, 1, 3)) == 1
    assert get_arrangement_count(".??..??...?##.", (1, 1, 3)) == 4
    assert get_arrangement_count("?#?#?#?#?#?#?#?.", (1, 3, 1, 6)) == 1
    assert get_arrangement_count("????.#...#...", (4, 1, 1)) == 1
    assert get_arrangement_count("????.######..#####.", (1, 6, 5)) == 4
    assert get_arrangement_count("?###????????.", (3, 2, 1)) == 10

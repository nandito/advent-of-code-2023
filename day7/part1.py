import numpy as np

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
types = [
    "five of a kind",
    "four of a kind",
    "full house",
    "three of a kind",
    "two pair",
    "one pair",
    "high card",
]


def get_hand_type(hand):
    """Return the type of hand"""
    hand_array = np.array(list(hand))
    card_counts = np.unique(hand_array, return_counts=True)
    if 5 in card_counts[1]:
        return types[0]
    elif 4 in card_counts[1]:
        return types[1]
    elif 3 in card_counts[1] and 2 in card_counts[1]:
        return types[2]
    elif 3 in card_counts[1]:
        return types[3]
    elif 2 in card_counts[1] and len(card_counts[1]) == 3:
        return types[4]
    elif 2 in card_counts[1]:
        return types[5]
    else:
        return types[6]


def hand_to_numbers(hand):
    """Convert the hand to numbers"""
    return [format(cards.index(x), "x") for x in list(hand)]


def sort_func(x):
    """Sort function"""
    return "".join(map(str, hand_to_numbers(x[0])))


def order_deck_by_strength(deck):
    """Order the deck by strength"""
    return sorted(deck, key=sort_func)


def solve_part1(lines):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        [hand, bid] = line.strip().split(" ")
        hand_type = get_hand_type(hand)
        if hand_type == types[0]:
            five_of_a_kind.append((hand, bid))
        elif hand_type == types[1]:
            four_of_a_kind.append((hand, bid))
        elif hand_type == types[2]:
            full_house.append((hand, bid))
        elif hand_type == types[3]:
            three_of_a_kind.append((hand, bid))
        elif hand_type == types[4]:
            two_pair.append((hand, bid))
        elif hand_type == types[5]:
            one_pair.append((hand, bid))
        else:
            high_card.append((hand, bid))

    # print("five of a kind:", order_deck_by_strength(five_of_a_kind))
    # print("four of a kind:", order_deck_by_strength(four_of_a_kind))
    # print("full house:", order_deck_by_strength(full_house))
    # print("three of a kind:", order_deck_by_strength(three_of_a_kind))
    # print("two pair:", order_deck_by_strength(two_pair))
    # print("one pair:", order_deck_by_strength(one_pair))
    # print("high card:", order_deck_by_strength(high_card))
    ordered_deck = (
        order_deck_by_strength(five_of_a_kind)
        + order_deck_by_strength(four_of_a_kind)
        + order_deck_by_strength(full_house)
        + order_deck_by_strength(three_of_a_kind)
        + order_deck_by_strength(two_pair)
        + order_deck_by_strength(one_pair)
        + order_deck_by_strength(high_card)
    )
    # print("ordered deck:", ordered_deck)
    total_winnings = 0
    for idx, card in enumerate(reversed(ordered_deck)):
        total_winnings += int(card[1]) * (idx + 1)
    print("total winnings:", total_winnings)

import numpy as np


cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def entropy(hand):
    """Calculate the entropy of the hand"""
    hand_array = np.array(list(hand))
    card_counts = np.unique(hand_array, return_counts=True)
    # print("\ncard counts:", card_counts)
    # print("card counts[1]:", card_counts[1])
    # print("card counts[1] / len(hand):", card_counts[1] / len(hand))
    # print("np.log2(card counts[1] / len(hand)):", np.log2(card_counts[1] / len(hand)))
    # print("np.log2(card counts[1] / len(hand)) * (card counts[1] / len(hand)):", np.log2(card_counts[1] / len(hand)) * (card_counts[1] / len(hand)))
    return -np.sum(np.log2(card_counts[1] / len(hand)) * (card_counts[1] / len(hand)))


def entropy_with_jokers(hand):
    try:
        # Get the most common card (excluding jokers)
        top = sorted(
            hand.replace("J", ""),
            key=lambda x: hand.count(x),
        )[-1]
        return entropy(hand.replace("J", top))
    except IndexError:
        return entropy(hand)


def solve_part2(lines):
    """Solve part 2"""
    hands = [(h, int(b)) for h, b in map(str.split, lines)]

    # print("hands:", hands)
    result = [
        (len(hands) - i) * bid
        for i, (__, bid) in enumerate(
            sorted(
                hands,
                key=lambda h: (
                    entropy_with_jokers(h[0]),
                    *map("".join(cards).index, h[0]),
                ),
            )
        )
    ]
    # print("result:", result)
    print("total winnings:", sum(result))

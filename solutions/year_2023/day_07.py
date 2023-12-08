import itertools
import re

# assume sorted hands (same cards always next to each other, cards in order]
hand_types = {
    "five_of_a_kind": re.compile(r'(\w)\1{4}'),
    "four_of_a_kind": re.compile(r'\w*(\w)\1\1\1\w*'),
    "full_house": re.compile(r"(\w)\1(\w)\2\2|(\w)\3\3(\w)\4"),
    "three_of_a_kind": re.compile(r"\w*(\w)\1\1\w*"),
    "two_pair": re.compile(r"\w*(\w)\1\w*(\w)\2\w*"),
    "one_pair": re.compile(r"\w*(\w)\1\w*"),
    "high_card": re.compile(r"\w"),
}

def parse_input(input_str):
    out_list = []
    for line in input_str.splitlines():
        i,j = line.split()
        out_list.append([i, int(j)])
    return out_list
    

def part_a(input_str: str):
    card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    card_hands_list = parse_input(input_str)
    hand_info = []
    for card_hand, points in card_hands_list:
        cards = sort_card_set(card_hand, card_order)
        for idx, (key, type_regex) in enumerate(hand_types.items()):
            if type_regex.match(cards):
                hand_info.append([tuple([idx] + [card_order.index(c) for c in card_hand]), points, card_hand, key])
                break
    hand_info.sort(key=lambda item: item[0], reverse=True)
    scores_list = [(idx+1) * item[1] for idx, item in enumerate(hand_info)]
    return sum(scores_list)


def sort_card_set(cards, card_order):
    c_sorted = [c for c in cards]
    c_sorted.sort(key=lambda c_: card_order.index(c_))
    c_sorted = ''.join(c_sorted)
    return  c_sorted

def get_best_card(card, card_order):
    if not 'J' in card:
        return card

    card = sort_card_set(card, card_order=card_order)
    n_j = 5 - card.index('J')
    hand_options = [card.replace('J' * n_j, ''.join(new_cards)) for new_cards in
                    itertools.combinations_with_replacement('AKQT98765432', n_j)]
    hand_options = [sort_card_set(c, card_order=card_order) for c in hand_options]

    for type_regex in hand_types.values():
        for c in hand_options:
            if type_regex.match(c):
                return c


def part_b(input_str: str):
    card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


    card_hands_list = parse_input(input_str)
    hand_info = []
    for card_hand, points in card_hands_list:
        # sort hand, jokers last
        cards = sort_card_set(card_hand, card_order)
        cards = get_best_card(cards, card_order)
        for idx, (key, type_regex) in enumerate(hand_types.items()):
            if type_regex.match(cards):
                hand_info.append([tuple([idx] + [card_order.index(c) for c in card_hand]), points, card_hand, key])
                break
    hand_info.sort(key=lambda item: item[0], reverse=True)

    # print(*hand_info, sep='\n')

    scores_list = [(idx + 1) * item[1] for idx, item in enumerate(hand_info)]
    return sum(scores_list)
#
# f
#     #
#     hand_info.sort(key=lambda item: item[0], reverse=True)
#
#     print(*hand_info, sep='\n')
#     scores = [(idx+1) * item[1] for idx, item in enumerate(hand_info)]
#     return sum(scores)


if __name__ == '__main__':
    # For debugging
    pass

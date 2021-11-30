"""
A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 2 through 10, jack, queen, king, or ace
(denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
The suit has no impact on value.

A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.



High Card
Hands which do not fit any higher category are ranked by the value of their highest card.

Pair
Two of the five cards in the hand have the same value.

Two Pairs
The hand contains two different pairs.

Three of a Kind
Three of the cards in the hand have the same value.

Straight
Hand contains five cards with consecutive values.

Flush
Hand contains five cards of the same suit.


Full House
Three cards of the same value, with the remaining two cards forming a pair.

Four of a Kind
Four cards with the same value.

Straight Flush
Five cards of the same suit in numerical order.


Royal Flush
Consists of the ace, king, queen, jack and ten of a suit.


Напишите программу, которая получает на вход пять карт и выводит старшую покерную комбинацию,
которая образуется этими картами.

Формат ввода:
Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.

Формат вывода:
Название старшей комбинации, сформировавшейся на пришедшем наборе.

Sample Input:

10C JC QC KC AC
Sample Output:

Royal Flush
"""
from typing import List


def count_pairs(nums: List[int]) -> int:
    k = 0
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            k += 1
            i += 1
        i += 1
    return k


def get_suit(card: str) -> str:
    return card[-1]


def get_weight(card: str) -> int:
    d = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 3,
        '6': 4,
        '7': 5,
        '8': 6,
        '9': 7,
        '10': 8,
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12
    }
    return d[card[:-1]]


def main():
    cards = input().split()
    suits = [get_suit(card) for card in cards]
    weights = [get_weight(card) for card in cards]
    sorted_weights = sorted(weights)
    if all(suit == suits[0] for suit in suits):
        if sorted_weights == list(range(sorted_weights[0], sorted_weights[4] + 1)):
            if sorted_weights == [8, 9, 10, 11, 12]:
                print('Royal Flush')
                return
            else:
                print('Straight Flush')
                return
    if (all(weight == sorted_weights[0] for weight in sorted_weights[0:3])
            or all(weight == sorted_weights[1] for weight in sorted_weights[1:5])):
        print('Four of a Kind')
        return
    if ((all(weight == sorted_weights[0] for weight in sorted_weights[0:3])
         and all(weight == sorted_weights[3] for weight in sorted_weights[3:5]))
            or (all(weight == sorted_weights[0] for weight in sorted_weights[0:2])
                and all(weight == sorted_weights[2] for weight in sorted_weights[2:5]))):
        print('Full House')
        return
    if all(suit == suits[0] for suit in suits):
        print('Flush')
        return
    if sorted_weights == list(range(sorted_weights[0], sorted_weights[4] + 1)):
        print('Straight')
        return
    if (all(weight == sorted_weights[0] for weight in sorted_weights[0:3])
            or all(weight == sorted_weights[1] for weight in sorted_weights[1:4])
            or all(weight == sorted_weights[2] for weight in sorted_weights[2:5])):
        print('Three of a Kind')
        return
    pairs = count_pairs(sorted_weights)
    if pairs == 2:
        print('Two Pairs')
        return
    if pairs == 1:
        print('Pair')
        return
    print('High Card')


if __name__ == '__main__':
    main()

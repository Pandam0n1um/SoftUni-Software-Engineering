card_deck=input().split()
n_shuffle=int(input())

top_card=card_deck[0]
bottom_card=card_deck[-1]

middle_deck= len(card_deck) // 2

shuffled_deck = []

for nth_shuffle in range(n_shuffle):

    left_deck = []
    right_deck = []

    for i in range(1, middle_deck):
        left_deck.append(card_deck[i])
    for i in range(middle_deck, len(card_deck) - 1):
        right_deck.append(card_deck[i])

    for index in range(len(left_deck)):
        shuffled_deck.append(right_deck[index])
        shuffled_deck.append(left_deck[index])

    card_deck=shuffled_deck.copy()
    card_deck.append(bottom_card)
    card_deck.insert(0,top_card)
    shuffled_deck = []
print(card_deck)
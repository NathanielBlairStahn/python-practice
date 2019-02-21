import numpy as np

def simulate_draw(num_cards=60, num_stars=3, num_diamonds=3, num_drawn=5):
    '''
    You have a shuffled deck of 60 cards containing the following
    cards of special interest:

    *Three of these cards in the deck are marked with a diamond.
    *Three of the cards are marked with a star.
    *The remaining cards are nothing special.

    You draw an initial hand of five cards, after which you must discard
    any of the star cards for an additional three cards drawn from the top
    of the deck. This process is repeated until you find yourself with a hand
    that does not contain any star cards.

    Write a simulation to approximate the probability that your initial draw
    results in a final hand containing a diamond card.

    Q: Do we draw three new cards for *each* star card you discard, or three
       new cards if you discard any number of star cards?
    A: For each.

    Algorithm:
    After the deck is shuffled, number the cards from 0 to 59 from top to bottom.
    I.e. 0 is the top card, 1 is the 2nd card, ..., 59 is the bottom card.
    Randomly choose 6 cards without replacement to be the stars and the diamonds.
    '''
    special = np.random.choice(num_cards, size=num_stars+num_diamonds, replace=False)
    stars = special[:num_stars] #first cards are stars
    diamonds = special[-num_diamonds:] #last cards are diamonds
    prev_card = -1
    next_card = num_drawn #The next card in the deck after we have drawn the top num_drawn cards
    stars_in_hand = stars < next_card
    while any(prev_card < stars < next_card):
          next_card = 1

def simulate_diamond_prob():
    pass

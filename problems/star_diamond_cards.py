import numpy as np

def simulate_draw(num_cards=60, num_stars=3, num_diamonds=3, num_drawn=5, num_redrawn=3):
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
    The stars and the diamonds are then represented by 6 random numbers in {0,...,59}.
    Thus we can draw a random sample without replacement from range(60), and assume that
    the first 3 of these random numbers are stars and the last 3 are diamonds.

    '''
    special = np.random.choice(num_cards, size=num_stars+num_diamonds, replace=False)
    #first cards are stars. Sort them to make calculations easier.
    stars = np.sort(special[:num_stars])
    diamonds = special[-num_diamonds:] #last cards are diamonds
    # #1st Attempt (unfinished, won't work yet):
    # prev_card = -1
    # next_card = num_drawn #The next card in the deck after we have drawn the top num_drawn cards
    # stars_in_hand = stars < next_card
    # while any(prev_card < stars < next_card):
    #       next_card = 1 #placeholder

    # #2nd Attempt (I think this should work):
    # next_star_idx=0
    # next_card = num_drawn #The next card in the deck after we have drawn the top num_drawn cards
    # while next_star_idx < len(stars) and stars[next_star_idx] < next_card:
    #     next_card += num_redrawn
    #     next_star_idx += 1

    #3rd Attempt:
    #The next card in the deck after we have drawn the top num_drawn cards
    next_card = num_drawn
    #Go through the stars in order to see if we need to draw more cards.
    for star in stars:
        #If the next star is less than the next card to draw, then it is in our hand,
        #so we must discard it and draw 3 more.
        if star < next_card:
            next_card += num_redrawn
        #Otherwise, there are no stars in our hand, so we're done drawing cards.
        else:
            break

    return next_card, stars, diamonds

def simulate_diamond_prob():
    pass

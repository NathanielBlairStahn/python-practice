import numpy as np

class FinalHand:
    """
    Class to encode the final hand in one complete draw of cards, including discarding
    stars and re-drawing.
    """
    def __init__(self, deck_size, initial_hand_size, next_card, stars, diamonds):
        self.deck_size = deck_size
        self.initial_hand_size = initial_hand_size
        self.next_card = next_card
        self.stars = stars
        self.diamonds = diamonds
        # self.num_to_redraw = num_to_redraw
        # self.num_to_redraw = 1

    def discarded_stars(self):
        """
        Returns the stars that were discarded.
        """
        return [star for star in self.stars if star < self.next_card]

    def diamonds_in_hand(self):
        """
        Returns a list of the diamonds in the current hand.
        """
        return [diamond for diamond in self.diamonds if diamond < self.next_card]

    def num_redrawn(self):
        """
        Returns the total number of cards redrawn.
        """
        return self.next_card - self.initial_hand_size

    def cards_in_hand(self):
        """
        Returns a generator to iterate through the cards in the current hand.
        """
        return (card for card in range(min(self.next_card, self.deck_size))
            if card not in self.stars)

    def num_cards_in_hand(self):
        """
        Returns the number of cards in the current hand.
        """
        return len(list(self.cards_in_hand()))

    def has_diamond(self):
        """
        Returns True if the hand contains a diamond.
        """
        return any(self.diamonds < self.next_card)

    def is_success(self):
        """
        Returns True if we were able to discard all the stars and redraw before reaching the end of the deck.
        """
        return self.next_card <= self.deck_size

def simulate_draw(num_cards=60, num_stars=3, num_diamonds=3, num_drawn=5, num_to_redraw=3):
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
    #     next_card += num_to_redraw
    #     next_star_idx += 1

    #3rd Attempt:
    #The next card in the deck after we have drawn the top num_drawn cards
    next_card = num_drawn
    #Go through the stars in order to see if we need to draw more cards.
    for star in stars:
        #If the next star is less than the next card to draw, then it is in our hand,
        #so we must discard it and draw 3 more.
        if star < next_card:
            next_card += num_to_redraw
        #Otherwise, there are no stars in our hand, so we're done drawing cards.
        else:
            break

    # return any(diamonds < next_card)
    # return next_card, stars, diamonds
    return FinalHand(num_cards, num_drawn, next_card, stars, diamonds)

def simulate_diamond_prob(num_trials):
    """
    The probability of having a diamond in your final hand appears to be around 0.267.
    """
    hands_with_diamond = 0
    for trial in range(num_trials):
        hands_with_diamond += simulate_draw().has_diamond()
        # hands_with_diamond += simulate_draw()
    return hands_with_diamond / num_trials

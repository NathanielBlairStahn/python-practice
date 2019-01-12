"""
Suppose you have a bar with n seats in a row. Unfriendly people arrive
and seat themselves randomly. Since they are unfriendly, they will not
sit next to anyone who is already seated (so they just leave in this case).

What is the expected occupancy fraction when no one else can be seated?
"""

import numpy as np

EMPTY = 0 #seat is empty
UNAVAILABLE = 1 #seat is empty but unavailable
OCCUPIED = 2 #seat is occupied

def seat_people(num_people):
    """Simulate seating n people."""

    seats = np.arange(num_people)
    #Using the fact that EMPTY=0
    seat_status = np.zeros(num_people, dtype=np.int)

    while any(seat_status==EMPTY):
        #Choose a random seat from those available
        seat = np.random.choice(seats[seat_status==EMPTY])
        seat_status[seat] = OCCUPIED

        if seat_status[seat-1] == EMPTY:
            seat_status[seat-1] = UNAVAILABLE
        if seat_status[(seat+1) % num_people] == EMPTY:
            seat_status[(seat+1) % num_people] = UNAVAILABLE

    return seat_status

def occupancy_fraction(seat_status):
    return (seat_status==OCCUPIED).mean()

def simulate_expected_occupancy(num_people, num_trials):
    occupancy_sum = 0
    for trial in range(num_trials):
        seat_statuses = seat_people(num_people)
        occupancy_sum += occupancy_fraction(seat_statuses)

    return occupancy_sum / num_trials

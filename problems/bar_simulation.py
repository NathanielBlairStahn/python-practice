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

def seat_people(num_seats):
    """Simulate seating people in n seats."""

    #Seats are numbered 0 to num_seats-1
    seats = np.arange(num_seats)
    #Using the fact that EMPTY=0
    seat_status = np.zeros(num_seats, dtype=np.int)

    #While a seat is available, put the next person in a random seat
    while any(seat_status==EMPTY):
        #Choose a random seat from those available, and sit there
        seat = np.random.choice(seats[seat_status==EMPTY])
        seat_status[seat] = OCCUPIED

        #Mark any adjacent EMPTY seats as unavailable
        if seat > 0 and seat_status[seat-1] == EMPTY:
            seat_status[seat-1] = UNAVAILABLE
        if seat < num_seats-1 and seat_status[seat+1] == EMPTY:
            seat_status[seat+1] = UNAVAILABLE

    return seat_status

# def seat_people_hashing(num_seats):
#     seats = set(range(num_seats))

def occupancy_fraction(seat_status):
    """Compute the fraction of seats occupied in an array of seat statuses."""
    return (seat_status==OCCUPIED).mean()

def simulate_expected_occupancy(num_seats, num_trials):
    """Run num_trials simulations to estimate the expected occupancy fraction
    for seating people in num_seats seats.
    """
    occupancy_sum = 0
    for trial in range(num_trials):
        seat_statuses = seat_people(num_seats)
        occupancy_sum += occupancy_fraction(seat_statuses)

    return occupancy_sum / num_trials

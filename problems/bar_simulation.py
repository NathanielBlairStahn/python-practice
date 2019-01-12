"""
Suppose you have a bar with n seats in a row. Unfriendly people arrive
and seat themselves randomly. Since they are unfriendly, they will not
sit next to anyone who is already seated.

What is the expected occupancy fraction when no one else can be seated?
"""

import numpy as np

EMPTY = 0 #seat is empty
UNAVAILABLE = 1 #seat is empty but unavailable
OCCUPIED = 2 #seat is occupied

def occupancy_fraction(seat_status):
    """Compute the fraction of seats occupied in an array of seat statuses."""
    return (seat_status==OCCUPIED).mean()

def seat_people(num_seats):
    """Simulate seating people in n seats.
    Returns an array of seat statuses (EMPTY, UNAVAILABLE, or OCCUPIED).

    Loop through people until no seats are left. For each iteration,
    check the seat statuses to see if any are empty. If so, choose a
    random seat from the empty ones, and update the status of the chosen
    seat and its adjacent seats.
    Use numpy array indexing to check which seats are available and to
    choose a random available seat on each iteration. This takes O(n)
    time per iteration because both the loop test and the random choice
    require accessing all n seat statuses in the array.
    Thus, one simulation runs in time O(n^2).
    """

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

def seat_people_faster(num_seats):
    """Simulate seating people in n seats using a rejection algorithm.
    Returns an array of seat statuses (EMPTY, UNAVAILABLE, or OCCUPIED).

    Assume we randomly assign n seats to n people without replacement,
    so each person from 1 to n has a unique randomly assigned seat
    between 1 and n. Each person then approaches the bar and attempts
    to sit in their assigned seat. If the seat is unavailable (i.e. taken
    or adjacent to a seat that is taken), the person leaves, and the next
    person approaches. This algorithm will take O(n) time to run one simulation.
    """

    #Assign each person fom 0 to n-1 a unique seat using a random permutation.
    seat_choices = np.random.permutation(num_seats)
    #Create an array to store the seat statuses.
    #Using the fact that EMPTY=0
    seat_status = np.zeros(num_seats, dtype=np.int)
    #Keep track of the number of remaining available seats
    remaining_seats = num_seats

    #Go through the chosen seats and seat each person if possible,
    #until we run out of available seats.
    for seat in seat_choices:
        #If the seat is available, seat the person.
        #Otherwise, don't do anything, and move onto the next person.
        if seat_status[seat] == EMPTY:
            seat_status[seat] = OCCUPIED
            remaining_seats -=1

            #Mark any adjacent EMPTY seats as unavailable
            if seat > 0 and seat_status[seat-1] == EMPTY:
                seat_status[seat-1] = UNAVAILABLE
                remaining_seats -=1
            if seat < num_seats-1 and seat_status[seat+1] == EMPTY:
                seat_status[seat+1] = UNAVAILABLE
                remaining_seats -=1

            #If there ar no seats left, we're done
            if remaining_seats == 0:
                break

    return seat_status

def seat_people_recursive(num_seats):
    """Simulate seating people in n seats using a recursive algorithm.
    Returns an array of seat statuses (EMPTY, UNAVAILABLE, or OCCUPIED).

    This runs in O(n) time, assuming numpy.random.randint(k) runs in
    constant time for any k.
    """

    #Using the fact that EMPTY=0
    seat_status = np.zeros(num_seats, dtype=np.int)
    _seat_subarray(seat_status)
    return seat_status

def _seat_subarray(seat_status):
    """Recursively choose a random seat, then seat people to the left and to the right.
    The array seat_status is assumed to be completely empty.
    """
    if len(seat_status) == 0:
        return

    #Choose a random seat and sit there
    seat = np.random.randint(len(seat_status))
    seat_status[seat] = OCCUPIED
    #print(seat_status, seat)

    #Seat people to the left, if there are seats to the left
    if seat > 0:
        seat_status[seat-1] = UNAVAILABLE
        _seat_subarray(seat_status[:seat-1])
     #Seat people to the right, if there are seats to the right
    if seat < len(seat_status)-1:
        seat_status[seat+1] = UNAVAILABLE
        _seat_subarray(seat_status[seat+2:])


def simulate_expected_occupancy(num_seats, num_trials, seating_function=seat_people_faster):
    """Run num_trials simulations to estimate the expected occupancy fraction
    for seating people in num_seats seats.
    """
    occupancy_sum = 0
    for trial in range(num_trials):
        seat_statuses = seating_function(num_seats)
        occupancy_sum += occupancy_fraction(seat_statuses)

    return occupancy_sum / num_trials

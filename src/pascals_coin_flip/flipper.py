"""
file: flipper.py

description:
    This file will contain all functions related to flipping a number
    of coins for later computation.

authors:
    - Matt London
"""
import random
from pascals_coin_flip.models import CoinResult


def flip_coin():
    """
    Flip one coin

    :return: Enum of the result
    """
    flip = random.randint(0, 1)

    return CoinResult(flip)


def flip_set(num_coins: int) -> tuple:
    """
    Now we want to flip a set of coins and return a tuple corresponding to
    which result we received

    Ex:
        If we flip 3 coins there are eight possibilities:
        HHH, HHT, HTH, HTT, THH, THT, TTH, TTT

        Since order doesn't matter, instead there are four possibilities:
            - 0 heads, 3 tails
            - 1 head, 2 tails
            - 2 heads, 1 tail
            - 3 heads, 0 tails

        This will be represented as a tuple in decreasing order of heads count,
        holding the coefficient of number of outcomes (0 or 1).

        In the case of 3 coin flips where we receive 1 head and 2 tails it will be:
        (H^0T^3, H^1T^2, H^2T^1, H^3T^0)
        (0,      1,      0,      0)

    :param num_coins: Number of coins in the set to flip
    :return: Tuple (size num_coins + 1) with outcome space set to 1
    """
    head_count = 0

    # Run the simulation to flip the coins
    for _ in range(num_coins):
        flip = flip_coin()
        if flip == CoinResult.HEADS:
            head_count += 1
        elif flip == CoinResult.TAILS:
            # Tails count is irrelevant since we can draw that from head_count
            # But it's also not needed in this computation
            pass
        else:
            raise "Function flip_coin() randint parameter error:\nRange not [0, 1]"

    # Now we build the tuple and set the corresponding space
    result = [0] * (num_coins + 1)
    result[head_count] = 1

    return tuple(result)


def flip_set_avg(num_coins: int, num_iter: int) -> tuple:
    """
    Flip a set of a given number of coins with a given number of iters

    :param num_coins: Number of coins in a set
    :param num_iter: Number of times to flip the set
    :return: A tuple with averages in each spot corresponding to coefficients
    """
    totals = [0] * (num_coins + 1)

    # Flip the set and sum totals
    for _ in range(num_iter):
        set_result = flip_set(num_coins)
        totals = tuple(a + b for a, b in zip(totals, set_result))

    # Now we average each into a probability by dividing by number of iterations
    avg = []

    for total in totals:
        avg.append(total / num_iter)

    return tuple(avg)

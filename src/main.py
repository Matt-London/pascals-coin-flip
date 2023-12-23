"""
file: main.py

description:
    This file is responsible for running the example of printing a number of
    rows in Pascal's triangle.

authors:
    - Matt London
"""
from pascals_coin_flip.flipper import flip_set_avg


def main():
    print("Hello World")


if __name__ == "__main__":
    NUM_ITER = 50_000_000
    num_coins = int(input("Enter number of coins to flip: "))
    # total_rows = int(input("Enter number of rows to print: "))

    # for num_coins in range(total_rows):

    num_adjust = 2 ** num_coins

    result = flip_set_avg(num_coins, NUM_ITER)

    print(f"{num_coins}. ", end="")

    for i in result:
        print(int(round(i * num_adjust)), end=" ")

    print()

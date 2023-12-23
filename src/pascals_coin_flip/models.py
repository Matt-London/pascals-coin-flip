"""
file: models.py

description:
    This file will contain all simple models for the program and should not
    contain extensive classes.

authors:
    - Matt London
"""
from enum import Enum


class CoinResult(Enum):
    """
    Enum to represent coin flip results
    """
    HEADS = 0
    TAILS = 1

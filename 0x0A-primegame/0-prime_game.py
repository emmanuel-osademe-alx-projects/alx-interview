#!/usr/bin/python3
"""module docs for 0-prime_game.py"""


def isWinner(x, nums):
    """returns the winner of the game"""
    maria_wins = 0
    ben_wins = 0
    if not isinstance(nums[0], int) or x < 1:
        return None
    for rounds in range(0,x):
        for n in nums:
            primes = [True] * (n + 1)
            primes[0] = primes[1] = False
			# Sieve of Eratosthenes to find all prime numbers
            for i in range(2, int(n ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False
			# Check if Maria or Ben wins the current round
            if primes.count(True) % 2 == 1:
                maria_wins += 1
            else:
                ben_wins += 1
        if maria_wins > ben_wins:
            return "Maria"
        if ben_wins > maria_wins:
            return "Ben"
        return None

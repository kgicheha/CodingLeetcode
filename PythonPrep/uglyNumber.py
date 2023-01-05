'''
263. Ugly Number

An ugly number is a positive integer whose prime factors
are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''

'''
EXAMPLE
Input: n = 6
Output: true
Explanation: 6 = 2 * 3
'''

'''
GIVEN: num
    prime numbers: can only divided fully by itself and 1
    prime factorization: process of factoring a number in terms of primes numbers
        to find the prime factor of a numbers,
            keep on dividing the original number by prime factors until we get the remainder equal to 1
            example
                prime factorization of number 30
                    we get 30/2 = 15
                    15/3 = 5
                    5/5 = 1
                    since the remainder 1, it cannot be further factorized
                    therefore 30 = 2 * 3 * 5, where 2 are the prime factors.

STEPS:
    edge case: if given number is negative, return false


RESULT: return true if given number is a positive integer whose prime factors are limited to 2,3,5
'''
def isUgly(n):
    if n < 0:
        return False
    # if (n > 0) and

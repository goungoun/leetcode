# 204. Count Primes (Medium)
# https://leetcode.com/problems/count-primes/

class Solution:
    """
    Get prime numbers less than n
    return cnt_prime_numbers

    * prime number: only divisible by one and itself

    Approach: Sieve of Eratosthenes
    List up all numbers less than n
    Exclude all its multiples as they are divisible, non-prime integers
    Remained numbers are prime numbers 
    """
    def countPrimes(self, n: int) -> int:
        if not n or n < 2:
            return 0

        # set all element to True, potentially they are prime number
        is_primes = [True] * n

        # except zero and one, prime number starts from 2
        is_primes[0] = False
        is_primes[1] = False
       
        for i in range(2, n): #for i in range(2, int(n ** 0.5) + 1):
            # If i is prime number, let's exclude its multiples
            if is_primes[i]:
                for j in range(i + i, n, i): # multiples
                    is_primes[j] = False

        return sum(is_primes)
      

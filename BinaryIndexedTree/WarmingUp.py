# The intuition of Binary Indexed Tree (a.k.a Fenwick Tree) #

# 0. Sum of Power of 2
'''
Every integer can be split be the sum of the power of 2, because 1 = 2^0 and any integer can be considered as the summation of 1.

We can do this split easily in python, as below:
'''

def splitint(N):
    Nbin = bin(N)[2:]
    Nintlist = [int(i) for i in Nbin]
    for power, digit in enumerate(reversed(Nintlist)):
        if digit == 1:
            yield power
            
            
'''
Easy to be test: 
'''
N = 200    
list(splitint(N)) # 200 = 2^3 + 2^6 + 2^7 = 
sum(2**i for i in splitint(N)) == N

'''
Take integer 13 as an example here, we can split it to 3 numbers.
13 = 2^0 + 2^2 + 2^3 = 1 + 4 + 8

Let s(13) to be the sum of the 13 elements before. s(13) can be split into 3 sub-sums:
s(13) = s(1) + s(4) + s(8)

We noticed for these 3 subsum:
1 = 2^0 
4 = 2^2
8 = 2^3
can be written as the power of 2, so cannot be split into the smaller pieces.
Similarly: s(200) = s(8) + s(64) + s(128)

Obviously, every summation function s can be split into several sub-sum, but cannot be split into smaller pieces.
'''

# 1. sum of given range
'''
Input: an integer array 
To find: the sum of the elements between indices i and j (i ≤ j).  ~O(logn)
Mutable: the array can be updated.   ~O(logn)
'''







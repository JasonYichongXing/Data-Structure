# The intuition of Binary Indexed Tree (a.k.a Fenwick Tree) #

# 0. Sum of Power of 2
'''
Every integer can be split into the sum of the power of 2, because 1 = 2^0 and any integer can be considered as the summation of 1.

We can do this split easily in python, as below:
'''

def splitint(N):
    Nbin = bin(N)[2:]
    Nintlist = [int(i) for i in Nbin]
    for power, digit in enumerate(reversed(Nintlist)):
        if digit == 1:
            yield power
            
            
'''
Easy to test: 
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
Pass

# 2. Update Binary Indexed Tree.
'''
Let's say we'd lile to change the value on index i by value_chng
First of all, obviously current index tree[i] need to be added by that value.
Then, instead of updating every the subsequent elementes after i, only partial points need to be updated.

So, how to determine those points?

We use bitwise operator AND: &
'''

def update(i, value_chng):
    while(i <= MaxN):
        tree[i] += value_chng
        i += i & -i
        
        
'''
i.e. starting from i = 1, the indexes need to update is:
1 & -1 1
2 & -2 2
4 & -4 4
8 & -8 8
16 & -16 16
32 & -32 32
64 & -64 64

if i = 3, then:
3 & -3 1
4 & -4 4
8 & -8 8
16 & -16 16
32 & -32 32
64 & -64 64
...

It will added to the nearest 2^i then, go along the 2^i+1, 2^i+2, ...

'''

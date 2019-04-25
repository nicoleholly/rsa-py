import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from nprime.pyprime import miller_rabin
##pip install nprime

## 3a. implementing gcd with Euclid's algorithm
def gcd(x,y):
	if y == 0:
		return x
	else:
		return gcd(y,x%y)


def main():
    while True:
        p = random.randint(65537, 6553700)
        if miller_rabin(p):
            break
    while True:
        q = random.randint(65537, 6553700)
        if miller_rabin(q):
            break
    print(p, q)


    ### 3b. refer to https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537
    e = 65537
    ## for security, padding seems to be more important than the size of public exponent?
    ## we can test the algorithm with small e if it takes too long time to compute.
    e_test = 3

    ### 4. multiplicative inverse


    ### 1. generate two prime #'s (nicole)
    ###     a. have a primality test
    ### 2. Times them together!!
    ### 3. Select e s.t. gcd(e, p-1,q-1) = 1 (kiwako)
    ###     a. have a gcd function
    ###     b. how to get e??
    ### 4. Calculate d (multiplicative inverse)
    ###     a. how to do that?
    ### ---
    ### 5. convert strings to nums and back again
    ### 6. Make it secure with padding && masking etc etc etc
main()

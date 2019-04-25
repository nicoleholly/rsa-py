import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from nprime.pyprime import miller_rabin
##pip install nprime

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

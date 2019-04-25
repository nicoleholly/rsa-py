




### 3a. implementing gcd with Euclid's algorithm
def gcd(x,y):
	if y == 0:
		return x
	else:
		return gcd(y,x%y)

### 3b. refer to https://crypto.stackexchange.com/questions/3110/impacts-of-not-using-rsa-exponent-of-65537
e = 65537
## for security, padding seems to be more important than the size of public exponent? 
## we can test the algorithm with small e if it takes too long time to compute.
e_test = 3

### 4. multiplicative inverse



def main():
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
main()

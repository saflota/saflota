#this approach isn't well known 
#so i wanted to share this after i spent some time to find it
def NOT_bitwise(x):
    return 2**(x.bit_length())-1-x
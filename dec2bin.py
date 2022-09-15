
def parse_input():
    return int(input())

def dec2bin(n):
    bin_repr = list()

    while n > 0:
        rest = n % 2
        n //= 2
        bin_repr.insert(0, rest)

    return bin_repr
        

def main():
    n_dec = parse_input()
    
    n_bin = dec2bin(n_dec)
    print(n_dec)

main()

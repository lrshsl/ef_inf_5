
e = 905
d = 785
n = 1007

enc = lambda msg, e, n: [
        pow(ord(ch), e) % n
        for ch in msg]

dec = lambda msg, d, n: ''.join(
        (chr(pow(ch, d) % n)
         for ch in msg))

txt = "cipher"

cipher = enc(txt, e, n)
print(' '.join(map(str, cipher)))
print(dec(cipher, d, n))

# assert dec(enc(txt, e, n), d, n) == txt

# cipher = 76, 69, 84, 887, 71, 79

# def crack(msg, e, n):
#     for i in range(n):
#         if pow(i, e) % n == msg:
#             return i

# d = crack(cipher, e=67, n=1340)
# print(d)

# print(dec(cipher, d, n))


import numpy as np

# e = 905
d = 97
n = 1333

enc = lambda msg, e, n: [
        pow(ord(ch), e) % n
        for ch in msg]

dec = lambda msg, d, n: ''.join(
        (chr(pow(ch, d) % n)
         for ch in msg))

cipher = [
        481, 546, 1064, 1230, 546, 1306, 1056, 546, 421, 1230, 1306, 1306
        ]
print(dec(cipher, d, n))

# txt = "cipher"

# cipher = enc(txt, e, n)
# print(' '.join(map(str, cipher)))
# print(dec(cipher, d, n))

# assert dec(enc(txt, e, n), d, n) == txt


# # Cracking

# cipher = 76, 69, 84, 887, 71, 79

# def crack(msg, e, n):
#     return get_key(e, n)

# def get_key(e, n):
#     for p, q in get_pq(n):
#         for d in range(1, n):
#             if e*d*(p-1)*(q-1) == 1:
#                 return d
#     return -1

# def maybe_prime_generator(n):
#     for p in range(1, n):
#         for t in range(1, n // 2):
#             if p % t == 0:
#                 break
#         else:
#             yield p

# def get_pq(n):
#     p = 1
#     q = 1
#     for p in maybe_prime_generator(n):
#         for q in maybe_prime_generator(n):
#             if p * q == n:
#                 yield p, q

# # d = crack(cipher, e=67, n=1340)
# d = crack(cipher, e=905, n=1007)
# print(d)

# # print(dec(cipher, d, n))


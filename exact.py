import csv
from functools import lru_cache
from fractions import Fraction

TURN_A = 0
TURN_B = 1

with open('config.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    a = reader.__next__()
    b = reader.__next__()

for key in a.keys():
    if key != "Which":
        a[key] = int(a[key])
        b[key] = int(b[key])

@lru_cache(maxsize = None)
def nCr(n, r):
    if r == 0: return 1
    if r == n: return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

@lru_cache(maxsize = None)
def B(k, n, p):
    return nCr(n, k) * p**k * (1-p)**(n-k)

@lru_cache(maxsize = None)
def playerA_win_prob(ahp, bhp, turn, w_attacks_left):
    if ahp <= 0: return 0
    if bhp <= 0: return 1
    if w_attacks_left > 0:
        n_a = a['w_attack']
    else:
        n_a = a['attack']
    n_b = b['attack']
    p_a = 1 - Fraction(b['defense'], 6) 
    p_b = 1 - Fraction(a['defense'], 6) 
    chance_if_A_hit = Fraction(0, 1)
    for i in range(a['attack']):
        new_attacks_left = w_attacks_left - 1
        if new_attacks_left < 0: new_attacks_left = 0
        chance_if_A_hit += B(i + 1, n_a, p_a) * playerA_win_prob(ahp, bhp - i - 1, TURN_B, new_attacks_left)
    chance_if_B_hit = Fraction(0, 1)
    for i in range(b['attack']):
        chance_if_B_hit += B(i + 1, n_b, p_b) * playerA_win_prob(ahp - i - 1, bhp, TURN_A, w_attacks_left)
    if turn == TURN_A:
        return (chance_if_A_hit + B(0, n_a, p_a) * chance_if_B_hit) / (1 - B(0, n_a, p_a) * B(0, n_b, p_b))
    else: 
        return (chance_if_B_hit + B(0, n_b, p_b) * chance_if_A_hit) / (1 - B(0, n_a, p_a) * B(0, n_b, p_b))

chance = float(playerA_win_prob(a['health'], b['health'], TURN_A, a['w_times']))
print("Chance of", a["Which"], "winning is", chance*100, "%")

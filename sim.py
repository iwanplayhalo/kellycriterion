# basic betting sim
import random
import numpy as np # for later probably
import matplotlib.pyplot as plt

def outcome(p, b = 1.0): # p is % win, b is payout 
    return b if random.random() < p else -1

def sim(n, m, p, b): #n = num steps, m = initial money, p = win%, b = payout odds
    tl = [m]
    f = ((b*p)-(1-p))/b # % of bankroll to bet assuming we go full kelly

    for i in range(n):
        m *= (1 + f * outcome(p,b))
        tl.append(m)
    return tl

n, m, p, b = 50, 100, 0.52, 1.0
paths = [sim(n,m,p,b) for i in range(200)]

for i in paths:
    plt.plot(i, alpha= 0.3)
plt.yscale("log")
plt.xlabel("bet number")
plt.ylabel("money")
plt.show()
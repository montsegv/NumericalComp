#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#

from random import choice
import random


def Coinflip():
    throw = [random.randint(1,2) for i in range(10000)]
    heads = throw.count(1)
    tails = throw.count(2)

    print('Cara: ', heads, ' y sello: ', tails)

Coinflip()
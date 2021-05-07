import random


def get_ranstr(num=10):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    res = ''
    for i in range(num):
        res += random.choice(H)

    return res

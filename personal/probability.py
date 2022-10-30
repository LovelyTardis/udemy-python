import random
import time


def probability():
    coin_flips = 0
    while( coin_flips != -1):
        try:
            coin_flips = int(input("Cuántas veces quieres tirar la moneda? "))
        except:
            continue
        result = {0: 0, 1: 0}
        for i in range(0, coin_flips):
            result[flip_coin()] += 1
        print(f"{result[0]}/{result[1]}")
    time.sleep(60)


def flip_coin():
    return random.randint(0, 1)


probability()

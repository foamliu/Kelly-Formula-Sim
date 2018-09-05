import random

import matplotlib.pyplot as plt


def gen_invest_op():
    b = random.uniform(0., 2)
    p = random.random()
    return b, p


if __name__ == '__main__':
    timestamp = 0
    balance = 100.
    balances = []
    threshold = 0.2
    while True:
        timestamp += 1

        print(balance)
        balances.append(balance)

        b, p = gen_invest_op()
        q = 1. - p

        if (b - 1) * p - q > 0:
            # play
            f = (b * p - q) / b
            win = random.random() <= p
            if win:
                balance += balance * f * (b - 1)
            else:
                balance -= balance * f

        if timestamp > 100:
            break

    plt.plot(balances)
    plt.ylabel('money')
    plt.show()

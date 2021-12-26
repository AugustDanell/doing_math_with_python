''' Assignment 5.2
    Verifying the law of large numbers, that the average value of results approaches the expected value for
    large numbers. A dice throw is simulated (assuming a balanced dice) for a certain amount of trials. As
    is seen, when the number of performed trials go towards infinity so too will the average approach the
    expected value of the dice throw.

'''

import random

def throw_dice():
    dice = random.randint(1, 6)
    return dice

def simulate_trials(l, expected_value):
    sum_trials = 0
    trials = l.pop()
    for i in range(trials):
        sum_trials += throw_dice()

    avg = sum_trials / trials

    if(len(l) >= 1):
        simulate_trials(l, expected_value)

    print('{0} trials: Average = {1}, {2} from the expected value.'.format(trials, avg, abs(avg - expected_value)))


print('Law of Large Numbers - Simulating Dice Throws.')
print('E(x) = 3.5. Simulating for amount of trials n = [100, 1000, 10000, 100000, 500000]')
print()
n = [100, 1000, 10000, 100000, 500000]
expected_value = 3.5
simulate_trials(n, expected_value)

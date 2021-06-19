import random
import robotCore.finished as rC
bet_size = random.randint(1,10)
exact_bets = random.sample(range(1,80), bet_size)
draws = [1,2,4,6,8,10,14,28,56]
no_draws = random.choice(draws)
no_draws = draws.index(no_draws) + 1
multiplier = random.randint(1,10)
start_from = "02. Feb. 2020 20:40"

rC.Robot_Core(exact_bets, no_draws, multiplier, start_from)

